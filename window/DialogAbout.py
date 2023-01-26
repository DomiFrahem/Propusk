from .ui_py.ui_DialogAbout import Ui_DialogAbout
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt
import os

class DialogAbout(QDialog, Ui_DialogAbout):
    def __init__(self, parent=None):
        super(DialogAbout, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
        self.version.setText(os.environ.get("VERSION"))