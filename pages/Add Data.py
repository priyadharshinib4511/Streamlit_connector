# streamlit_app.py

import streamlit as st
import json


from power_automate_connection import DuckDBConnection

st.set_page_config(
    page_title="Hello",
    page_icon="👋",
)

conn = st.experimental_connection("api", type=DuckDBConnection)
data = conn.get_file_data().json()
print(data)

file_name =  []
file_name_index = {}

for x in data: 
    file_name.append(x["Name"])
    file_name_index[x["Name"]] = x

option = st.selectbox(
    'How would you like to be contacted?',
    file_name)

selected_file  = file_name_index[option]

table = conn.get_table_data({"filePath": selected_file["Id"]}).json()
print("here", table)
st.write(table[0]["name"])

columns = conn.get_table_header({"filePath": selected_file["Id"], "tableName": table[0]["name"]}).json()

print(columns[0])

column_data = list(columns[0].keys())

print(column_data)

column_data = column_data[2:]

with st.form("my_form"):
   st.write("Create File")
   for x in column_data:
      tableName = st.text_input(x)     
    




   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       conn = st.experimental_connection("api", type=DuckDBConnection)
       conn.add_data({"fileName": fileName, "sheetName": sheetName })


