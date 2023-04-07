from PySide6.QtWidgets import QDialog
from PySide6.QtPrintSupport import QPrintDialog, QPrinter
from PySide6.QtGui import QPainter, QPixmap, QPageSize
from PySide6.QtCore import Qt
import pdfkit
from module import create_filename
from pdf2image import convert_from_path


class Print:
    def __init__(self, text: str) -> None:
        
        self.printer = QPrinter()
        self.printer.setFullPage(True)
        self.printer.setPageSize(QPageSize.A4)
        
        pdf  = CreatorPDF(text)
        image = convert_from_path(pdf.get_path_to_pdf())[0].toqimage()
        image = QPixmap.fromImage(image)
        # print(self.printer.pageRect())
        image = image.scaledToWidth(self.printer.width(), Qt.SmoothTransformation)
        
        dialog = QPrintDialog(self.printer)
        if dialog.exec() == QDialog.Accepted:
            self.handle_paint_request(image)

        
    def handle_paint_request(self, im):
        painter = QPainter(self.printer)
        
        painter.drawPixmap(0, 0, im)
        painter.end()
       


class CreatorPDF():
    def __init__(self, text_html):
        self.__file_name = create_filename('pdf')
        # self.__file_name = 'pdf.pdf'
        configuration = pdfkit.configuration(
            wkhtmltopdf="/usr/bin/wkhtmltopdf")
        pdfkit.from_string(text_html, self.__file_name, configuration=configuration, css=None, options={
            "enable-local-file-access": ""
        })
        
    def get_path_to_pdf(self) -> str:
        return self.__file_name
 