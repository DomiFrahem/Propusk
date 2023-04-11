from datetime import datetime
import os
import platform
import subprocess
from module.MyMessageBox import show_dialog
from PySide6.QtWidgets import QMessageBox



def create_filename(prefix: str = "propusk") -> str:
    return os.path.join(os.environ.get('PHOTO_DIR'), F"{prefix}_{datetime.now().timestamp()}.jpg")

def get_path_wkhtmltopdf() -> str:
    match platform.system():
        case 'Linux':
            result = subprocess.Popen(['whereis wkhtmltopdf'], shell=True, stdout=subprocess.PIPE).stdout.read()
            return str(result).split(' ')[1]
        case 'Windows':
            path_window_programm = "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe"
            if os.path.exists(path_window_programm):
                return path_window_programm
            else:
                show_dialog(QMessageBox.Icon.Critical, 
                            "Не найдено ПО",
                            "Не установлена программа wkhtmltopdf")
        case _: ...
    
    
