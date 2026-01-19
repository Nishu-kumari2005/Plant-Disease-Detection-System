import tensorflow as tf
from keras.applications import MobileNetV2
from keras.layers import Dense, GlobalAveragePooling2D
from keras.models import Model
from keras.optimizers import Adam

# -------------------------
# CONFIG
# -------------------------
IMG_SIZE = (224, 224)
BATCH_SIZE = 32
EPOCHS = 5
DATASET_PATH = "dataset/train"

# -------------------------
# LOAD DATASET (Keras 3 way)
# -------------------------
train_ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    image_size=IMG_SIZE,
    batch_size=BATCH_SIZE
)

class_names = train_ds.class_names
num_classes = len(class_names)

# Normalize images
normalization_layer = tf.keras.layers.Rescaling(1./255)
train_ds = train_ds.map(lambda x, y: (normalization_layer(x), y))

# -------------------------
# MODEL (MobileNetV2)
# -------------------------
base_model = MobileNetV2(
    weights="imagenet",
    include_top=False,
    input_shape=(224, 224, 3)
)
base_model.trainable = False

x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dense(128, activation="relu")(x)
output = Dense(num_classes, activation="softmax")(x)

model = Model(inputs=base_model.input, outputs=output)

model.compile(
    optimizer=Adam(),
    loss="sparse_categorical_crossentropy",
    metrics=["accuracy"]
)

# -------------------------
# TRAIN
# -------------------------
model.fit(train_ds, epochs=EPOCHS)


with open("model/class_names.txt", "w") as f:
    for name in class_names:
        f.write(name + "\n")


# -------------------------
# SAVE MODEL
# -------------------------
model.save("model/plant_disease_model.h5")

print("✅ Model training completed and saved.")
