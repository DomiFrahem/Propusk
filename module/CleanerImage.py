from .WorkWithDB import connect, list_propusk
from sqlalchemy import select
from appdirs import user_data_dir
import os


class CleanerImage:
    def __init__(self, path: str):
        self._path = path
        
        if os.path.exists(path):    
            self._files_in_db = self._get_list_files_from_db()
        else:
            raise ValueError(F"Не корректный путь: {path}")

    def _get_list_files_from_db(self) -> list:
        with connect() as conn:
            list_files = select(
                list_propusk.c.face_photo,
                list_propusk.c.pasport_photo
            ).select_from(list_propusk)
            return sum([[self._only_file(x[0]), self._only_file(x[0])]
                        for x in conn.execute(list_files).all()], [])

    def _only_file(self, path: str) -> str:
        if '/' in path:
            return path.split('/')[-1]
        else:
            return path.split('\\')[-1]

    def clear(self) -> None:
        _, _, files = os.walk(self._path).__next__()
        for file in files:
            if file not in self._files_in_db:
                os.remove(os.path.join(self._path, file))
                print(F"Удален файл: {os.path.join(self._path, file)}")

