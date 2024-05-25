import logging
import dataclasses
import random
import numpy as np
import PIL.Image
import cv2
import torch
import irisml.core

from yolov9.utils.augmentations import (Albumentations, augment_hsv,
                                        copy_paste, letterbox, mixup,
                                        random_perspective)
from yolov9.utils.general import (xyn2xy, xywhn2xyxy, xyxy2xywhn)

logger = logging.getLogger(__name__)


class Task(irisml.core.TaskBase):
    """Create train and test dataset (including transform) from YoloV9 repo.
    Returned image is PIL RGB, and labels are (Nx5) tensors, (class_id, x1, y1, x2, y2 absolute).
    This is an experimental task to check parity.
    TODO: separate into common tasks and add tests.
    """

    VERSION = '0.1.0'

    @dataclasses.dataclass
    class Config:
        input_size: int
        train: bool = True
        stop_mosaic_epoch: int = int(1e5)
        mosaic: float = 0.0
        augment: bool = False
        copy_paste: float = 0.0
        mixup: float = 0.0
        scale: float = 0.5
        flipud: float = 0
        fliplr: float = 0.5

    @dataclasses.dataclass
    class Outputs:
        dataset: torch.utils.data.Dataset

    @dataclasses.dataclass
    class Inputs:
        dataset: torch.utils.data.Dataset

    def execute(self, inputs):
        return self.Outputs(YoloV9Dataset(inputs.dataset, self.config.input_size, self.config.train,
                                          self.config.stop_mosaic_epoch, self.config.mosaic, self.config.augment,
                                          self.config.mixup, self.config.copy_paste, self.config.scale,
                                          self.config.flipud, self.config.fliplr))

    def dry_run(self, inputs):
        return self.execute(inputs)


class FakeDataset(torch.utils.data.Dataset):
    def __init__(self, data):
        self._data = data

    def __len__(self):
        return len(self._data)

    def __getitem__(self, index):
        return self._data[index]


class YoloV9Dataset(torch.utils.data.Dataset):
    def __init__(self, dataset, img_size, is_train, stop_mosaic_epoch, mosaic=0.0, augment=False, mixup=0.,
                 copy_paste=0.0, scale=0.5, flipud=0.0, fliplr=0.5):

        self.dataset = dataset
        self.is_train = is_train
        self.img_size = img_size
        self.stop_mosaic_epoch = stop_mosaic_epoch
        self._epoch = 0
        self.mosaic = mosaic
        self.augment = augment
        self.mixup = mixup
        self.copy_paste = copy_paste
        self.n = len(dataset)
        self.indices = range(self.n)
        self.labels, self.segments = self.get_labels_and_segments()
        self.save_debug = False
        self.albumentations = Albumentations(size=img_size) if augment else None
        if not self.is_train:
            self.mosaic = 0
            self.augment = False

        self.hsv_h = 0.015
        self.hsv_s = 0.7
        self.hsv_v = 0.4
        self.degrees = 0.0
        self.translate = 0.1
        self.shear = 0.0
        self.perspective = 0.0
        self.flipud = flipud
        self.fliplr = fliplr

        self.scale = scale   # scale range (1-scale, 1+scale)
        self.mosaic_border = [-self.img_size // 2, -self.img_size // 2]

    def __len__(self):
        return len(self.dataset)

    def __getitem__(self, index):
        self.save_debug = False
        mosaic = self._epoch < self.stop_mosaic_epoch and self.mosaic and random.random() < self.mosaic

        if mosaic:
            # Load mosaic
            img, labels = self.load_mosaic(index)

            # MixUp augmentation
            if random.random() < self.mixup:
                img, labels = mixup(img, labels, *self.load_mosaic(random.randint(0, self.n - 1)))

        else:
            # Load image
            img, (h0, w0), (h, w) = self.load_image(index)

            # Letterbox
            shape = self.img_size  # final letterboxed shape
            img, ratio, pad = letterbox(img, shape, auto=False, scaleup=self.augment)

            labels = self.labels[index].copy()
            if labels.size:  # normalized xywh to pixel xyxy format
                labels[:, 1:] = xywhn2xyxy(labels[:, 1:], ratio[0] * w, ratio[1] * h, padw=pad[0], padh=pad[1])
            if self.augment:
                img, labels = random_perspective(img,
                                                 labels,
                                                 degrees=self.degrees,
                                                 translate=self.translate,
                                                 scale=self.scale,
                                                 shear=self.shear,
                                                 perspective=self.perspective)

        nl = len(labels)  # number of labels
        if nl:
            labels[:, 1:5] = xyxy2xywhn(labels[:, 1:5], w=img.shape[1], h=img.shape[0], clip=True, eps=1E-3)

        if self.augment:
            # Albumentations
            img, labels = self.albumentations(img, labels)
            nl = len(labels)  # update after albumentations

            # HSV color-space
            augment_hsv(img, hgain=self.hsv_h, sgain=self.hsv_s, vgain=self.hsv_v)

            # Flip up-down
            if random.random() < self.flipud:
                img = np.flipud(img)
                if nl:
                    labels[:, 2] = 1 - labels[:, 2]

            # Flip left-right
            if random.random() < self.fliplr:
                img = np.fliplr(img)
                if nl:
                    labels[:, 1] = 1 - labels[:, 1]

        labels_out = torch.zeros((nl, 6))
        if nl:
            labels_out[:, 1:] = torch.from_numpy(labels)

        if self.save_debug:
            self.save_box_img(img, labels_out[:, 2:], 'final')

        # Convert
        img = img.transpose((2, 0, 1))[::-1]  # HWC to CHW, BGR to RGB
        img = np.ascontiguousarray(img)

        img, labels_out = self.to_irisml_format(img, labels_out)

        return img, labels_out

    def load_mosaic(self, index):
        # YOLOv5 4-mosaic loader. Loads 1 image + 3 random images into a 4-image mosaic
        labels4, segments4 = [], []
        s = self.img_size
        yc, xc = (int(random.uniform(-x, 2 * s + x)) for x in self.mosaic_border)  # mosaic center x, y
        indices = [index] + random.choices(self.indices, k=3)  # 3 additional image indices
        random.shuffle(indices)

        for i, index in enumerate(indices):
            # Load image
            img, _, (h, w) = self.load_image(index)

            # place img in img4
            if i == 0:  # top left
                img4 = np.full((s * 2, s * 2, img.shape[2]), 114, dtype=np.uint8)  # base image with 4 tiles
                x1a, y1a, x2a, y2a = max(xc - w, 0), max(yc - h, 0), xc, yc  # xmin, ymin, xmax, ymax (large image)
                x1b, y1b, x2b, y2b = w - (x2a - x1a), h - (y2a - y1a), w, h  # xmin, ymin, xmax, ymax (small image)
            elif i == 1:  # top right
                x1a, y1a, x2a, y2a = xc, max(yc - h, 0), min(xc + w, s * 2), yc
                x1b, y1b, x2b, y2b = 0, h - (y2a - y1a), min(w, x2a - x1a), h
            elif i == 2:  # bottom left
                x1a, y1a, x2a, y2a = max(xc - w, 0), yc, xc, min(s * 2, yc + h)
                x1b, y1b, x2b, y2b = w - (x2a - x1a), 0, w, min(y2a - y1a, h)
            elif i == 3:  # bottom right
                x1a, y1a, x2a, y2a = xc, yc, min(xc + w, s * 2), min(s * 2, yc + h)
                x1b, y1b, x2b, y2b = 0, 0, min(w, x2a - x1a), min(y2a - y1a, h)

            img4[y1a:y2a, x1a:x2a] = img[y1b:y2b, x1b:x2b]  # img4[ymin:ymax, xmin:xmax]
            padw = x1a - x1b
            padh = y1a - y1b

            # Labels
            labels, segments = self.labels[index].copy(), self.segments[index].copy()
            if labels.size:
                labels[:, 1:] = xywhn2xyxy(labels[:, 1:], w, h, padw, padh)  # normalized xywh to pixel xyxy format
                segments = [xyn2xy(x, w, h, padw, padh) for x in segments]
            labels4.append(labels)
            segments4.extend(segments)

        # Concat/clip labels
        labels4 = np.concatenate(labels4, 0)
        for x in (labels4[:, 1:], *segments4):
            np.clip(x, 0, 2 * s, out=x)  # clip when using random_perspective()

        # Augment
        img4, labels4, segments4 = copy_paste(img4, labels4, segments4, p=self.copy_paste)
        if self.save_debug:
            self.save_box_img(img4, xyxy2xywhn(labels4[:, 1:], w=img4.shape[1], h=img4.shape[0], clip=True, eps=1E-3).astype(int), 'mosaic', convert=False)

        img4, labels4 = random_perspective(img4,
                                           labels4,
                                           segments=segments4,
                                           degrees=self.degrees,
                                           translate=self.translate,
                                           scale=self.scale,
                                           shear=self.shear,
                                           perspective=self.perspective,
                                           border=self.mosaic_border)  # border to remove

        return img4, labels4

    def load_image(self, i):
        im_pil, _ = self.dataset[i]
        # PIL to cv2
        im = np.array(im_pil)[:, :, ::-1]  # RGB to BGR
        h0, w0 = im.shape[:2]  # orig hw
        r = self.img_size / max(h0, w0)  # ratio
        if r != 1:  # if sizes are not equal
            interp = cv2.INTER_LINEAR if (self.augment or r > 1) else cv2.INTER_AREA
            im = cv2.resize(im, (int(w0 * r), int(h0 * r)), interpolation=interp)
        return im, (h0, w0), im.shape[:2]  # im, hw_original, hw_resized

    def get_labels_and_segments(self):
        labels, segments = [], []
        for _, targets in self.dataset:
            # xyxy to cx,cy,w,h
            t = targets.numpy()
            t[:, 3] -= t[:, 1]
            t[:, 4] -= t[:, 2]
            t[:, 1] += t[:, 3] / 2
            t[:, 2] += t[:, 4] / 2
            labels.append(t)

        segments = [[]] * len(labels)
        return labels, segments

    def to_irisml_format(self, img, labels):
        labels = labels[:, 1:]  # remove img idx
        labels[:, [1, 2]] -= labels[:, [3, 4]] / 2  # xy center to top-left corner
        labels[:, [3, 4]] += labels[:, [1, 2]]

        # CHW to HWC
        img = img.transpose((1, 2, 0))
        img = PIL.Image.fromarray(img)
        return img, torch.tensor(labels)

    def set_epoch(self, epoch: int):
        self._epoch = epoch
        mosaic = self._epoch < self.stop_mosaic_epoch and self.mosaic and random.random() < self.mosaic
        if not mosaic:
            logger.warning(f"mosaic closed at epoch {epoch}")
