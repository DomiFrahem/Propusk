from .ui_py.ui_DialogSettingCam import Ui_DialogSettingCam
from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Qt, Slot

from module.WorkWithDB import *
from widgets import create_widget_cam_shecked
from logger import logger


class SettingCam(QDialog, Ui_DialogSettingCam):
    def __init__(self, parent=None) -> None:
        super(SettingCam, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.widget = None

        self.__mode = self.mode_list.currentData()
        self.__load_cams_from_db()

        self.save_setting_cam.clicked.connect(self.__save_cams)
        self.mode_list.currentIndexChanged.connect(self.__change_mode)
        self.tabWidget.currentChanged.connect(self.__change_type)

        # self.__recreate_widget()

    def __change_type(self) -> None:
        if self.tabWidget.currentIndex() == 1:
            self.__mode = 'document'

        self.__load_cams_from_db()

    def __change_mode(self) -> None:
        self.__mode = self.mode_list.currentData()
        self.__recreate_widget(self.__mode)
        logger.info(F'Change cams to {self.__mode}')

    @Slot()
    def __recreate_widget(self, select_mode: str = 'video') -> None:
        self.__del_widget()
        if self.tabWidget.currentIndex() == 0:
            self.widget = create_widget_cam_shecked(mode=select_mode,
                name_object=u'widget',
                obj=self.tab,
                layout=self.verticalLayout)
        else:
            self.widget = create_widget_cam_shecked(
                name_object=U'widget',
                obj=self.tab_2,
                layout=self.verticalLayout_3)


    def __del_widget(self) -> None:
        if self.widget is not None:
            self.verticalLayout.removeWidget(self.widget)
            self.verticalLayout_3.removeWidget(self.widget)

        self.widget = None

    def __load_cams_from_db(self):
        with connect() as conn:
            result = conn.execute(cam_setting.select().where(
                cam_setting.c.type == self.tabWidget.currentIndex()
            )).fetchone()
            if result:
                self.__mode = result.mode
                self.__recreate_widget(self.__mode)
                match self.__mode:
                    case 'video':
                        self.mode_list.setCurrentIndex(0)
                        self.widget.line_cam.setCurrentText(
                            result.selected_cam)
                    case 'snapshot':
                        self.mode_list.setCurrentIndex(1)
                        self.widget.line_cam.setText(result.selected_cam)
                    case 'document':
                        self.widget.line_cam.setCurrentText(
                            result.selected_cam)
                    case _: ...
            else: self.__recreate_widget()

    def __save_cams(self) -> None:
        query = None
        with connect() as conn:
            result = conn.execute(cam_setting.select().where(
                cam_setting.c.type == self.tabWidget.currentIndex()
            )).fetchone()
            if result is None:
                query = cam_setting.insert().values(
                    type=self.tabWidget.currentIndex(),
                    mode=self.__mode,
                    selected_cam=self.widget.get_value())
            else:
                query = cam_setting.update().where(
                    cam_setting.c.type == self.tabWidget.currentIndex()
                ).values(mode=self.__mode, selected_cam=self.widget.get_value())
            result = conn.execute(query)
