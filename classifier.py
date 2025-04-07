# import tensorflow as tf
# from tensorflow.keras.models import load_model
# from tensorflow.keras.preprocessing import image
# import numpy as np
# from PIL import Image
# import io
#
# IMAGE_SIZE = (180, 180)
# THRESHOLD = 0.5
#
# def preprocess_image(image_data):
#     """Предсказывает класс изображения (кошка или собака)."""
#     img = Image.open(io.BytesIO(image_data)).resize((180, 180))
#     img_array = image.img_to_array(img)
#     img_array = np.expand_dims(img_array, axis=0)
#     img_array /= 255.0  # Нормализация
#
#
#
# def load_and_preprocess_image(path: str):
#     image_data = tf.keras.preprocessing.image.load_img(
#         path, target_size=IMAGE_SIZE
#     )
#     return preprocess_image(image_data)
#
# def classify(model, image_path: str):
#     preprocessed_image = load_and_preprocess_image(image_path)
#     predictions = model.predict(preprocessed_image)
#     score = predictions[0][0]
#
#     label = "cat" if score <= THRESHOLD else "dog"
#     prob = 1 - score if label == "cat" else score
#
#     return label, prob
