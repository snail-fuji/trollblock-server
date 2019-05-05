class DemoModel:
    def load(self):
        print("Demo model loaded")

    def preprocess(self, messages):
        return messages

    def predict_probabilities(self, messages):
        print("Demo model called")
        return [0 for _ in messages]