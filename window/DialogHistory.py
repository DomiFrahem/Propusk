import os

# from module.ImageTool import rotate_image
from pdf2image import convert_from_path
from PySide6.QtCore import Slot
from PySide6.QtGui import QPixmap
from PySide6.QtWidgets import QDialog
from sqlalchemy import func, select

from logger import logger
from module import create_filename
from module.ModelPropusk import PropuskDataMethods
from module.Printer import CreatorPDF
from module.QRCode import make
from module.TemplatePropusk import TemplatePropusk
from module.WorkWithDB import connect, list_personal, list_place, list_propusk

from .ui_py.ui_DialogHistory import Ui_DialogHistory


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
        except IndexError as err:
            logger.debug(err)
            self.browser.clear()
        except OSError as err:
            logger.debug(err)

    @Slot(str)
    def filter_items(self, text: str) -> None:
        for index in range(self.list_propusk.count()):
            item = self.list_propusk.item(index)
            if text:
                item.setHidden(not self.match_text(text, item.text()))
            else:
                item.setHidden(False)

    def match_text(self, text: str, keywords:str) -> bool:
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
                    list_propusk.c.face,
                    list_propusk.c.document
                ).select_from(list_propusk).join(
                    list_personal, list_propusk.c.personal == list_personal.c.id
                ).join(
                    list_place, list_propusk.c.place == list_place.c.id
                ).where(list_propusk.c.id_propusk == id_propusk)
            ).fetchone()

            pdm = PropuskDataMethods(*row)
            face = os.path.join(os.environ.get(
                'PHOTO_DIR'), pdm.get_value("face"))
            documet = os.path.join(os.environ.get(
                'PHOTO_DIR'), pdm.get_value("document"))
            pdm.set_value("face", face)
            pdm.set_value("document", documet)
            pdm.set_value("qrcode", make(pdm.get_value('id_propusk'), create_filename('qr')))

            path_doc = os.path.join(os.path.dirname(os.path.abspath(__package__)), 'docs')
            render_text = str(TemplatePropusk(pdm._propusk_data.__dict__, path_doc))
            # print(render_text)
            
            # Print(render_text)
            pdf = CreatorPDF(render_text)
            image  = convert_from_path(pdf.get_path_to_pdf())[0]
            image_path = create_filename()
            QPixmap.fromImage(image.toqimage()).save(image_path, 'jpg')
            
            self.browser.setText(F"<img src='file:{image_path}'>")
