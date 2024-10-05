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
        (project.name, project.code, project.open),
    )
    db_obj["con"].commit()
    db_obj["con"].close()


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


def get_avg_burn_rate(project):
    db_obj = get_db_objects()
    burn_rate = (
        db_obj["cur"]
        .execute(
            "SELECT SUM(planned_budget) / MAX(period) "
            f"FROM budget_details WHERE project_code = '{project.code}';"
        )
        .fetchone()[0]
    )
    db_obj["con"].close()
    return burn_rate


def get_remaining_budget(project, percent):

    db_obj = get_db_objects()

    total_budget = (
        db_obj["cur"]
        .execute(
            "SELECT SUM(planned_budget) "
            f"FROM budget_details WHERE project_code = '{project.code}';"
        )
        .fetchone()[0]
    )

    if percent and total_budget == 0:
        raise ValueError("Budget cannot be zero.")

    remaining_budget = (
        db_obj["cur"]
        .execute(
            "SELECT SUM(planned_budget) - SUM(actual_budget) "
            f"FROM budget_details WHERE project_code = '{project.code}';"
        )
        .fetchone()[0]
    )

    db_obj["con"].close()
    return remaining_budget / total_budget if percent else remaining_budget
