from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from datetime import datetime


class PLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(PLineEdit, self).__init__(parent)
        self.setValidator(QRegularExpressionValidator(
            r"\d{14}", self
        ))
        
        self.setReadOnly(True)
        self.__create_id()
        self.selectionChanged.connect(lambda: self.setSelection(0, 0))
        
    def clear(self) -> None:
        self.__create_id()

    def __create_id(self) -> None:
        self.setText(datetime.now().strftime("%Y%m%d%H%M%S"))
    
        
    def mousePressEvent(self, action) -> None:
        self.__create_id()
        
    def get_value(self) -> None:
        return int(self.text())
