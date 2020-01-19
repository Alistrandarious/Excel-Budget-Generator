from excelbudget.budget_excel_generator import BudgetExcelGenerator

class BudgetItems(BudgetExcelGenerator):
    def __init__(self):  # automatically run theses as opposed to typing it in
        super().__init__()
        self.budget_items = {}

    def add_budget_item(self, item, value):
        self.budget_items[item] = value

    def return_budget_item_value(self, key):
        try:
            self.budget_items[key]
        except KeyError:
            print("Item not found")

    def delete_budget_item(self, item):
        try:
            self.budget_items[item]
        except KeyError:
            print("Item not found")
            raise

    def print_budget_item(self):
        print(self.budget_items)

    def save_budget_items(self, file_name_and_path='default'):
        self._create_budget_list(self.budget_items)
        self._save_file_as(file_name_and_path)


