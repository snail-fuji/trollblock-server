class BasicModel:
    def __init__(self, decorated_model):
        self.model = decorated_model

    def init(self):
        self._load()

    def _load(self):
        self.model.load()

    def predict(self, messages_with_ids):
        keys = [key for key in messages_with_ids.keys()]
        messages = [messages_with_ids[key] for key in keys]
        preprocessed_messages = self.preprocess(messages)
        if preprocessed_messages:
            probabilities = self._predict_probabilities(preprocessed_messages)
        else:
            probabilities = []
        return dict(zip(keys, probabilities))

    def preprocess(self, messages):
        messages = [message.strip() for message in messages]
        messages = [message for message in messages if message]
        return self._preprocess(messages)

    def _preprocess(self, messages):
        return self.model.preprocess(messages)

    def _predict_probabilities(self, messages):
        return self.model.predict_probabilities(messages)