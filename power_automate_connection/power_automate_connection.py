from streamlit.connections import ExperimentalBaseConnection
from streamlit.runtime.caching import cache_data

import pandas as pd
import requests
import json

class DuckDBConnection(ExperimentalBaseConnection["Session"]):
    """Basic st.experimental_connection implementation for DuckDB"""

    def _connect(self, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        # x = requests.post("https://prod-06.centralindia.logic.azure.com:443/workflows/d6b6c513bd864c209ce6eb5ac5681f54/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=PG5ORhrCv8F-Qtm8AvifDiy7c8wTXpY-HiqLpyUJKnI", {"id": 1})
        # print(x.text)
        return True
    
    def add_data(self, params, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        print(params)
        x = requests.post("https://prod-06.centralindia.logic.azure.com:443/workflows/d6b6c513bd864c209ce6eb5ac5681f54/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=PG5ORhrCv8F-Qtm8AvifDiy7c8wTXpY-HiqLpyUJKnI", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        print(x.text)

    def create_table(self, params, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        print(params)
        x = requests.post("https://prod-14.centralindia.logic.azure.com:443/workflows/c49bc9dfd0624bb68c9c776562fec1ea/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=Dxpj3rH8ZBsgviwsDfpVH9NAtyj2sGaTQVF8JxXB4nE", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        print(x.text)

    def get_file_data(self, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        x = requests.get("https://prod-20.centralindia.logic.azure.com:443/workflows/617789c647ce4178a2ac29823292b43b/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=SjDoqhiPe7T55cZ476c8PA4ZVB8mKf22fEB6_2b2iWk")
        return x

    def get_table_data(self, params, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        x = requests.post("https://prod-14.centralindia.logic.azure.com:443/workflows/9339373f8f3a430b9f52293354eb094f/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=2F0Rq1Nq9VzMWYt522GmdX3LFuUdvnzi1vIGGqAIFos", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    def get_table_header(self, params, **kwargs):
        # if 'database' in kwargs:
        #     db = kwargs.pop('database')
        # else:
        #     db = self._secrets['database']
        # return duckdb.connect(database=db, **kwargs)
        x = requests.post("https://prod-24.centralindia.logic.azure.com:443/workflows/83d1f659d3054f06860f1e511182f5b2/triggers/manual/paths/invoke?api-version=2016-06-01&sp=%2Ftriggers%2Fmanual%2Frun&sv=1.0&sig=zJRPEXZKj_c41Lb6Q9X0ufGM-07YVoarlmlKIETOhdE", data=json.dumps(params), headers={'Content-Type': 'application/json'})
        return x

    
    # def cursor(self) -> duckdb.DuckDBPyConnection:
    #     return self._instance.cursor()

    # def query(self, query: str, ttl: int = 3600, **kwargs) -> pd.DataFrame:
    #     @cache_data(ttl=ttl)
    #     def _query(query: str, **kwargs) -> pd.DataFrame:
    #         cursor = self.cursor()
    #         cursor.execute(query, **kwargs)
    #         return cursor.df()
        
    #     return _query(query, **kwargs)