import streamlit as st
from datetime import datetime
import requests
from add_update import add_update_expense
from analytic_category import analytics
from analytic_month import analytic_by_month

API_URL = "http://localhost:8000"  # Update this with your actual API URL

st.title("Expense Tracking System")

# Tabs for functionality
tab1, tab2, tab3 = st.tabs(["Add/Update Expense", "Analytics by Category","Analytics by Month"
                                                                          ""])

with tab1:
    add_update_expense()

with tab2:
    analytics()

with tab3:
    analytic_by_month()


