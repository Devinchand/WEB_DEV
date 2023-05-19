import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.subheader("Bumi Serumpun Sebalai")

#Menu/tabs
tab1, tab2, tab3 = st.tabs(["Sejarah", "Data Penduduk","Destinasi Wisata"])
data = np.random.randn(10, 1)

#Sejarah
tab1.subheader("Sejarah Bumi Serumpun Sebalai")
tab1.line_chart(data)

#data
tab2.subheader("Data penduduk ")
tab2.write(data)

#wisata
tab3.subheader("Destinasi Wisata")
tab3.write(data)


#Side_bar
side = st.sidebar.radio("Menu", ["Sejarah", "Data Penduduk","Destinasi Wisata"])

if side == "Sejarah":
    st.tabs(["Sejarah"])
if side == "Data Penduduk":
    st.tabs(["Data Penduduk"])
if side == "Destinasi Wisata":
    st.tabs(["Destinasi Wisata"])
