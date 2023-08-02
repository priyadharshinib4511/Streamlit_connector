# streamlit_app.py

import streamlit as st

# from power_automate_connection import PowerAutomateExcelConnection

st.set_page_config(
    page_title="Power Automate Excel Connection",
    page_icon="👋",
)

st.title("Power Automate Excel Connection")

st.subheader('This Connection does all the utilites to MS Excel on Onedrive using Power Automate As the interface')

st.markdown("""
<style>
div[data-testid="metric-container"] {
   background-color: rgba(28, 131, 225, 0.1);
   border: 1px solid rgba(28, 131, 225, 0.1);
   padding: 5% 5% 5% 10%;
   border-radius: 5px;
   color: rgb(30, 103, 119);
   overflow-wrap: break-word;
   text
}

/* breakline for metric text         */
div[data-testid="metric-container"] > label[data-testid="stMetricLabel"] > div {
   overflow-wrap: break-word;
   white-space: break-spaces;
   color: red;
}
</style>
"""
, unsafe_allow_html=True)

st.metric(label="1. You can Create a File", value="")

st.metric(label="2. You can Create a Table", value="")

st.metric(label="3. You can Add a record", value="")

st.metric(label="4. You can update record(s)", value="")

st.metric(label="5. You can delete record(s)", value="")



