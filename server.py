from flask import Flask, request, jsonify
import models
from flask_cors import CORS
from werkzeug.contrib.fixers import ProxyFix


app = Flask(__name__)
CORS(app)
app.wsgi_app = ProxyFix(app.wsgi_app)


@app.route('/api', methods=['POST'])
def predict():
    model = request.args.get('model')
    messages = request.get_json(force=True)
    toxicity = models.predict(model, messages)
    return jsonify(toxicity)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
