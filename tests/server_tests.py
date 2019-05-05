import unittest
import server
import models
import json
from unittest.mock import MagicMock


class ServerTestCase(unittest.TestCase):
    def test_predict(self):
        server.app.config['TESTING'] = True
        models.models["test"] = self
        test_probabilities = {
            "id": 1
        }
        self.predict = MagicMock(return_value=test_probabilities)
        test_messages = {
            "id": "test_message"
        }
        test_messages_json = json.dumps(test_messages)
        client = server.app.test_client()
        response = client.post('/api?model=test', data=test_messages_json)
        self.predict.assert_any_call(test_messages)
        self.assertSequenceEqual(response.json, test_probabilities)

