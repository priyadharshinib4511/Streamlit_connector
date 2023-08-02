import streamlit as st
import json

from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Create Table",
    page_icon="👋",
)

conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
data = conn.get_file_data().json()

file_name =  []
file_name_index = {}


# process file name
for x in data: 
    file_name.append(x["Name"])
    file_name_index[x["Name"]] = x

option = st.selectbox(
    'Select File Name',
    file_name)

selected_file  = file_name_index[option]
with st.form("my_form"):
   st.write("Create File")
   tableName = st.text_input('Table Name')
   columnName = st.text_input('Column Names (Enter comma (,) separated values)')
   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
       
       res = conn.create_table({
                "filepath": selected_file["Id"],
                "tableRange": "A1:A"+str(len(list(columnName.split(',')))),
                "tableName": tableName,
                "columnName": columnName
        })
       if res.status_code == 200:
        st.success('Table Created Successfully')
       else:
        st.error('Something Went Wrong!')



