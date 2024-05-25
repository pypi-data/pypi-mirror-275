import json
import pathlib
import tempfile
import unittest
from irisml.tasks.load_yolov9_prediction_results import Task


class TestLoadYolov9PredictionResults(unittest.TestCase):
    def test_simple(self):
        with tempfile.TemporaryDirectory() as temp_dir:
            temp_dir = pathlib.Path(temp_dir)
            predictions_path = temp_dir / 'predictions.json'
            dataset_path = temp_dir / 'dataset.json'
            predictions_path.write_text(json.dumps([{'image_id': 0, 'category_id': 0, 'score': 0.5, 'bbox': [0, 0, 64, 64]},
                                                    {'image_id': 0, 'category_id': 1, 'score': 1.0, 'bbox': [0, 0, 128, 128]},
                                                    {'image_id': 1, 'category_id': 0, 'score': 0.25, 'bbox': [16, 16, 48, 48]}]))

            dataset_path.write_text(json.dumps({'images': [{'id': 0, 'width': 128, 'height': 128},
                                                           {'id': 1, 'width': 64, 'height': 64}],
                                                'annotations': [{'image_id': 0, 'category_id': 0, 'bbox': [0, 0, 32, 32]},
                                                                {'image_id': 0, 'category_id': 1, 'bbox': [0, 0, 128, 128]}]}))

            outputs = Task(Task.Config(predictions_path=predictions_path, dataset_path=dataset_path)).execute(Task.Inputs())

            self.assertEqual(len(outputs.predictions), 2)
            self.assertEqual(len(outputs.targets), 2)
            self.assertEqual(outputs.predictions[0].shape, (2, 6))
            self.assertEqual(outputs.targets[0].shape, (2, 5))
            self.assertEqual(outputs.predictions[1].shape, (1, 6))
            self.assertEqual(outputs.targets[1].shape, (0, 5))
            self.assertEqual(outputs.predictions[0].tolist(), [[0, 0.5, 0, 0, 0.5, 0.5], [1, 1.0, 0.0, 0.0, 1.0, 1.0]])
            self.assertEqual(outputs.targets[0].tolist(), [[0, 0, 0, 0.25, 0.25], [1, 0, 0, 1.0, 1.0]])
            self.assertEqual(outputs.predictions[1].tolist(), [[0, 0.25, 0.25, 0.25, 1.0, 1.0]])


