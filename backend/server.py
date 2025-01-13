from fastapi import FastAPI, HTTPException
from datetime import date
from typing import List
from pydantic import BaseModel
import db_helper as db


class Expenses(BaseModel):
    amount: float
    category: str
    notes: str


class DateRange(BaseModel):
    start_date: date
    end_date: date

class RangeDate(BaseModel):
    start_date : date
    end_date:date


app = FastAPI()


@app.get("/expenses/{expense_date}", response_model=List[Expenses])
def get_expense(expense_date: date):
    expenses = db.fetch_data_date(expense_date)
    if not expenses:
        raise HTTPException(status_code=404, detail="No expenses found for the given date.")
    return expenses


@app.post("/expenses/{expense_date}")
def add_or_update_expenses(expense_date: date, expenses: List[Expenses]):
    db.delete_expense_date(expense_date)  # Delete existing records for the date
    for exp in expenses:
        db.insert_expense_date(expense_date, exp.amount, exp.category, exp.notes)
    return {"message": "Expenses updated successfully"}


@app.post("/analytics/")
def get_analytics(date_range: DateRange):
    data = db.fetch_expense_sumary(date_range.start_date, date_range.end_date)
    if data is None:
        raise HTTPException(status_code=500, detail="Failed to retrieve data summary.")

    breakdown = {}
    total = sum([row["total_amount"] for row in data])

    for row in data:
        percentage = (row["total_amount"]/total)*100 if total != 0 else 0
        breakdown[row["category"]] ={
            "total_amount" : row["total_amount"],
            "percentage": percentage
        }
    return breakdown

@app.get("/monthly/")
def get_monthly_exp_summary():
    total_expense = db.fetch_monthly_expense()
    return total_expense