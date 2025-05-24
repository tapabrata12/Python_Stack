from pathlib import Path
import streamlit as st
import tensorflow as tf
import numpy as np
from tensorflow.keras.preprocessing import image
from PIL import Image

# load the model
directory = Path(__file__).parent.absolute()
model_path = directory / 'cat_dog_classifier.h5'
model = tf.keras.models.load_model(str(model_path))

# Streamlit UI
st.title('🐶🐱 Cat vs. Dog Classifier')
st.write("Upload an image, and the model will predict whether it's a cat or a dog.")

# Upload image
uploaded_file = st.file_uploader("Choose an image...", type=['jpg', 'png', 'jpeg'])

if uploaded_file is not None:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_container_width=True)

    img = img.resize((150, 150))
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)

    prediction = model.predict(img_array)
    result = "🐶 Dog" if prediction[0][0] > 0.5 else "🐱 Cat"

    st.subheader("Prediction:")
    st.success(f"The model predicts: **{result}**")
