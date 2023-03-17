from PySide6.QtWidgets import QMessageBox
from logger import logger

def show_dialog(state: QMessageBox.Icon, title: str, massage: str):
   msgBox = QMessageBox()
   msgBox.setIcon(state)
   msgBox.setText(massage)
   msgBox.setWindowTitle(title)
   msgBox.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
#    msgBox.buttonClicked.connect(msgButtonClick)

   returnValue = msgBox.exec()
   if returnValue == QMessageBox.Ok:
      logger.info('MyMessageBox press ok')