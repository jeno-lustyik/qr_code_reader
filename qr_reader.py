import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
import streamlit as st
from PIL import Image

st.title('QR Code Reader v0.5')

img = st.file_uploader('Upload your QR image here')



if img is not None:
    img = Image.open(img)
    img.save('img.jpg')
    img = cv.imread('img.jpg')
    qr = cv.QRCodeDetector()
    x, y, string = qr.detectAndDecode(img)

    st.text(f'Your QR code contains the following:\n\n{x}')


