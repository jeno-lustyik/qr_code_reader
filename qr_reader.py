import cv2 as cv
import streamlit as st
from PIL import Image

st.title('QR Code Reader')

img = st.file_uploader('Upload your QR image here')

if img is not None:
    img = Image.open(img)
    img.save('img.jpg')
    img = cv.imread('img.jpg')
    qr = cv.QRCodeDetector()
    x, y, string = qr.detectAndDecode(img)

    st.text(f'Your QR code contains the following:\n\n{x}')
