import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

from gsheetsdb import connect
from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Menu/tabs
tab1, tab2 = st.tabs(["Data penduduk", "Data Wisatawan"])

#DATA PENDUDUK
with tab1 :
    st.header("Data Penduduk")
    sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
    sheet_name = "datapenduduk"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    datapenduduk = pd.read_csv(url)
    st.caption('Jumlah Penduduk yang Terdaftar Pada Tahun 2021 dan 2022')
    datapenduduk['2021'] = pd.to_numeric(datapenduduk['2021'], errors='coerce')  # Mengubah kolom menjadi tipe data numerik
    datapenduduk['2022'] = pd.to_numeric(datapenduduk['2022'], errors='coerce')  # Mengubah kolom menjadi tipe data numerik
    st.write(datapenduduk)

    # Bar chart untuk data penduduk taun 2021
    fig = go.Figure(data=[go.Bar(x=datapenduduk['Kabupaten/Kota'], y=datapenduduk['2021'])])
    fig.update_layout(title='Grafik Jumlah Penduduk 2021', xaxis_title='Kabupaten/Kota', yaxis_title='2021')
    st.plotly_chart(fig)
    st.caption('Jumlah Total Penduduk di Tahun 2021 Sebanyak 1.473.165 Juta Jiwa')

    st.write("----")

    # Bar chart untuk data penduduk tahun 2022
    fig = go.Figure(data=[go.Bar(x=datapenduduk['Kabupaten/Kota'], y=datapenduduk['2022'])])
    fig.update_layout(title='Grafik Jumlah Penduduk 2022', xaxis_title='Kabupaten/Kota', yaxis_title='2022')
    st.plotly_chart(fig)
    st.caption('Jumlah Total Penduduk di Tahun 2022 Sebanyak 1.494.621 Juta Jiwa')

    
#DATA WISATAWAN
with tab2 :
    st.header("Data Wisatawan Tahun 2018")
    sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
    sheet_name = "dataturis"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    dataturis = pd.read_csv(url)
    st.caption('Dihitung dalam (ribu)')
    st.write(dataturis)

    st.header("Data Wisatawan Tahun 2019")
    sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
    sheet_name = "dataturis2"
    url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
    dataturis2 = pd.read_csv(url)
    st.caption('Dihitung dalam (ribu)')
    st.write(dataturis2)


