from PIL import Image, UnidentifiedImageError
import os
from logger import logger
from datetime import datetime


def rotate_image(path_file: str, gradus: int = -90) -> str:
    try:
        image = Image.open(path_file, 'r')
        rotate_path_image = os.path.join(
            os.path.dirname(image.filename),
            F"rotate_{os.path.split(image.filename)[1]}"
        )
    
        rotate_img = image.rotate(gradus, expand=True)
        rotate_img.save(rotate_path_image)
    
        return rotate_path_image
    
    except FileNotFoundError:
        logger.error(F"Файл не найден: {path_file=}")
        return None
    except UnidentifiedImageError:
        logger.error(F"Не правильный формат: {path_file=}")
        return None


def create_filename() -> str:
    return os.path.join(os.environ.get('PHOTO_DIR'), F"propusk_{datetime.now().timestamp()}.jpg")
