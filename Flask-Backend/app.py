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
ctmodel = load_model('Models/ct-scan/chest_CT_SCAN-DenseNet201.hdf5')

# Load the MRI model
mrimodel = load_model('Models/MRI/VGG16-Brain-Tumor-MRI-3.h5')

# Load the pneumonia model
pneumonia_model = load_model("Models/PNEUMONIA/pneumonia_model.h5")

cancerModel = load_model("Models\LUNG-CANCER\lung cancer_final_99.h5")
cancerModel.compile(optimizer='rmsprop',
                    loss=tf.keras.losses.SparseCategoricalCrossentropy(
                        from_logits=True),
                    metrics=['accuracy'])


class NumpyInt64Encoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, np.int64):
            return int(obj)
        return super().default(obj)


# Backend routes
@app.route('/predict-ct', methods=['POST'])
def predict_ct():
    if 'image' not in request.files:
        return jsonify({'error': 'No image file provided'})

    # Load and preprocess the image
    img = request.files['image']
    img_path = f"tmp/{img.filename}"  # Save the file temporarily
    img.save(img_path)

    img = image.load_img(img_path, target_size=(460, 460))
    img = image.img_to_array(img)
    img = np.expand_dims(img, axis=0)
    img = preprocess_input(img)

    # Make predictions on the image
    predictions = ctmodel.predict(img)

    # Interpret the predictions
    class_labels = ['Adenocarcinoma', 'Large.cell.carcinoma',
                    'Normal', 'Squamous.cell.carcinoma']
    predicted_class_index = np.argmax(predictions, axis=1)
    predicted_class_label = class_labels[predicted_class_index[0]]

    # Prepare the response
    response = {
        'predicted_class': predicted_class_label,
        'probability': float(predictions[0][predicted_class_index[0]]) * 100
    }

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
