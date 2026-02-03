from app.database.db import Database
from app.inventory.inventory_service import InventoryService
from app.sales.sales_service import SalesService

class AppContext:
    def __init__(self):
        self.db = Database()
        self.inventory = InventoryService(self.db)
        self.sales = SalesService(self.db, self.inventory)
