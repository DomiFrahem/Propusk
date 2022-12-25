from PySide6.QtWidgets import QTextEdit, QDialog
from PySide6.QtPrintSupport import QPrintDialog, QPrinter

class Printer:
    def __init__(self, text: str) -> None:
        self.editor = QTextEdit()
        self.editor.setHtml(text)
        
    def print(self) -> None:
        dialog = QPrintDialog()
        if dialog.exec_() == QDialog.Accepted:
            self.editor.document().print_(dialog.printer())