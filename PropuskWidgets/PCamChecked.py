
from PySide6.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QComboBox, QPushButton, QMessageBox
from PropuskWidgets.PStackedWidget import PStackedWidget
from module.cam import IPCam, USBCam, get_list_name_cam, check_error
from module.MyMessageBox import show_dialog
from time import sleep


class PCamChecked(QWidget):
    def __init__(self, parent=None, mode: str = 'video') -> None:
        super().__init__(parent)

        self.__mode = mode
        self.vLayout = QVBoxLayout(self)
        self.vLayout.setObjectName(u'vLayout')

        match self.__mode:
            case 'video':
                self.line_cam = QComboBox(self)
                # load list cam
                [self.line_cam.addItem(x) for x in get_list_name_cam()]
            case 'snapshot': self.line_cam = QLineEdit(self)

        self.line_cam.setObjectName(u"line_cam")
        self.vLayout.addWidget(self.line_cam)

        self.pStackedWidget = PStackedWidget(self, mode=mode)
        self.pStackedWidget.setObjectName(u'pStackedWidget')
        self.vLayout.addWidget(self.pStackedWidget)

        self.hLayout = QHBoxLayout()
        self.hLayout.setObjectName(u'hLayout')

        self.btn_check = QPushButton(self)
        self.btn_check.setObjectName('btn_check')
        self.btn_check.setText('Проверить')
        self.btn_check.clicked.connect(self.__start_cam)
        self.hLayout.addWidget(self.btn_check)

        self.btn_stop = QPushButton(self)
        self.btn_stop.setObjectName('btn_stop')
        self.btn_stop.setText('Остановить')
        self.btn_stop.clicked.connect(self.__stop_cam)
        self.hLayout.addWidget(self.btn_stop)

        self.vLayout.addLayout(self.hLayout)

    def get_value(self) -> str:
        match self.__mode:
            case 'video':
                return self.line_cam.currentText()
            case 'snapshot':
                return self.line_cam.text()
            case _: return None

    def __start_cam(self) -> None:
        
        match self.__mode:
            case 'video':
                self.pStackedWidget.to_video()
                self.__wwc = USBCam(self.pStackedWidget.video,
                                    self.line_cam.currentText())
                self.__wwc.start_cam()
            case 'snapshot':
                self.pStackedWidget.to_video()
                self.__wwc = IPCam()
                self.__wwc.qLabel = self.pStackedWidget.video
                self.__wwc.lnk_connect = self.line_cam.text()
                self.__wwc.start()
                    
            case _: return None

    def __stop_cam(self):
        self.__wwc.stop_cam()
        del self.__wwc
        self.pStackedWidget.to_image()
        
    def __del__(self) -> None:
        self.__stop_cam