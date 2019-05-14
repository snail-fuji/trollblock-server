from demo.utils.utils import demo_load


class DemoModel:
    def load(self):
        demo_load()

    def preprocess(self, messages):
        return messages

    def predict_probabilities(self, messages):
        print("Demo model called")
        return [0 for _ in messages]