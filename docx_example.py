from random import random
from platform import system
from weasyprint import HTML
from jinja2 import Environment, FileSystemLoader
import os
from module.Printer import Printer
from PySide6.QtWidgets import QApplication

# import printfactory
# from PySide6.QtGui import QtPrinter

# with open("/home/asidorov/project/propusk/docs/template_propusk.html") as file:
#     document = BeautifulSoup(file, 'html.parser')
    
#     for teg in document.find_all("number_propusk"):
#         teg.string = teg.string.replace("number_propusk", "dfhlkasbdfbkasd")
#         # teg["text"] = teg.contents[0].replace("number_propusk", "dfhlkasbdfbkasd")
#         # teg.contents[0] = str(73649718263481)
        
#     print(document)
# path_photo = "/home/asidorov/project/propusk/image/no_media_main.jpg"
app = QApplication([])

dir_path = os.path.dirname(os.path.abspath(__file__))
env = Environment(loader=FileSystemLoader(dir_path))

template_vars = {
    "number_propusk": "85875875687",
    "date_from": "lkjhkljahdfks",
    "image_face": F'file://{os.path.join(dir_path, "image", "no_media_main.jpg")}',
    "image_pasport": F'file://{os.path.join(dir_path, "image", "no_media_main.jpg")}'
}

template = env.get_template('docs/template_propusk.html')
text = template.render(template_vars)
HTML(string=template.render(template_vars)).write_pdf("pdftest.pdf")


# printer = Printer(os.path.join(dir_path, "pdftest.pdf"))
printer = Printer(text)
printer.print()

# with open("test.html", "w") as f:
#     f.write(text)
    
# HTML(string=template.render(template_vars)).write_pdf("pdftest.pdf")

# print(system())
    