import tensorflow as tf
from tensorflow.keras.applications import VGG16
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D
from tensorflow.keras.preprocessing.image import ImageDataGenerator
import matplotlib.pyplot as plt

# Step 2: Use GPU
device_name = tf.test.gpu_device_name()
print('GPU found' if device_name else 'No GPU found')

# Step 3: Set dataset path and parameters
dataset_path = '/content/extracted_dataset/tablet_dataset'
img_size = (100, 470)  # Smaller image size for speed
batch_size = 64        # Larger batch size to reduce steps per epoch

# Step 4: Create data generators
datagen = ImageDataGenerator(rescale=1./255, validation_split=0.2)

train_data = datagen.flow_from_directory(
    dataset_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='training',
    shuffle=True
)

val_data = datagen.flow_from_directory(
    dataset_path,
    target_size=img_size,
    batch_size=batch_size,
    class_mode='categorical',
    subset='validation'
)

# Step 5: Build VGG16-based model
base_model = VGG16(weights='imagenet', include_top=False, input_shape=(160, 160, 3))
base_model.trainable = False  # Freeze base model

vgg_model = Sequential([
    base_model,
    GlobalAveragePooling2D(),
    Dense(128, activation='relu'),
    Dense(train_data.num_classes, activation='softmax')
])

vgg_model.compile(optimizer='adam', loss='categorical_crossentropy', metrics=['accuracy'])

# Step 6: Train the model
print("Training VGG16 (Fast Setup)...")
vgg_history = vgg_model.fit(
    train_data,
    validation_data=val_data,
    epochs=30,
    verbose=1
)

# Step 7: Plot training vs validation accuracy
plt.figure(figsize=(8, 5))
plt.plot(vgg_history.history['accuracy'], label='Train Accuracy')
plt.plot(vgg_history.history['val_accuracy'], label='Validation Accuracy')
plt.title('VGG16 Training vs Validation Accuracy')
plt.xlabel('Epoch')
plt.ylabel('Accuracy')
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
