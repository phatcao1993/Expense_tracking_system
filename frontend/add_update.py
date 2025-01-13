import streamlit as st
from datetime import datetime
import requests

API_URL = "http://localhost:8000"  # Update this with your actual API URL

def add_update_expense():
    # Date Input
    selected_date = st.date_input("Enter Date", datetime(2024, 8, 1), label_visibility="collapsed")
    formatted_date = selected_date.strftime("%Y-%m-%d")  # Format date for the API

    # Fetch existing expenses for the selected date
    response = requests.get(f"{API_URL}/expenses/{formatted_date}")
    if response.status_code == 200:
        existing_expense = response.json()
    else:
        st.error(f"Failed to retrieve expenses. Error: {response.status_code}")
        existing_expense = []  # Fallback to an empty list

    # Expense categories
    categories = ["Rent", "Food", "Shopping", "Entertainment", "Other"]

    with st.form(key="expense_form"):
        # Form for expenses
        st.markdown("### Add or Update Expenses")

        expenses = []  # List to collect entered expenses

        # Iterate through up to 5 expenses
        for i in range(5):
            if i < len(existing_expense):
                # Pre-fill with existing data if available
                amount = existing_expense[i]["amount"]
                category = existing_expense[i]["category"]
                notes = existing_expense[i]["notes"]
            else:
                # Default values for new entries
                amount = 0.0
                category = "Shopping"
                notes = ""

            # Create columns for inputs
            col1, col2, col3 = st.columns(3)
            with col1:
                amount_input = st.number_input(
                    label="Amount",
                    min_value=0.0,
                    step=1.0,
                    value=amount,
                    key=f"amount_{i}",
                    label_visibility="collapsed"
                )
            with col2:
                category_input = st.selectbox(
                    label="Category",
                    options=categories,
                    index=categories.index(category),
                    key=f"category_{i}",
                    label_visibility="collapsed"
                )
            with col3:
                note_input = st.text_input(
                    label="Notes",
                    value=notes,
                    key=f"note_{i}",
                    label_visibility="collapsed"
                )

            # Append to expenses list
            expenses.append({
                "amount": amount_input,
                "category": category_input,
                "notes": note_input
            })

        # Submit button
        submit_button = st.form_submit_button("Submit")
        if submit_button:
            # Filter out empty expenses
            filtered_expenses = [expense for expense in expenses if expense["amount"] > 0]
            response = requests.post(f"{API_URL}/expenses/{formatted_date}", json=filtered_expenses)
            if response.status_code == 200:
                st.success("Expenses updated successfully!")
            else:
                st.error(f"Failed to update expenses. Error: {response.status_code} - {response.text}")
