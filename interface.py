import business_logic as bl

print("Welcome to the Steer Budget Tracker.\n")
project_name = input("Please enter the name of your project: ")
total_budget = int(input("Please enter the total budget: "))
periods = int(
    input("Please enter the number of time periods for your project: ")
)
amt_spent = int(input("Please enter the budget spent to date: "))

print(f"PROJECT SUMMARY REPORT: {project_name}")
print(f"Total periods: {periods}")
print(f"Average burn rate: {bl.get_avg_burn_rate(total_budget, periods)}")
print(
    f"Budget remaining: {bl.get_remaining_budget(amt_spent, total_budget)} of {total_budget}."
)
