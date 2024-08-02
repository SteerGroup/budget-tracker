import sqlite3
from pathlib import Path

BUDGET_DB_FILE = "budget.db"


def create_db():
    Path(BUDGET_DB_FILE).touch(exist_ok=True)
    db_obj = get_db_objects()
    create_projects_table(db_obj["cur"])
    create_budget_details_table(db_obj["cur"])
    db_obj["con"].close()


def get_db_objects():
    con = sqlite3.connect(BUDGET_DB_FILE)
    return {"con": con, "cur": con.cursor()}


def create_projects_table(db_cur):
    db_cur.execute(
        """
        CREATE TABLE IF NOT EXISTS projects(
            name TEXT,
            code TEXT PRIMARY KEY,
            open INTEGER
        )
        """
    )


def create_budget_details_table(db_cur):
    db_cur.execute(
        """
        CREATE TABLE IF NOT EXISTS budget_details(
            project_code TEXT,
            period INTEGER,
            task INTEGER,
            staff TEXT,
            planned_budget REAL,
            actual_budget REAL
        )
        """
    )


def add_project(project):
    db_obj = get_db_objects()
    db_obj["cur"].execute(
        "INSERT INTO projects VALUES(?, ?, ?);",
        (project.name, project.code, project.open),
    )
    db_obj["con"].commit()
    db_obj["con"].close()
