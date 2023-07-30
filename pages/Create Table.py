# streamlit_app.py

import streamlit as st
import json


from power_automate_connection import DuckDBConnection

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

with st.form("my_form"):
   st.write("Create File")
   fileName = st.text_input('File Name')
   sheetName = st.text_input('Sheet Name ')



   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       conn = st.experimental_connection("api", type=DuckDBConnection)
       conn.add_data({"fileName": fileName, "sheetName": sheetName })


