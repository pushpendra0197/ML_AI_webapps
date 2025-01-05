import easyocr
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
import re
import streamlit as st
from PIL import Image
import time
import joblib
st.title("Extract Text from Image[ ◉¯]")
st.caption("Kindly upload jpeg or jpg")
file=st.file_uploader("Upload Image",type=["jpeg","jpg"])
button=st.button("Click For Conversion")
if button:
    if file:
        image=Image.open(file)
        Model=joblib.load(r"pages\converter")
        answer=Model.readtext(image)
        with st.spinner('Wait for it...'):
         time.sleep(8)
         text=[]
        for i in  answer:
            text.append(i[-2])
            final_string=" ".join(text)
    st.text(final_string)
