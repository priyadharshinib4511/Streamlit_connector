import streamlit as st
import json
from st_aggrid import AgGrid
import pandas as pd    
from st_aggrid import AgGrid, GridOptionsBuilder, DataReturnMode, AgGridTheme, JsCode, GridUpdateMode
from streamlit_autorefresh import st_autorefresh
from streamlit_js_eval import streamlit_js_eval

from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Delete Data",
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


gb = GridOptionsBuilder.from_dataframe(df)
gb.configure_default_column(editable=False, wrapText=True, autoHeight=True)
gb.configure_side_bar()
gb.configure_selection('multiple', use_checkbox=True)
gb_grid_options = gb.build()

grid_return = AgGrid(
        df,
        gridOptions = gb_grid_options,
        key = list(data[0].keys())[0],
        data_return_mode = DataReturnMode.AS_INPUT,
        allow_unsafe_jscode = True,
        fit_columns_on_grid_load = False,
        enable_enterprise_modules = False,
        height = 320,
        width = '100%',
        theme = "streamlit"
    )
selected_rows = grid_return["selected_rows"]

rows_to_delete = []

for x in selected_rows:
    del x["_selectedRowNodeInfo"]
    rows_to_delete.append(int(x["Id"]))

if st.button('Delete'):
    print("inside delete", df)
    conn = st.experimental_connection("api", type=PowerAutomateExcelConnection)
    res = conn.delete_value(
    {
        "fileId": selected_file["Id"],
        "tabelName": table[0]["name"],
        "keyColumn": list(data[0].keys())[0],
        "data": rows_to_delete
    })
    if res.status_code == 200:
        st.success('Record(s) Deleted Successfully')
    else:
        st.error('Something Went Wrong!')
    streamlit_js_eval(js_expressions="parent.window.location.reload()")



