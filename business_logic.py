def get_pct_budget_used(amt_spent, total_budget):
    return amt_spent / total_budget


def get_remaining_budget(amt_spent, total_budget, percent=False):
    amt_remaining = total_budget - amt_spent
    if percent:
        return amt_remaining / total_budget
    else:
        return amt_remaining
