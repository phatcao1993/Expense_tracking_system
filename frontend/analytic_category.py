import streamlit as st
from datetime import datetime
import requests
from pandas import DataFrame

API_URL = "http://localhost:8000"

def analytics():
    col1, col2 = st.columns(2)
    with col1:
        start_date = st.date_input("Start_date", datetime(2024,8,1))
    with col2:
        end_date = st.date_input("End_date", datetime(2024,8,2))

    if st.button("Get Analytics"):
        payload ={
            "start_date": start_date.strftime("%Y-%m-%d"),
            "end_date": end_date.strftime("%Y-%m-%d")
        }


        response = requests.post(f"{API_URL}/analytics/", json= payload)
        response = response.json()

        data = {
            "Category": list(response.keys()),
            "Amount" : [ response[category]["total_amount"] for category in response],
            "Percentage": [ response[category]["percentage"]for category in response]
        }
        df = DataFrame(data)
        df_sorted = df.sort_values(by = "Percentage", ascending = False)

        st.bar_chart(data = df_sorted.set_index("Category")["Percentage"], width= 0 , height= 0, use_container_width= True)
        st.table(df_sorted)



