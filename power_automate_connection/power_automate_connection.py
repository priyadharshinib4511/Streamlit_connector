from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import pandas as pd
import requests
import json



class PowerAutomateExcelConnection(ExperimentalBaseConnection["Session"]):
    """Basic st.experimental_connection implementation for DuckDB"""

    def _connect(self, **kwargs):
        
        return True
    
    def create_file(self, params, **kwargs):
        """
        This method creates a excel file

        Args:
            self (undefined):
            params (parameters to create file):
            **kwargs (undefined):

        """        
        x = requests.post("https://prod-06.centralindia.logic.azure.com:443/workflows/d6b6c513bd864c209ce6eb5ac5681f54/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=PG5ORhrCv8F-Qtm8AvifDiy7c8wTXpY-HiqLpyUJKnI", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x
    
    def create_table(self, params, **kwargs):
        """
        This method creates a table in the selected excel file

        Args:
            self (undefined):
            params (parameters to create table):
            **kwargs (undefined):

        """     
        x = requests.post("https://prod-14.centralindia.logic.azure.com:443/workflows/c49bc9dfd0624bb68c9c776562fec1ea/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Dxpj3rH8ZBsgviwsDfpVH9NAtyj2sGaTQVF8JxXB4nE", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def get_file_data(self, **kwargs):
        """
        This method gets the file metadata information

        Args:
            self (undefined):
            params (parameters to get file data):
            **kwargs (undefined):

        """
        x = requests.get("https://prod-20.centralindia.logic.azure.com:443/workflows/617789c647ce4178a2ac29823292b43b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SjDoqhiPe7T55cZ476c8PA4ZVB8mKf22fEB6_2b2iWk")
        return x

    def get_table_data(self, params, **kwargs):
        """
        This method gets the table metadata information

        Args:
            self (undefined):
            params (parameters to get table data):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-14.centralindia.logic.azure.com:443/workflows/9339373f8f3a430b9f52293354eb094f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=2F0Rq1Nq9VzMWYt522GmdX3LFuUdvnzi1vIGGqAIFos", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def get_table_header(self, params, **kwargs):
        """
        This method gets the table header information

        Args:
            self (undefined):
            params (parameters to get table header):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-24.centralindia.logic.azure.com:443/workflows/83d1f659d3054f06860f1e511182f5b2/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=zJRPEXZKj_c41Lb6Q9X0ufGM-07YVoarlmlKIETOhdE", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def add_data(self, params, **kwargs):
        """
        This method adds the data to the file

        Args:
            self (undefined):
            params (parameters to add data to file):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-26.centralindia.logic.azure.com:443/workflows/2995e4e950dd4b019a661a75685bd8cb/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=1vc8JDbPFnIM_PCHgjbNAPn7Yx7UV6uVaDzZuDhhrb0", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def get_table_values(self, params, **kwargs):
        """
        This method gets all the records in the table

        Args:
            self (undefined):
            params (parameters to get table records):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-30.centralindia.logic.azure.com:443/workflows/f0f9ad6bb96b48058ee4d592940972d5/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=lOw3F9J9gHkkGrSNFuYLAQAnJ1opV3xbWLRam6eIMCA", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def delete_value(self, params, **kwargs):
        """
        This method deletes the records in the table

        Args:
            self (undefined):
            params (parameters to delete table records):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-28.centralindia.logic.azure.com:443/workflows/548a1c7225fe41f1b033500e84975a7d/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=HtBUi_ybNWD-UshYvDVKStmDTwFCJPiwcKe2sH1yrR4", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def update_values(self, params, **kwargs):
        """
        This method updates the records in the table

        Args:
            self (undefined):
            params (parameters to update table records):
            **kwargs (undefined):

        """
        x = requests.post("https://prod-01.centralindia.logic.azure.com:443/workflows/c696115519c44934b09c59a00fa3b3df/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=TowkhQ_VPS-bzuvZyLVMsBk67mfOm8n3esZ2ck0IxVI", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x