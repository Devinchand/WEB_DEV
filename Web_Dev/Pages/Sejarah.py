import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Sejarah
st.subheader("Sejarah Bumi Serumpun Sebalai")
st.write('Pelan tapi pasti, Bangka Belitung terus bersolek. Kecantikannya tak hanya dirasakan penduduk lokal. Secara nasional, termasuk dunia, juga turut merasakan pesonanya. Ini jelas kebanggaan, juga prestasi, mengingat Bangka Belitung merupakan provinsi baru, terbentuk pada tahun 2000.')
st.write('Provinsi Kepulauan Bangka Belitung terdiri dari dua pulau besar, yakni Pulau Bangka dan Pulau Belitung. Ada juga pulau-pulau kecil lainnya. Di zaman kerajaan, wilayah ini masuk dalam kekuasaan Sriwijaya, Majahapit, juga Mataram.ru')

