import sys
from PyQt5.QtWidgets import QApplication
from app.context import AppContext
from app.main_window import MainWindow

def main():
    app = QApplication(sys.argv)
    context = AppContext()
    window = MainWindow(context)
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
