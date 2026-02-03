class InventoryService:
    def __init__(self, db):
        self.db = db

    def adjust_stock(self, article_id, qty, source):
        self.db.execute(
            "INSERT INTO inventory_history(article_id, qty, source) VALUES (?,?,?)",
            (article_id, qty, source)
        )

    def get_history(self):
        return self.db.query("""
            SELECT h.date, a.name, h.qty, h.source
            FROM inventory_history h
            JOIN articles a ON a.id = h.article_id
            ORDER BY h.date DESC
        """)
