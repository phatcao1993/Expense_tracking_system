# Expense Tracking System
## Overview 
 The Expense Tracking System is a web application designed to help users manage their personal finances. It includes a Streamlit frontend for the user interface and a FastAPI backend for handling the server-side logic. The system allows users to track their expenses and gain insights into their financial habits.
## Features
 - A user-friendly expense tracking interface is built with Streamlit.
 - Fast and efficient backend powered by FastAPI.
 - Persistent data storage using MySQL.
 - Real-time updates with fast server reload and interactive frontend.
 
# Project Structure

 - **frontend/** : contains Streamlit applicatipn codes
 - **backend/** : contains FastAPI server , mySQL-connector-python codes
 - **terst** : contains tests case for both backend and frontend
 - **-requirments.txt** : List of required Python Package
 - **README.md** : provides overviews structure for the project

# Setup Instructions

1. **Clone the repository**:
    ```bash
   git clone
   https://github.com/phatcao1993/Expense_tracking_system.git
     
   ```
1. **Install dependencies:**:
   ```commandline
    pip install -r requirements.txt
    ```
1. **Run the FastAPI server :**:
   ```commandline
   uvicorn server:app --reload
   ```
1. **Run the Streamlit application :**:
    ```commandline

    streamlit run frontend/app.py
```
