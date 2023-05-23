import streamlit as st
import pandas as pd
import numpy as np

from gsheetsdb import connect
from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Menu/tabs
tab1, tab2 = st.tabs(["Data penduduk", "Data Wisatawan"])

#Sejarah
with tab1 :
    st.header("Data Penduduk")
    sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
    sheet_name = "datapenduduk"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    datapenduduk = pd.read_csv(url)


#data
with tab2 :
    st.header("Data Wisatawan")
    sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
    sheet_name = "dataturis"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    dataturis = pd.read_csv(url)


