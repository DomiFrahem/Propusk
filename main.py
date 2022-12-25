from window.MainWindow import MainWindow
from PySide6.QtWidgets import QApplication
from module.WorkWithDB import init_db
import sys

def main():
    init_db()
    
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
