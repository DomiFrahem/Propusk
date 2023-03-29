from PySide6.QtWidgets import QLineEdit
from PySide6.QtGui import QRegularExpressionValidator
from datetime import datetime
from PySide6.QtCore import Slot


class PLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(PLineEdit, self).__init__(parent)
        self.setValidator(QRegularExpressionValidator(
            r"\d{14}", self
        ))
        
        self.setReadOnly(True)
        self.__create_id()
        
    def clear(self) -> None:
        self.__create_id()

    def __create_id(self) -> None:
        self.setText(datetime.now().strftime("%Y%m%d%H%M%S"))
        
    def mousePressEvent(self, event) -> None:
        self.__create_id()
        return super().mousePressEvent(event)
