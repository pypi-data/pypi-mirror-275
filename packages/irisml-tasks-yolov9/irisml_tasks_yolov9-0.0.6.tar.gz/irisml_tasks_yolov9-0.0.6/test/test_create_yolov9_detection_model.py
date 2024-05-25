import unittest
import torch
from irisml.tasks.create_yolov9_detection_model import Task

class TestCreateYolov9DetectionModel(unittest.TestCase):
    def test_yolov9(self):
        model = Task(Task.Config(model_name='yolov9c', num_classes=3)).execute(Task.Inputs()).model

        self.assertIsInstance(model, torch.nn.Module)
        outputs = model.training_step(torch.rand(2, 3, 32, 32), [torch.zeros(0, 5), torch.tensor([[0, 0.0, 0.0, 1.0, 1.0]])])
        self.assertIsInstance(outputs, dict)
        self.assertIsInstance(outputs['loss'], torch.Tensor)

        outputs = model.prediction_step(torch.rand(2, 3, 32, 32))
        self.assertIsInstance(outputs, list)
        self.assertEqual(len(outputs), 2)
        self.assertIsInstance(outputs[0], torch.Tensor)
        self.assertIsInstance(outputs[1], torch.Tensor)

    def test_gelan(self):
        model = Task(Task.Config(model_name='gelanc', num_classes=3)).execute(Task.Inputs()).model

        self.assertIsInstance(model, torch.nn.Module)
        outputs = model.training_step(torch.rand(2, 3, 32, 32), [torch.zeros(0, 5), torch.tensor([[0, 0.0, 0.0, 1.0, 1.0]])])
        self.assertIsInstance(outputs, dict)
        self.assertIsInstance(outputs['loss'], torch.Tensor)

        outputs = model.prediction_step(torch.rand(2, 3, 32, 32))
        self.assertIsInstance(outputs, list)
        self.assertEqual(len(outputs), 2)
        self.assertIsInstance(outputs[0], torch.Tensor)
        self.assertIsInstance(outputs[1], torch.Tensor)
