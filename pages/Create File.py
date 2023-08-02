import streamlit as st
import json

from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Create File",
    page_icon="👋",
)

with st.form("my_form"):
   st.write("Create File")
   fileName = st.text_input('File Name')
   sheetName = st.text_input('Sheet Name ')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
       res = conn.create_file({"fileName": fileName, "sheetName": sheetName })
       if res.status_code == 200:
        st.success('File Created Successfully')
       else:
        st.error('Something Went Wrong!')






