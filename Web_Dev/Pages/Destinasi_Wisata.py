import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Menu/tabs
tab1, tab2 = st.tabs(["Pulau Bangka", "Pulau Belitung"])

#Sejarah
tab1.subheader("Pulau bangka")


#data
tab2.subheader("Pulau Belitung")


