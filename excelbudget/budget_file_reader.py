from openpyxl import load_workbook


class BudgetFileReader:

    def __init__(self, file_name_and_path):

        self.workbook = load_workbook(file_name_and_path, read_only=True)
        self.worksheet = self.workbook.active

    def return_cell_value(self, cell_reference):
        return self.worksheet[cell_reference].value

    def print_worksheet(self):
        for item in self.worksheet:
            print(item)

    def print_all_cell_data(self):
        for val in self.worksheet.values:
            print(val)

    def print_all_data_cells_coordinates(self):
        for row in self.worksheet.rows:
            for item in row:
                print(item.coordinate)

