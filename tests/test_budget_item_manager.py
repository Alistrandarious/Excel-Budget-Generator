from excelbudget.budget_items_manager import BudgetItems


class TestBudgetItemManager:

    budget_item_manager = BudgetItems()

    def test_items_empty_on_initialisation(self):
        assert bool(self.budget_item_manager.budget_items) is False

    def test_add_item_budget_list(self):
        self.budget_item_manager.add_budget_item("Income", 2000)
        assert bool(self.budget_item_manager.budget_items) is False

    def test_budget_item_value_returned(self):
        assert self.budget_item_manager.return_budget_item_value("Income") == 2000

    def test_item_is_removed_from_budget_list(self):
        self.budget_item_manager.delete_budget_item("Income")
        assert bool(self.budget_item_manager.budget_items) is False

    def test_incorrect_key_raises_key_error_for_returning_item(self):
        with pytest.raises(KeyError):
            self.budget_item_manager.return_budget_item_value("test")
    #  python -m pytest -v
