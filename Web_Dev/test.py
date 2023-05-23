import gsheetsdb
import streamlit as st
import pandas as pd

st.title("Connect to Google Sheets")
gsheet_url = "https://docs.google.com/spreadsheets/d/1s1MSs8-bu_KIgbC33mVNy_zrlBnSPhD6YR91qW0sHJo/edit?usp=sharing"
conn = connect()
rows = conn.execute(f'SELECT * FROM "{gsheet_url}"')
df_gsheet = pd.DataFrame(rows)
st.write(df_gsheet)