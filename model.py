import tensorflow as tf
from tensorflow.keras.layers import Rescaling
from tensorflow.keras.callbacks import EarlyStopping, ReduceLROnPlateau

# Load the dataset
dataset = tf.keras.preprocessing.image_dataset_from_directory(
    r"D:\Programs\herbal\leaf_data",
    batch_size=32,
    image_size=(224, 224),
    shuffle=True
)
labels = dataset.class_names
print("Class Labels:", labels)

# Split dataset into training, validation, and test sets
def get_dataset_partitions_tf(ds, train_split=0.8, val_split=0.1, test_split=0.1, shuffle=True, shuffle_size=10000):
    assert (train_split + val_split + test_split) == 1
    if shuffle:
        ds = ds.shuffle(shuffle_size, seed=12)
    train_size = int(train_split * len(ds))
    val_size = int(val_split * len(ds))
    train_ds = ds.take(train_size)
    val_ds = ds.skip(train_size).take(val_size)
    test_ds = ds.skip(train_size + val_size)
    return train_ds, val_ds, test_ds

train_ds, val_ds, test_ds = get_dataset_partitions_tf(dataset)
print(f"Train: {len(train_ds)}, Validation: {len(val_ds)}, Test: {len(test_ds)}")

# Data augmentation for training data
data_augmentation = tf.keras.Sequential([
    tf.keras.layers.RandomFlip("horizontal_and_vertical"),
    tf.keras.layers.RandomRotation(0.2),
    tf.keras.layers.RandomZoom(0.2),
    tf.keras.layers.RandomContrast(0.2),
])

# Rescaling layer
resize_and_rescale = tf.keras.Sequential([
    tf.keras.layers.Resizing(224, 224),
    tf.keras.layers.Rescaling(1. / 255)
])

# Load the pre-trained VGG19 model
base_model = tf.keras.applications.VGG19(
    weights='imagenet',
    input_shape=(224, 224, 3),
    include_top=False,
    pooling='avg'
)
base_model.trainable = False  # Freeze the base model

# Build the model
inputs = tf.keras.Input(shape=(224, 224, 3))
x = data_augmentation(inputs)
x = resize_and_rescale(x)
x = base_model(x, training=False)
x = tf.keras.layers.Dense(256, activation='relu')(x)  # Increased dense layer size
x = tf.keras.layers.BatchNormalization()(x)  # Add Batch Normalization
x = tf.keras.layers.Dropout(0.3)(x)  # Increased dropout rate
outputs = tf.keras.layers.Dense(len(labels), activation='softmax')(x)
model = tf.keras.Model(inputs, outputs)

# Compile the model
model.compile(
    optimizer=tf.keras.optimizers.Adam(learning_rate=1e-4),
    loss='sparse_categorical_crossentropy',
    metrics=['accuracy']
)

# Callbacks
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)
reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.5, patience=3)

# Train the model
history = model.fit(
    train_ds,
    validation_data=val_ds,
    batch_size=32,
    epochs=25,  # Increased epochs
    callbacks=[early_stopping, reduce_lr]
)

# Evaluate on the test set
test_loss, test_accuracy = model.evaluate(test_ds)
print(f"Test Loss: {test_loss}, Test Accuracy: {test_accuracy}")

# Save the model
model.save('optimized_model_vgg19.h5')