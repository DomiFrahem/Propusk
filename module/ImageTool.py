from PIL import Image, UnidentifiedImageError
import os
from logger import logger
from datetime import datetime
import cv2


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



def cupture_face(path_photo) -> None:
    img = cv2.imread(path_photo)
    face_recog = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    face_result = face_recog.detectMultiScale(img, scaleFactor=2, minNeighbors=3)
    print(face_result)
    if len(face_result) != 0:
        
        x,y,w,h = face_result[-1]
        
        img = img[y-50:y+h+80,x-50:x+50+w]
        cv2.imwrite(F"propusk_{datetime.now().timestamp()}.jpg", img)
            
        # cv2.imshow("Result", img)
        #Этот метод выводит результат на экран. Первый аргумент - что то по типу комментария к картинке, второй - сама картинка
        # cv2.waitKey(0)
