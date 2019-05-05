from models.basic_model import BasicModel
from models.demo.demo_model import DemoModel

model_classes = {
    "demo": DemoModel
}

models = {

}


def predict(model_name, messages):
    if model_name not in models:
        models[model_name] = BasicModel(model_classes[model_name]())
        models[model_name].init()
    return models[model_name].predict(messages)
