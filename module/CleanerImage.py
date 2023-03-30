from .WorkWithDB import connect, list_propusk
from sqlalchemy import select
from appdirs import user_data_dir
import os
from logger import logger

class CleanerImage:
    def __init__(self, path: str):
        self._path = path
        
        if os.path.exists(path):    
            self._files_in_db = self._get_list_files_from_db()
        else:
            logger.error(F"Не корректный путь: {path}")
            raise ValueError(F"Не корректный путь: {path}")

    def _get_list_files_from_db(self) -> list:
        with connect() as conn:
            list_files = select(
                list_propusk.c.face,
                list_propusk.c.document
            ).select_from(list_propusk)
            
            result = conn.execute(list_files).all()
            
            images = []
            for face, document in result:
                images.append(face)
                images.append(document)
            
            return images

    def clear(self) -> None:
        _, _, files = os.walk(self._path).__next__()
        for file in files:
            if file not in self._files_in_db:
                os.remove(os.path.join(self._path, file))
                logger.info(F"Удален файл: {os.path.join(self._path, file)}")

