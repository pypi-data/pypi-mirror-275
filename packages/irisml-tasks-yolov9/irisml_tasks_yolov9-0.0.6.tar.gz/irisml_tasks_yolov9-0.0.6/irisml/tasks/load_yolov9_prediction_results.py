import collections
import dataclasses
import json
import logging
import pathlib
import torch
import irisml.core

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Load prediction results of the official YoloV9 validation script.

    Config:
        predictions_path (Path): Path to the JSON file containing the predictions. Example: runs/val/exp0/yolov9-c_predictions.json
        dataset_path (Path): Path to the JSON file containing the dataset. Example: datasets/coco/annotations/instances_val2017.json
    """
    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        predictions_path: pathlib.Path
        dataset_path: pathlib.Path

    @dataclasses.dataclass
    class Outputs:
        predictions: list[torch.Tensor]
        targets: list[torch.Tensor]

    def execute(self, inputs):
        logger.info(f'Loading predictions from {self.config.predictions_path} and dataset from {self.config.dataset_path}')
        predictions_data = json.loads(self.config.predictions_path.read_text())
        dataset_data = json.loads(self.config.dataset_path.read_text())
        predictions_by_image_id = collections.defaultdict(list)
        for p in predictions_data:
            predictions_by_image_id[p['image_id']].append(p)

        annotations_by_image_id = collections.defaultdict(list)
        for annotation in dataset_data['annotations']:
            image_id = annotation['image_id']
            annotations_by_image_id[image_id].append(annotation)

        all_predictions = []
        all_targets = []
        for image in dataset_data['images']:
            image_id = image['id']
            width = image['width']
            height = image['height']
            predictions = torch.Tensor([[p['category_id'], p['score'], *_convert_bbox(p['bbox'], width, height)] for p in predictions_by_image_id[image_id]]).view(-1, 6)
            targets = torch.Tensor([[a['category_id'], *_convert_bbox(a['bbox'], width, height)] for a in annotations_by_image_id[image_id]]).view(-1, 5)

            all_predictions.append(predictions)
            all_targets.append(targets)

        logger.info(f'Loaded {len(all_predictions)} predictions')
        assert len(all_predictions) == len(all_targets)
        return self.Outputs(predictions=all_predictions, targets=all_targets)

    def dry_run(self, inputs):
        return self.Outputs(predictions=[], targets=[])


def _convert_bbox(bbox, width, height):
    x, y, w, h = bbox
    return x / width, y / height, (x + w) / width, (y + h) / height
