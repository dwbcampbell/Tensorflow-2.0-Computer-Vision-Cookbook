import matplotlib.pyplot as plt
import numpy as np
from keras.applications import imagenet_utils
from keras.applications.inception_v3 import *
from keras.preprocessing.image import *

model = InceptionV3(weights='imagenet')

image = load_img('dog.jpg', target_size=(299, 299))

image = img_to_array(image)
image = np.expand_dims(image, axis=0)

image = preprocess_input(image)

predictions = model.predict(image)
prediction_matrix = (imagenet_utils
                     .decode_predictions(predictions))

for i in range(5):
    imagenet_id, label, probability = prediction_matrix[0][i]
    print(f'{i + 1}. {label}: {probability * 100:.3f}%')

_, label, _ = prediction_matrix[0][0]
plt.figure()
plt.title(f'Label: {label}.')
original = load_img('dog.jpg')
original = img_to_array(original)
plt.imshow(original / 255.0)
plt.show()
