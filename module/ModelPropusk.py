from datetime import datetime
from dataclasses import dataclass
from logger import logger


def key_error(func):
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            logger.info("ModelPropusk -> Ключ не правильный")

    return wrapper


@dataclass
class Personal:
    id: int
    name: str


@dataclass
class Place:
    id: int
    name: str


@dataclass
class PropuskData:
    id_propusk: int
    date_from: datetime
    date_to: datetime
    personal: Personal
    place: Place
    receiving_man: str
    purpose_visite: str
    face_photo: str


class PropuskDataMethods:
    def __init__(self, id_propusk: int = None,
                 date_from: datetime = None,
                 date_to: datetime = None,
                 personal: Personal = None,
                 place: Place = None,
                 receiving_man: str = None,
                 purpose_visite: str = None,
                 face_photo: str = None):

        self._propusk_data = PropuskData(id_propusk,
                                         date_from,
                                         date_to,
                                         personal,
                                         place,
                                         receiving_man,
                                         purpose_visite,
                                         face_photo)

    @key_error
    def set_value(self, key: str, value: str | int | datetime | Personal | Place):
        #Пустышка если ключа не существует выкенет из функции
        self._propusk_data.__dict__[key] 
        self._propusk_data.__dict__[key] = value

    @key_error
    def get_value(self, key):
        return self._propusk_data.__dict__[key]

    def checking_empty_values(self) -> bool:
        return all(self._propusk_data.__dict__.values())

