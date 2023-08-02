import streamlit as st
import json
from st_aggrid import AgGrid
import pandas as pd    
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, AgGridTheme, JsCode, GridUpdateMode
from streamlit_autorefresh import st_autorefresh
from streamlit_js_eval import streamlit_js_eval



from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Update Data",
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
    'How would you like to be contacted?',
    file_name)

selected_file  = file_name_index[option]

table = conn.get_table_data({"filepath": selected_file["Id"]}).json()
st.write('Table Name : ' + table[0]["name"])

data = conn.get_table_values({"fileId": selected_file["Id"], "tableName": table[0]["name"]}).json()

for x in data:
    del x["@odata.etag"]
    del x["ItemInternalId"]

df = pd.json_normalize(data)


grid_return1 = AgGrid(df, editable=True)
new_df = grid_return1['data']

if st.button('Update'):
    conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
    res = conn.update_values(
    {
        "fileId": selected_file["Id"],
        "tabelName": table[0]["name"],
        "keyColumn": list(data[0].keys())[0],
        "data": new_df.to_dict('records')
    })
    if res.status_code == 200:
        st.success('Record(s) Updated Successfully')
    else:
        st.error('Something Went Wrong!')
    streamlit_js_eval(js_expressions="parent.window.location.reload()")



