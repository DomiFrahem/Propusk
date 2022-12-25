from .ui_py.WindowListPersonal import Ui_WindowListPersonal
from module.WorkWithDB import connect, list_personal
from module.MessageBox import showDialog

# from module.Decoration import clean_and_update_data
from PySide6.QtWidgets import QMainWindow, QListWidgetItem, QMessageBox
from PySide6.QtCore import Qt, Slot



class ListPersonal(QMainWindow, Ui_WindowListPersonal):
    def __init__(self, parent=None) -> None:
        super(ListPersonal, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)

        self.btn_save_personal.clicked.connect(self._save)
        self.btn_update_personal.clicked.connect(self._update)
        self.btn_delete_personal.clicked.connect(self._delete)

        self.list_personal_widget.itemSelectionChanged.connect(
            self._selected_item)
        self._load_data()
        

    @Slot()
    def _save(self) -> None:
        if any([
            self.lastname.text(),
            self.firstname.text(),
            self.middlename.text()]):
            with connect() as conn:
                insert_personal = list_personal.insert().values(
                 lastname=self.lastname.text(),
                firstname=self.firstname.text(),
                middlename=self.middlename.text()
                )
                conn.execute(insert_personal)

            self._clean_line_edit()
            self._load_data()
        else:
            showDialog(
                    QMessageBox.Warning,
                    title="Пустые поля",
                    massage="Заполните все поля!"
                )
            
    def _clean_line_edit(self):
        self.lastname.clear()
        self.firstname.clear()
        self.middlename.clear()

    @Slot()
    def _update(self) -> None:
        with connect() as conn:
            update_personal = list_personal.update().where(
                list_personal.c.id == self.selected_id
            ).values(
                lastname=self.lastname.text(),
                firstname=self.firstname.text(),
                middlename=self.middlename.text()
            )

            conn.execute(update_personal)
        self._clean_line_edit()
        self._load_data()

    @Slot()
    def _delete(self) -> None:
        with connect() as conn:
            if hasattr(self, 'selected_id'):
                conn.execute(
                    list_personal.delete().where(
                        list_personal.c.id == self.selected_id)
                )
            else:
                showDialog(
                    QMessageBox.Warning,
                    title="Не выбран элемент списка",
                    massage="Выбирите элемент списка перед тем как удалять!"
                )

        self._clean_line_edit()
        self._load_data()

    @Slot()
    def _selected_item(self) -> None:
        try:
            id = self.list_personal_widget.selectedItems()[0].id
            self.selected_id = int(id)
            with connect() as conn:
                personal = list_personal.select().where(
                    list_personal.c.id == id)
                personal_from_db = conn.execute(personal).fetchone()

                self.lastname.setText(personal_from_db.lastname)
                self.firstname.setText(personal_from_db.firstname)
                self.middlename.setText(personal_from_db.middlename)

        except IndexError:
            self._clean_line_edit()

    def _load_data(self) -> None:
        self.list_personal_widget.clear()
        with connect() as conn:
            for personal in conn.execute(list_personal.select()).all():
                self.list_personal_widget.addItem(self._create_item(
                    id=personal.id,
                    lastname=personal.lastname,
                    firstname=personal.firstname,
                    middlename=personal.middlename
                ))

    def _create_item(self, id, lastname, firstname, middlename) -> None:
        item = QListWidgetItem(F"{lastname} {firstname} {middlename}")
        item.id = id
        return item
