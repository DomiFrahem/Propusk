from PySide6.QtWidgets import QMessageBox
from logger import logger

def show_dialog(state: QMessageBox.Icon, title: str, massage: str) -> bool:
   msgBox = QMessageBox()
   msgBox.setIcon(state)
   msgBox.setText(massage)
   msgBox.setWindowTitle(title)
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      return True
   else:
      return False