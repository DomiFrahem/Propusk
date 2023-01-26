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
        self._create_id()
        
        self.textChanged.connect(
            self._create_id
        )
        
        self.textEdited.connect(
            self._create_id
        )
        
        self.cursorPositionChanged.connect(
            self._create_id
        )
        
    def clear(self) -> None:
        self._create_id()

    def _create_id(self) -> None:
        self.setText(datetime.now().strftime("%Y%m%d%H%M%S"))
