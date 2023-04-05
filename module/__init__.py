from datetime import datetime
import os



def create_filename() -> str:
    return os.path.join(os.environ.get('PHOTO_DIR'), F"propusk_{datetime.now().timestamp()}.jpg")

def create_path_qr() -> str:
    return os.path.join(os.environ.get('PHOTO_DIR'), F"qr_{datetime.now().timestamp()}.png")