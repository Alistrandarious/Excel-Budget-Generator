from excelbudget.budget_items_manager import BudgetItems

budget = BudgetItems()
budget.add_budget_item("Dinner", 30)
budget.add_budget_item("Lunch", 20)
budget.add_budget_item("Entertainment", 500)
budget.add_budget_item("Big John's Admin Fee", 100)

budget.save_budget_items()