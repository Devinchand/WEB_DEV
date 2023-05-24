import streamlit as st
import pandas as pd
import numpy as np

from PIL import Image

# Set halaman
st.set_page_config(
    page_title="Bangka Belitung Tuorism",
    page_icon="D:\coding\streamlit\WEB_DEV\photo\Iconbabel.png",
    layout="wide",
    initial_sidebar_state="auto"
)

# Logo awal
image = Image.open("D:\coding\streamlit\WEB_DEV\photo\logobabel.png")
st.image(image, use_column_width=True)
st.markdown("<h1 style='text-align: center; color: white; font-size: 30px;'>Bumi Serumpun Sebalai</h1>", unsafe_allow_html=True)

st.write("----")

# Judul
st.title("Selamat Datang di Bangka Belitung Tuorism")

# Deskripsi
st.markdown("""
Bangka Belitung tourism adalah platform yang menyediakan berbagai destinasi wisata yang ada di Provinsi Kepulauan Bangka Belitung Secara online. Hal ini dapat memudahkan wisatawan baik dalam negeri maupun luat negeri.


Melalui platform ini, Anda dapat mengakses beberapa layanan seperti:
- Rekomendasi Destinasi Wisata.
- Sejarah singkat kepulauan Bangka Belitung.
- Data penduduk.


Silakan pilih menu di navigasi untuk mengakses layanan yang Anda butuhkan.

""")



# Footer
st.markdown("---")
st.markdown("© 2023 Bangka Belitung Tourism")

