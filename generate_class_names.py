import tensorflow as tf

DATASET_PATH = "dataset/train"

ds = tf.keras.utils.image_dataset_from_directory(
    DATASET_PATH,
    image_size=(224, 224),
    batch_size=32
)

class_names = ds.class_names

with open("model/class_names.txt", "w") as f:
    for name in class_names:
        f.write(name + "\n")

print("✅ class_names.txt regenerated successfully")
print("Total classes:", len(class_names))
