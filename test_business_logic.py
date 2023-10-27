import business_logic


def test_get_pct_budget_used():
    assert business_logic.get_pct_budget_used(30000, 100000) == 0.3
    assert business_logic.get_pct_budget_used(120000, 100000) == 1.2


def test_get_remaining_budget():
    assert business_logic.get_remaining_budget(30000, 100000) == 70000
    assert (
        business_logic.get_remaining_budget(30000, 100000, percent=True) == 0.7
    )
    assert business_logic.get_remaining_budget(120000, 100000) == -20000
    assert (
        business_logic.get_remaining_budget(120000, 100000, percent=True)
        == -0.2
    )
