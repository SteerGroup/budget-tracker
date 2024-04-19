import sqlite3
from pathlib import Path

BUDGET_DB_FILE = "budget.db"


def create_db():
    Path(BUDGET_DB_FILE).touch(exist_ok=True)


def get_db_objects():
    con = sqlite3.connect(BUDGET_DB_FILE)
    return {"con": con, "cur": con.cursor()}


def create_project_table():
    pass


def create_budget_details_table():
    pass
