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

    # def get_avg_burn_rate(self):  # TODO: Update
    #     return self.total_budget / self.duration

    # def get_pct_budget_used(self):  # TODO: Update
    #     if self.total_budget == 0:
    #         raise ValueError("Budget cannot be zero.")
    #     if not isinstance(self.total_budget, int):
    #         raise ValueError("Budget must be numeric.")
    #     return self.amount_spent / self.total_budget

    # def get_remaining_budget(self, percent=False):  # TODO: Update
    #     amt_remaining = self.total_budget - self.amount_spent
    #     if percent:
    #         return amt_remaining / self.total_budget
    #     else:
    #         return amt_remaining
