from .ui_py.ui_DialogSettingCam import Ui_DialogSettingCam
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt

from module.WorkWithDB import *
from PropuskWidgets.PCamChecked import PCamChecked
from logger import logger


class SettingCam(QDialog, Ui_DialogSettingCam):
    def __init__(self, parent=None) -> None:
        super(SettingCam, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.save_setting_cam.clicked.connect(self.__save_cams)
        self.mode_list.currentTextChanged.connect(self.__change_mode)

        # self.__recreate_widget()
        self.__load_cams_from_db()
        self.__mode = self.mode_list.currentData()


    def __change_mode(self) -> None:
        self.__mode = self.mode_list.currentData()
        self.__recreate_widget(self.__mode)
        logger.info(F'Change cams to {self.__mode}')

    def __recreate_widget(self, select_mode: str = 'video') -> None:
        if hasattr(self, 'widget'):
            delattr(self, 'widget')

        self.widget = PCamChecked(self.groupBox, mode=select_mode)
        self.widget.setObjectName('widget')
        self.gridLayout_3.addWidget(self.widget, 1, 0, 1, 1)

    def __load_cams_from_db(self):
        with connect() as conn:
            result = conn.execute(cam_setting.select()).fetchone()
            if result:
                self.__recreate_widget(result.mode)
                match result.mode:
                    case 'video': self.widget.line_cam.setCurrentText(result.mode)
                    case 'snapshot': self.widget.line_cam.setText(result.selected_cam)
            else: self.__recreate_widget()

    def __save_cams(self) -> None:
        query = None
        with connect() as conn:
            result = conn.execute(cam_setting.select()).fetchone()
            if result is None:
                query = cam_setting.insert().values(
                    mode=self.__mode, selected_cam=self.widget.get_value())
            else:
                query = cam_setting.update().where(
                    cam_setting.c.id == 1).values(mode=self.__mode, selected_cam=self.widget.get_value())
            result = conn.execute(query)
