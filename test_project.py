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

    # def test_zero_budget(self, test_project):
    #     with pytest.raises(ValueError, match="Budget cannot be zero"):
    #         test_project.get_pct_budget_used(30000, 0)

    # def test_non_numeric_budget(self, test_project):
    #     with pytest.raises(ValueError, match="Budget must be numeric"):
    #         test_project.get_pct_budget_used(30000, "X")


def test_get_remaining_budget(test_project):
    assert test_project.get_remaining_budget() == 108000
    assert test_project.get_remaining_budget(percent=True) == 0.9
    # assert test_project.get_remaining_budget(120000, 100000) == -20000
    # assert (
    #     test_project.get_remaining_budget(120000, 100000, percent=True)
    #     == -0.2
    # )


class TestGetAvgBurnRate:
    def test_success(self, test_project):
        assert test_project.get_avg_burn_rate() == 40000
