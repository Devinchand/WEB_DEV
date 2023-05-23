import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image
#Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")


#Sejarah
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\Doeloe.jpg")
st.image(image)
st.subheader("Sejarah Bumi Serumpun Sebalai")
st.write("Pelan tapi pasti, Bangka Belitung terus bersolek. Kecantikannya tak hanya dirasakan penduduk lokal. Secara nasional, termasuk dunia, juga turut merasakan pesonanya. Bangka Belitung dikenal sebagai daerah penghasil timah, memiliki pantai yang indah dan kerukunan antar etnis. Ini jelas kebanggaan, juga prestasi, mengingat Bangka Belitung merupakan provinsi baru, terbentuk pada tahun 2000.")
st.write("Provinsi Kepulauan Bangka Belitung terdiri dari dua pulau besar, yakni Pulau Bangka dan Pulau Belitung. Ada juga pulau-pulau kecil lainnya. Di zaman kerajaan, wilayah ini masuk dalam kekuasaan Sriwijaya, Majahapit, juga Mataram.")
st.write("Setelahnya, Bangka Belitung menjadi daerah jajahan Inggris. Pada 10 Desember 1816, dilaksanakan serah terima kepada pemerintah Belanda, berlangsung di Muntok.")
st.write("Pada masa penjajahan Belanda, terjadi perlawanan, dilakukan oleh Depati Barin. Perlawanan kemudian dilanjutkan putranya, Depati Amir, hingga berakhir dengan pengasingan ke Kupang, Nusa Tenggara Timur. Selama masa penjajahan, banyak kekayaan di pulau ini dirampas.")
st.write("Kendati demikian, Bangka Belitung mampu bertahan, termasuk melakukan sejumlah perlawanan. Baru pada tahun 2000, Bumi Serumpun Sebalai resmi menjadi wilayah otonom.")
st.write("Ketika itu, Pemerintah Republik Indonesia mengakui keberadaan Bangka Belitung sebagai provinsi, tak lagi menginduk bersama Sumatera Selatan. Penetapan ini dikukuhkan berdasarkan Undang-Undang Nomor 27 Tahun 2000.")
