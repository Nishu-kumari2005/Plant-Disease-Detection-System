import os
import tensorflow as tf
from flask import Flask, request, jsonify
from PIL import Image
import numpy as np

app = Flask(__name__)

# -------------------------
# ABSOLUTE PATH HANDLING
# -------------------------
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "..", "model", "plant_disease_model.h5")
CLASS_PATH = os.path.join(BASE_DIR, "..", "model", "class_names.txt")

# -------------------------
# LOAD MODEL & CLASSES
# -------------------------
model = tf.keras.models.load_model(MODEL_PATH)

with open(CLASS_PATH, "r") as f:
    class_names = [line.strip() for line in f]

# -------------------------
# PREDICT ROUTE
# -------------------------
@app.route("/predict", methods=["POST"])
def predict():
    if "image" not in request.files:
        return jsonify({"error": "No image uploaded"}), 400

    img = Image.open(request.files["image"]).convert("RGB")
    img = img.resize((224, 224))

    img_array = np.array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    preds = model.predict(img_array)[0]
    idx = int(np.argmax(preds))
    confidence = float(preds[idx] * 100)

    return jsonify({
        "disease": class_names[idx],
        "confidence": round(confidence, 2)
    })

# -------------------------
# RUN SERVER
# -------------------------
if __name__ == "__main__":
    app.run(debug=True)
