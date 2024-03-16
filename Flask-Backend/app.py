from flask import Flask, request, jsonify

import numpy as np
import os
from flask_cors import CORS
import json

app = Flask(__name__)
app.debug = True
CORS(app)


@app.route('/', methods=['GET'])
def welcome():
    return "Hi"


if __name__ == '__main__':
    app.run(port=8000)
