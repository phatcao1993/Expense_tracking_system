from backend import db_helper as db

def test_fetch_data_date():
    expense = db.fetch_data_date("2024-08-02")

    assert expense[0]["amount"] == 50
    assert expense[0]["category"] == "Entertainment"
    assert expense[0]["notes"] == "Movie tickets"

def test_fetch_data_date_invalid():
    expense = db.fetch_data_date("9999-09-10")

    len(expense) == 0

def test_fetch_expense_sumary():
    exp = db.fetch_expense_sumary("2024-08-03","2024-08-08")
    assert exp[0]["total_amount"] == 255
    assert exp[0]["category"] == "Food"

def test_fetching_monthly_expense():
    expense = db.fetch_monthly_expense ()
    assert  expense[0]["month"] == 8
    assert expense[0]["total_amount"] == 6542.0




