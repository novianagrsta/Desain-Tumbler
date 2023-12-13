import streamlit as st
import numpy as np
import cv2
import PIL.Image as im
from helper import *

st.title('Custom Tumbler')

tumbler_image = im.open('tumbler3.jpeg')
st.image(tumbler_image)

tumbler_image_cv = read_image('tumbler3.jpeg')  # for OpenCV

color_image = st.file_uploader(
    'Upload an image of your custom color/pattern here', type=['png', 'jpeg', 'jpg'])

if color_image is not None:
    try:
        # Konversi gambar yang diunggah ke dalam bentuk yang dapat diproses oleh OpenCV
        file_bytes = np.asarray(bytearray(color_image.read()), dtype=np.uint8)
        color_image_cv = cv2.imdecode(file_bytes, 1)
        color_image_cv = cv2.cvtColor(color_image_cv, cv2.COLOR_BGR2RGB)

        # Memastikan kedua gambar memiliki ukuran yang sama sebelum diproses
        tumbler_image_cv, color_image_cv = resize_to_img1(tumbler_image_cv, color_image_cv)

        mask = create_custom_mask(tumbler_image_cv)
        result = create_custom_color(tumbler_image_cv, color_image_cv, mask)
        st.image(result)

    except Exception as e:
        st.error(f'Error processing image: {e}')
