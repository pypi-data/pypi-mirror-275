import dataclasses
import logging
import pathlib
import typing
import torch
import yolov9.models.yolo
import yolov9.utils.general
import yolov9.utils.loss_tal
import yolov9.utils.loss_tal_dual
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Create a YoloV9 model using the Yolov9 library.

    Config:
        model_name ('yolov9-c', 'yolov9-e', 'yolov9'): The model name to create.
        num_classes (int): The number of classes in the dataset.
        nms_conf_threshold (float): The confidence threshold for non-maximum suppression.
        nms_iou_threshold (float): The IoU threshold for non-maximum suppression.
    """

    VERSION = '0.1.1'

    @dataclasses.dataclass
    class Config:
        model_name: typing.Literal['yolov9c', 'yolov9e', 'yolov9', 'gelanc', 'gelane', 'gelan']
        num_classes: int
        nms_conf_threshold: float = 0.001
        nms_iou_threshold: float = 0.7

    @dataclasses.dataclass
    class Outputs:
        model: torch.nn.Module

    def execute(self, inputs):
        logger.info(f"Creating YoloV9 model. name={self.config.model_name}, num_classes={self.config.num_classes}")
        config_filepath = pathlib.Path(__file__).parent / 'resources' / f'{self.config.model_name}.yaml'
        if not config_filepath.exists():
            raise ValueError(f"Unknown model name: {self.config.model_name}")

        yolo_model = yolov9.models.yolo.DetectionModel(config_filepath, nc=self.config.num_classes)
        yolo_model.hyp = {'cls_pw': 1.0, 'fl_gamma': 0.0}  # Required by ComputeLoss
        has_dual_loss = self.config.model_name.startswith('yolov9')  # yolov9 model has two detection heads
        return self.Outputs(YoloV9DetectionModel(yolo_model, has_dual_loss, self.config.nms_conf_threshold, self.config.nms_iou_threshold))

    def dry_run(self, inputs):
        return self.execute(inputs)


class YoloV9DetectionModel(torch.nn.Module):
    def __init__(self, yolo_model, has_dual_loss, nms_conf_threshold, nms_iou_threshold):
        super().__init__()
        self._model = yolo_model
        self._has_dual_loss = has_dual_loss
        self._nms_conf_threshold = nms_conf_threshold
        self._nms_iou_threshold = nms_iou_threshold
        loss_class = yolov9.utils.loss_tal_dual.ComputeLoss if has_dual_loss else yolov9.utils.loss_tal.ComputeLoss
        self._loss = loss_class(self._model)

    def training_step(self, inputs, targets):
        # Yolo expectes targets to be (N, 6) where N is the number of boxes in the batch.
        # The 6 columns are: image_index, class_id, x, y, w, h
        targets = torch.cat([self._add_image_index_to_targets(t, i) for i, t in enumerate(targets)])
        assert targets.shape[1] == 6, "Targets should have 6 columns: image_index, class, x, y, x2, y2"
        self._loss.to(inputs.device)

        # Convert targets from (x1, y1, x2, y2) to (cx, cy, w, h)
        targets[:, 4] -= targets[:, 2]
        targets[:, 5] -= targets[:, 3]
        targets[:, 2] += targets[:, 4] / 2
        targets[:, 3] += targets[:, 5] / 2

        features = self._model(inputs)
        loss, _ = self._loss(features, targets)
        return {'loss': loss}

    def prediction_step(self, inputs):
        pred = self._model(inputs)
        if self._has_dual_loss:
            assert isinstance(pred[0], list)
            pred = pred[0][1]

        yolo_predictions = yolov9.utils.general.non_max_suppression(pred, self._nms_conf_threshold, self._nms_iou_threshold, labels=[], multi_label=True, agnostic=False, max_det=300)
        for p in yolo_predictions:
            # Convert [x,y,x2,y2,conf,cls] to [cls,conf,x,y,x2,y2]
            p[:, [0, 1, 2, 3, 4, 5]] = p[:, [5, 4, 0, 1, 2, 3]]
            p[:, (2, 4)] /= inputs.shape[3]  # Normalize x
            p[:, (3, 5)] /= inputs.shape[2]

        return yolo_predictions

    def load_state_dict(self, *args, **kwargs):
        self._model.load_state_dict(*args, **kwargs)

    def state_dict(self):
        return self._model.state_dict()

    @staticmethod
    def _add_image_index_to_targets(targets: torch.Tensor, image_index):
        return torch.cat([torch.full((targets.shape[0], 1), image_index, device=targets.device), targets], dim=1)
