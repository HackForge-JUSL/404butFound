from flask import Flask, request, jsonify
import tensorflow as tf
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.densenet import preprocess_input
from tensorflow.keras.applications.vgg16 import preprocess_input as preprocess_input_mri
import numpy as np
import os
from flask_cors import CORS
import json

app = Flask(__name__)
app.debug = True
CORS(app)

# Load the models here


# Backend routes
@app.route('/predict-ct', methods=['POST'])
def predict_ct():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load and preprocess the image
    img = request.files['image']
    img_path = f"tmp/{img.filename}"  # Save the file temporarily
    img.save(img_path)

    # Remove the temporary image file
    os.remove(img_path)

    # Return the response in JSON format
    return jsonify(response)


@app.route('/predict-mri', methods=['POST'])
def predict_mri():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load and preprocess the image
    img = request.files['image']
    img_path = f"tmp/{img.filename}"  # Save the file temporarily
    img.save(img_path)

    # Remove the temporary image file
    os.remove(img_path)

    # Return the response in JSON format
    return jsonify(response)


@app.route('/pneumonia', methods=['POST'])
def pneumonia_prediction():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load and preprocess the image
    img = request.files['image']
    img_path = f"tmp/{img.filename}"  # Save the file temporarily
    img.save(img_path)

    # Remove the temporary image file
    os.remove(img_path)

    # Return the response in JSON format
    return jsonify(response)


@app.route('/cancer-prediction', methods=['POST'])
def cancer_prediction():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load and preprocess the image
    img = request.files['image']
    img_path = f"tmp/{img.filename}"  # Save the file temporarily
    img.save(img_path)

    # Remove the temporary image file
    os.remove(img_path)

    # Return the response in JSON format
    return jsonify(response)


# Test route
@app.route('/', methods=['GET'])
def welcome():
    return "Hi"


if __name__ == '__main__':
    app.run(port=8000)
