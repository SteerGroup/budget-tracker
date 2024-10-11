import db_helpers


class Project:
    def __init__(
        self,
        name: str,
        code: str,
        open: bool,
        budget_csv_path: str | None = None,
    ):
        db_helpers.create_db()
        self.name = name
        self.code = code
        self.open = open
        self.add_project_to_db()
        if budget_csv_path:
            self.parse_budget_csv(budget_csv_path)

    def add_project_to_db(
        self,
    ):  # TODO: reimplement commented properties as DB calcs
        db_helpers.add_project(self)
        # self.total_budget = project_yaml["total_budget"]
        # self.amount_spent = project_yaml["amount_spent"]
        # self.duration = project_yaml["duration"]
        # self.staff_count = project_yaml["staff_count"]
        # self.staff_list = project_yaml["staff_list"]

    # def write_yaml(self):
    #     project_dict = {
    #         "name": self.name,
    #         "code": self.code,
    #         "open": self.open,
    #         "total_budget": self.total_budget,
    #         "amount_spent": self.amount_spent,
    #         "duration": self.duration,
    #         "staff_count": self.staff_count,
    #         "staff_list": self.staff_list,
    #     }
    #     with open(self.yaml_path, "w") as file:
    #         yaml.dump(project_dict, file)

    def parse_budget_csv(self, budget_csv_path):
        db_helpers.add_project_budget_details(self, budget_csv_path)

    def total_budget(self):
        db_obj = db_helpers.get_db_objects()

        total_budget = (
            db_obj["cur"]
            .execute(
                "SELECT SUM(planned_budget) "
                f"FROM budget_details WHERE project_code = '{self.code}';"
            )
            .fetchone()[0]
        )
        db_obj["con"].close()
        return total_budget

    def spent_budget(self):
        db_obj = db_helpers.get_db_objects()
        spent_budget = (
            db_obj["cur"]
            .execute(
                "SELECT SUM(actual_budget) "
                f"FROM budget_details WHERE project_code = '{self.code}';"
            )
            .fetchone()[0]
        )
        db_obj["con"].close()
        return spent_budget

    def duration(self):
        db_obj = db_helpers.get_db_objects()
        duration = (
            db_obj["cur"]
            .execute(
                "SELECT MAX(period) "
                f"FROM budget_details WHERE project_code = '{self.code}';"
            )
            .fetchone()[0]
        )
        db_obj["con"].close()
        return duration

    def planned_burn_rate(self):
        return self.total_budget() / self.duration()

    def percent_budget_used(self):
        total_budget = self.total_budget()
        if total_budget == 0:
            raise ValueError("Budget cannot be zero.")
        return self.spent_budget() / total_budget

    def remaining_budget(self, percent=False):
        total_budget = self.total_budget()
        if total_budget == 0:
            raise ValueError("Budget cannot be zero.")
        remaining_budget = total_budget - self.spent_budget()
        return remaining_budget / total_budget if percent else remaining_budget
