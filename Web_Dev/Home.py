import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

st.set_page_config(
    page_title="WebDev"
)

#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")




st.sidebar.success("pilih halaman")
