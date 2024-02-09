from project import Project

print("Welcome to the Steer Budget Tracker.\n")

project_YAML_path = input(
    "Please enter the path to your project's YAML file: "
)
project = Project(project_YAML_path)

print(f"PROJECT SUMMARY REPORT: {project.name}")
print(f"Total periods: {project.duration}")
print(f"Average burn rate: {project.get_avg_burn_rate()}")
print(
    f"Budget remaining: {project.get_remaining_budget()} "
    f"of {project.total_budget}"
)
print(f"Percent remaining: {project.get_remaining_budget(percent=True)}")
