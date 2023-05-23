import streamlit as st
import pandas as pd #if you will
import gspread
from google.oauth2 import service_account

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets","https://www.googleapis.com/auth/drive"
    ],
)
conn = connect(credentials=credentials)
client=gspread.authorize(credentials)

sheet_id = "1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo"
sheet_name = "datapenduduk"
url = f"https://docs.google.com/spreadsheets/d/{sheet_id}/gviz/tq?tqx=out:csv&sheet={sheet_name}"
datapenduduk = pd.read_csv(url)
