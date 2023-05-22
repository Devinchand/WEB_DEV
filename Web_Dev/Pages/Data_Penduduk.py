import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Menu/tabs
tab1, tab2, tab3 = st.tabs(["Sejarah", "Data Penduduk","Destinasi Wisata"])

#Sejarah
tab1.subheader("Sejarah Bumi Serumpun Sebalai")


#data
tab2.subheader("Data penduduk ")


#wisata
tab3.subheader("Destinasi Wisata")

