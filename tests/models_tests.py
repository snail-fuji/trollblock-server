import unittest
import models
from models.basic_model import BasicModel
from unittest.mock import MagicMock, Mock, call
from collections import OrderedDict


class ModelsTestCase(unittest.TestCase):
    def predict(self, messages):
        pass

    def preprocess(self, messages):
        pass

    def load(self):
        self.initialized = True

    def test_predict(self):
        test_messages = {
            "id1": "TestMessage1"
        }
        test_predictions = {
            "id1": 0
        }
        self.predict = MagicMock(return_value=test_predictions)
        models.models = {
            "test": self
        }
        result = models.predict("test", test_messages)
        self.predict.assert_any_call(test_messages)
        self.assertSequenceEqual(result, test_predictions)

    def test_init_model(self):
        models.model_classes = {
            "test": ModelsTestCase
        }
        models.predict("test", {})
        assert models.models["test"].model.initialized


class BasicModelTestCase(unittest.TestCase):
    def test_init(self):
        model = BasicModel(self)
        self.load = MagicMock()
        model.init()
        self.load.assert_any_call()

    def test_predict(self):
        test_messages = ["TestMessage2", "TestMessage1"]
        test_messages_with_ids = OrderedDict([
            ("id{}".format(i), message)
            for i, message in enumerate(test_messages)
        ])
        test_probabilities = [1, 0]
        test_preprocessed_messages = [
            message + "_preprocessed"
            for message in test_messages
        ]
        model = BasicModel(self)
        self.preprocess = MagicMock(return_value=test_preprocessed_messages)
        self.predict_probabilities = MagicMock(return_value=test_probabilities)
        process = Mock(
            preprocess=self.preprocess,
            predict=self.predict_probabilities
        )

        result = model.predict(test_messages_with_ids)

        process.assert_has_calls([
            call.preprocess(test_messages),
            call.predict(test_preprocessed_messages)
        ])

        self.assertSequenceEqual(
            result,
            dict(
                zip(test_messages_with_ids.keys(), test_probabilities)
            )
        )

    def test_predict_skip_empty_messages(self):
        test_messages = {
            "id": "    "
        }
        model = BasicModel(self)
        self.preprocess = MagicMock(side_effect=lambda x: x)
        self.predict_probabilities = MagicMock()
        result = model.predict(test_messages)

        assert result == {}
        self.predict_probabilities.assert_not_called()
