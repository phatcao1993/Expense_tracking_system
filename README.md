# Expense Tracking System
 this project is an expense management systems that contains Streamlit frontend application and FastAPI backend server
 
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
