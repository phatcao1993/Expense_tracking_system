import logging

import mysql.connector
from contextlib import contextmanager
from logging_setup import setup_logger

logger = setup_logger("db_helper")

@contextmanager
def get_db_connection(commit=False):
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="Nightjileo321!",
            database="expense_manager"
        )
        if connection.is_connected():
            print("Successfully connected to the database")
        cursor = connection.cursor(dictionary=True)
        yield cursor
        if commit:
            connection.commit()
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        if 'cursor' in locals() and cursor:
            cursor.close()
        if 'connection' in locals() and connection.is_connected():
            connection.close()

def fetch_data_date(expense_date):
    logger.info(f"fetching expense on {expense_date}")
    with get_db_connection() as cursor:
        cursor.execute("SELECT * FROM expenses WHERE expense_date = %s", (expense_date,))
        data = cursor.fetchall()
        return data


def insert_expense_date(expense_date, amount, category, notes):
    logger.info(f"insert expense on {expense_date}")
    with get_db_connection(commit=True) as cursor:
        cursor.execute(
            "INSERT INTO expenses (expense_date, amount, category, notes) VALUES (%s, %s, %s, %s)",
            (expense_date, amount, category, notes)
        )

def delete_expense_date(expense_date):
    logger.info(f"delete expense on {expense_date}")
    with get_db_connection(commit=True) as cursor:
        cursor.execute("DELETE FROM expenses WHERE expense_date = %s", (expense_date,))

def fetch_expense_sumary(start_date, end_date):
    logger.info(f"fetching expense summary from {start_date} to {end_date}")
    with get_db_connection() as cursor:
        cursor.execute("select sum(amount) as total_amount,category from expense_manager.expenses where expense_date BETWEEN %s AND %s group by category",
                       (start_date, end_date))
        data = cursor.fetchall()
        return data

def fetch_monthly_expense():
    logging.info("fetching monthly expense")
    with get_db_connection() as cursor:
        cursor.execute("select month(expense_date) as Month, sum(amount) as total_amount from expenses group by month(expense_date)")
        data = cursor.fetchall()
        return data

if __name__ == "__main__":
    # Example usage for a date range
    report = fetch_monthly_expense()
    print(report )

#sumary = fetch_expense_sumary("2024-08-01","2024_08-06")

#print(sumary)