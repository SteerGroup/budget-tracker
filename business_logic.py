def get_pct_budget_used(amt_spent, total_budget):
    if total_budget == 0:
        raise ValueError("Budget cannot be zero.")
    if not isinstance(total_budget, int):
        raise ValueError("Budget must be numeric.")
    return amt_spent / total_budget


def get_remaining_budget(amt_spent, total_budget, percent=False):
    amt_remaining = total_budget - amt_spent
    if percent:
        return amt_remaining / total_budget
    else:
        return amt_remaining


def get_avg_burn_rate(total_budget, periods):
    return total_budget / periods
