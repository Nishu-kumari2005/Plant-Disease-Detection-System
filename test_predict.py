import tensorflow as tf
import numpy as np
from PIL import Image

# -------------------------
# LOAD MODEL
# -------------------------
model = tf.keras.models.load_model("model/plant_disease_model.h5")

# -------------------------
# LOAD CLASS NAMES
# -------------------------
with open("model/class_names.txt", "r") as f:
    class_names = [line.strip() for line in f]

print("✅ Total classes loaded:", len(class_names))

# -------------------------
# LOAD & PREPROCESS IMAGE
# -------------------------
img_path = "test_leaf.webp"   # <-- put leaf image in project root
img = Image.open(img_path).convert("RGB")  # ensure 3 channels
img = img.resize((224, 224))

img_array = np.array(img) / 255.0
img_array = np.expand_dims(img_array, axis=0)

# -------------------------
# PREDICTION
# -------------------------
predictions = model.predict(img_array)
class_index = np.argmax(predictions[0])
confidence = predictions[0][class_index] * 100

# -------------------------
# OUTPUT
# -------------------------

if class_index < len(class_names):
    print("🌱 Predicted Disease:", class_names[class_index])
    print(f"✅ Confidence: {confidence:.2f}%")
else:
    print("❌ Class index out of range")
    print("Predicted index:", class_index)
    print("Available classes:", len(class_names))

