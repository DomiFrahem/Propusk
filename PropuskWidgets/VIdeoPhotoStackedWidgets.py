from PySide6.QtWidgets import QStackedWidget, QWidget, QLabel

class StackedWidget(QStackedWidget):
    def __init__(self, parent=None):
        super(StackedWidget, self).__init__(parent)
        
        self.addWidget()
    
    def setup_image_stacked(self) -> None:
        ...    
        
    def setup_video_stacked(self) -> None:
        ...    