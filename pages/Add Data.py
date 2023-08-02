import streamlit as st
import json

from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Add Data",
    page_icon="👋",
)

conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
data = conn.get_file_data().json()

file_name =  []
file_name_index = {}

for x in data: 
    file_name.append(x["Name"])
    file_name_index[x["Name"]] = x

option = st.selectbox(
    'Select the file',
    file_name)

selected_file  = file_name_index[option]

table = conn.get_table_data({"filePath": selected_file["Id"]}).json()
st.write(table[0]["name"])

columns = conn.get_table_header({"filePath": selected_file["Id"], "tableName": table[0]["name"]}).json()

column_data = list(columns[0].keys())

column_data = column_data[2:]

formData = {}

with st.form("my_form"):
   st.write("Create File")
   #construct form based on columns
   for x in column_data:
      formValue = st.text_input(x)
      formData[x] = formValue   
   submitted = st.form_submit_button("Submit")
   if submitted:
       conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
       res = conn.add_data({"fileName": selected_file["Id"], "tableName": table[0]["name"], "row": formData })
       if res.status_code == 200:
        st.success('Record Added Successfully')
       else:
        st.error('Something Went Wrong!')


