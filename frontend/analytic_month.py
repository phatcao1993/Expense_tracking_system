from http.client import responses

import streamlit as st
from datetime import datetime
import requests
from pandas import DataFrame

API_URL = "http://localhost:8000"

def analytic_by_month():
    response = requests.get(f"{API_URL}/monthly/")
    response = response.json()

    data = {
        "Month" : [response[i]["Month"] for i in range(len(response))],
        "Total" : [response[i]["total_amount"] for i in range(len(response))]
    }

    df = DataFrame(data)
    df_sorted = df.sort_values(by="Month", ascending=True)

    st.bar_chart(data = df_sorted.set_index("Month")["Total"], width= 0 , height= 0, use_container_width= True)

    st.table(df_sorted)













