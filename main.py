from init_var import *
import os
import sys

from PySide6.QtWidgets import QApplication
# from appdirs import user_data_dir 



def main():
    app = QApplication(sys.argv)
    
    load_variables()
    
    from module.WorkWithDB import init_db    
    from module.CleanerImage import CleanerImage
    from window.MainWindow import MainWindow
    
    init_db()
    
    CleanerImage(os.environ.get('PHOTO_DIR')) \
        .clear()
    
    
    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
