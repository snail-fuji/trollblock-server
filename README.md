# TrollBlock server

## Installation

```bash
$ docker-compose up
```

## Usage

```bash
$ curl localhost/api?model=demo -X POST -d '{"test": "message"}'

{"test":0}
```

## Model installation

Specify an url to the model package in `requirements.txt`
Model package should contain `setup.py` and the class with the following methods:

```python
class YourModel:
    def load(self):
        pass

    def preprocess(self, messages):
        pass

    def predict_probabilities(self, messages):
        pass
```
You can see the example in the repository [HERE](https://github.com/belya/troll2vec/tree/package)

Then add `YourModel` class in `model_classes` dict of `./models/__init__.py`:

```python
from demo.model import DemoModel
...
model_classes = {
    # Add your models here, like:
    "demo": DemoModel
}
...
```