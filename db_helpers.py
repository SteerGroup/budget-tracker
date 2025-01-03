import csv
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
    # TODO: Change "open" to "active" later on
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
    # TODO: add try except clause to catch unique value error
    db_obj = get_db_objects()
    db_obj["cur"].execute(
        "INSERT INTO projects VALUES(?, ?, ?);",
        (project.name, project.code, project.active),
    )
    db_obj["con"].commit()
    db_obj["con"].close()


def code_exists(code):
    db_obj = get_db_objects()
    code_count = (
        db_obj["cur"]
        .execute(f"SELECT COUNT(*) FROM projects WHERE code = '{code}';")
        .fetchone()[0]
    )
    db_obj["con"].close()
    return True if code_count > 0 else False


def get_proj_info(project, label):
    db_obj = get_db_objects()
    value = (
        db_obj["cur"]
        .execute(
            f"SELECT {label} "
            f"FROM projects WHERE code = '{project.code}';"
        )
        .fetchone()[0]
    )
    db_obj["con"].close()
    return value


def add_project_budget_details(project, budget_path):
    db_obj = get_db_objects()
    with open(budget_path, newline="") as budget_file:
        reader = csv.DictReader(budget_file)
        for row in reader:
            db_obj["cur"].execute(
                "INSERT INTO budget_details VALUES(?, ?, ?, ?, ?, ?);",
                (
                    project.code,
                    row["period"],
                    row["task"],
                    row["staff"],
                    row["planned_budget"],
                    row["actual_budget"],
                ),
            )
    db_obj["con"].commit()
    db_obj["con"].close()
