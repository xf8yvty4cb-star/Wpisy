from PyQt5.QtWidgets import QMainWindow
from PyQt5.uic import loadUi
from app.inventory.inventory_history import InventoryHistoryDialog

class MainWindow(QMainWindow):
    def __init__(self, context):
        super().__init__()
        self.context = context
        loadUi("app/ui/main_window.ui", self)
        self.actionHistoriaMagazynu.triggered.connect(self.show_inventory_history)

    def show_inventory_history(self):
        dlg = InventoryHistoryDialog(self.context)
        dlg.exec_()
