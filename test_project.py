import pytest
from project import Project


@pytest.fixture
def test_project():
    return Project("test_project.yaml")


class TestGetPctBudgetUsed:
    def test_success(self, test_project):
        assert test_project.get_pct_budget_used() == 0.1
        test_project.amount_spent += 12000
        assert test_project.get_pct_budget_used() == 0.2

    def test_zero_budget(self, test_project):
        test_project.total_budget = 0
        with pytest.raises(ValueError, match="Budget cannot be zero"):
            test_project.get_pct_budget_used()

    def test_non_numeric_budget(self, test_project):
        test_project.total_budget = "Zero"
        with pytest.raises(ValueError, match="Budget must be numeric"):
            test_project.get_pct_budget_used()


class TestGetRemainingBudget:
    def test_positive(self, test_project):
        assert test_project.get_remaining_budget() == 108000
        assert test_project.get_remaining_budget(percent=True) == 0.9

    def test_negative(self, test_project):
        test_project.amount_spent = 150000
        assert test_project.get_remaining_budget() == -30000
        assert test_project.get_remaining_budget(percent=True) == -0.25


class TestGetAvgBurnRate:
    def test_success(self, test_project):
        assert test_project.get_avg_burn_rate() == 40000
