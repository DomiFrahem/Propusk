from .ui_py.ui_DialogCustomVariables import Ui_DialogCustomVariables
from PySide6.QtWidgets import QDialog, QFileDialog, QMessageBox
from PySide6.QtCore import Qt
from module.MyMessageBox import show_dialog


class DialogCustomVariables(Ui_DialogCustomVariables, QDialog):
    def __init__(self, parent: str = None) -> None:
        self.path_env = parent
        super(DialogCustomVariables, self).__init__()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.btn_show_path_photo.clicked.connect(
            self._show_path_photo
        )

        self.btn_show_path_database.clicked.connect(
            self._show_path_database
        )

        self.btn_save.clicked.connect(
            self._save
        )

    def _show_path_photo(self) -> None:
        dir = str(QFileDialog.getExistingDirectory(None, "Выбрать директорию где будут храниться фоотографии"))
        self.path_photo.setText(dir)

    def _show_path_database(self) -> None:
        dir = str(QFileDialog.getExistingDirectory(None, "Выбрать директорию где будет храниться база данных"))
        self.path_db.setText(dir)

    def _save(self) -> None:
        with open(self.path_env, 'w+', encoding="utf-8") as file:
            file.write(F"DB_DIR={self.path_db.text()} \n")
            file.write(F"PHOTO_DIR={self.path_photo.text()} \n")

        show_dialog(QMessageBox.Icon.Information,
                    "Успешно!",
                    "Сохранения произошло успешно!")
        self.close()
