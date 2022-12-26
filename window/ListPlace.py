from .ui_py.ui_DialogListPlace import Ui_DialogListPlace
from PySide6.QtWidgets import QDialog, QListWidgetItem
from PySide6.QtCore import Qt, Slot
from module.WorkWithDB import connect, list_place


class ListPlace(QDialog, Ui_DialogListPlace):
    def __init__(self, parent=None) -> None:
        super(ListPlace, self).__init__(parent)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.setupUi(self)
    
        self.btn_save_place.clicked.connect(self._save)
        self.btn_update_place.clicked.connect(self._update)
        self.btn_delete_place.clicked.connect(self._delete)

        self.list_place_widget.itemSelectionChanged.connect(
            self._select_item
        )

        self._load_data()

    @Slot()
    def _save(self) -> None:
        with connect() as conn:
            insert_place = list_place.insert().values(
                name_place = self.line_name_place.text()
            )
            
            conn.execute(insert_place)
        
        self._clean_line_edit()
        self._load_data()

    @Slot()
    def _update(self) -> None:
        if hasattr(self, "selected_id"):
            with connect() as conn:
                update_place = list_place.update().where(
                    list_place.c.id == self.selected_id
                ).values(
                    name_place = self.line_name_place.text()
                )
                
                conn.execute(update_place)

            self._clean_line_edit()
            self._load_data()
        
        
    @Slot()
    def _delete(self) -> None:
        if hasattr(self, "selected_id"):
            with connect() as conn:
                conn.execute(
                    list_place.delete().where(
                        list_place.c.id == self.selected_id
                    )
                )
        
            self._clean_line_edit()
            self._load_data()
                

    def _clean_line_edit(self) -> None:
        self.line_name_place.clear()
        
        
    @Slot()
    def _select_item(self) -> None:
        try:
            id = self.list_place_widget.selectedItems()[0].id
            self.selected_id = int(id)
            
            with connect() as conn:
                place = list_place.select().where(
                    list_place.c.id == id)
                
                place_from_db = conn.execute(place).fetchone()
                self.line_name_place.setText(place_from_db.name_place)
                
        except IndexError:
            self._clean_line_edit()

    @Slot()
    def _load_data(self) -> None:
        self.list_place_widget.clear()
        
        with connect() as conn:
            for place in conn.execute(
                list_place.select()
            ).all():
                self.list_place_widget.addItem(
                    self._create_item(
                        id=place.id,
                        name_place=place.name_place
                    )
                )

    def _create_item(self, id: int, name_place: str) -> None:
        item = QListWidgetItem(name_place)
        item.id = id
        return item
