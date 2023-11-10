import pytest
import business_logic


class TestGetPctBudgetUsed:
    def test_success(self):
        assert business_logic.get_pct_budget_used(30000, 100000) == 0.3
        assert business_logic.get_pct_budget_used(120000, 100000) == 1.2

    def test_zero_budget(self):
        with pytest.raises(ValueError, match="Budget cannot be zero"):
            business_logic.get_pct_budget_used(30000, 0)

    def test_non_numeric_budget(self):
        with pytest.raises(ValueError, match="Budget must be numeric"):
            business_logic.get_pct_budget_used(30000, "X")


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


class TestGetAvgBurnRate:
    def test_success(self):
        assert business_logic.get_avg_burn_rate(120000, 12) == 10000
