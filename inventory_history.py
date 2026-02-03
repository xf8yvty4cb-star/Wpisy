from PyQt5.QtWidgets import QDialog, QTableWidgetItem
from PyQt5.uic import loadUi

class InventoryHistoryDialog(QDialog):
    def __init__(self, context):
        super().__init__()
        self.context = context
        loadUi("app/ui/inventory_history.ui", self)
        self.load_data()

    def load_data(self):
        rows = self.context.inventory.get_history()
        self.table.setRowCount(len(rows))

        for r, row in enumerate(rows):
            for c, value in enumerate(row):
                self.table.setItem(r, c, QTableWidgetItem(str(value)))
