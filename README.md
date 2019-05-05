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

Use `./models/zoo/` directory to store your models. 
Each model package should contain the class with the following methods:

```python
class YourModel:
    def load(self):
        pass

    def preprocess(self, messages):
        pass

    def predict_probabilities(self, messages):
        pass
```

Define your model in these lines of `./models/__init__.py`:

```python
...
model_classes = {
    # Add your models here, like:
    "demo": DemoModel
}
...
```