from PySide6.QtWidgets import QDialog
from PySide6.QtCore import Slot
from .ui_py.ui_DialogHistory import Ui_DialogHistory
from module.WorkWithDB import connect, list_propusk, list_personal, list_place
from sqlalchemy import select, func
from module.ModelPropusk import PropuskDataMethods
from module.TemplatePropusk import TemplatePropusk
import os
from module.ImageTool import rotate_image
# from PySide6.QtGui import QStandardItemModel


class DialogHistory(Ui_DialogHistory, QDialog):
    def __init__(self, parent=None):
        super(DialogHistory, self).__init__(parent)
        self.setupUi(self)
        self.line_search.textChanged.connect(
            self.filter_items
        )
        self.list_propusk.itemSelectionChanged.connect(
            self.selected_item
        )

        self.load_data()

        self.list_propusk.setCurrentRow(0)

    def selected_item(self) -> None:
        try:
            id_propusk = self.list_propusk.selectedItems()[0].text()
            self.load_page(int(id_propusk))
        except IndexError:
            self.browser.clear()

    @Slot(str)
    def filter_items(self, text: str) -> None:
        for index in range(self.list_propusk.count()):
            item = self.list_propusk.item(index)
            if text:
                item.setHidden(not self.match_text(text, item.text()))
            else:
                item.setHidden(False)

    def match_text(self, text, keywords) -> None:
        return text in keywords

    def load_data(self) -> None:
        with connect() as conn:
            rows = conn.execute(
                list_propusk.select()) \
                .all()

            for line in rows:
                self.list_propusk.addItem(str(line.id_propusk))

    def load_page(self, id_propusk: int) -> None:
        with connect() as conn:
            row = conn.execute(
                select(
                    list_propusk.c.id_propusk,
                    list_propusk.c.date_from,
                    list_propusk.c.date_to,
                    func.format(
                        list_personal.c.lastname
                        + " " + list_personal.c.firstname
                        + " " + list_personal.c.middlename)
                    .label("personal"),
                    func.format(list_place.c.name_place).label("place"),
                    list_propusk.c.receiving_man,
                    list_propusk.c.purpose_visite,
                    list_propusk.c.face_photo
                ).select_from(list_propusk).join(
                    list_personal, list_propusk.c.personal == list_personal.c.id
                ).where(list_propusk.c.id_propusk == id_propusk)
            ).fetchone()

            pdm = PropuskDataMethods(*row)
            pdm.set_value("face_photo",
                          rotate_image(pdm.get_value("face_photo"))
                          )
            
            render_text = str(TemplatePropusk(pdm._propusk_data.__dict__,
                                              os.path.join(os.path.dirname(
                                                  os.path.abspath(__package__)), 'docs')
                                              ))

            self.browser.setText(render_text)
