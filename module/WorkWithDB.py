from sqlalchemy import (MetaData, Table, Column, Integer,
                        DateTime, String, Text, ForeignKey,
                        create_engine, func)
import os
from module.MyMessageBox import show_dialog
from PySide6.QtWidgets import QMessageBox

meta = MetaData()

FILE_NAME = None
if os.environ.get("DB_DIR"):
    FILE_NAME = os.path.join(os.environ.get("DB_DIR"), "propusk.db")
else:
    if os.environ.get("DEFAULT_PATH"):
        FILE_NAME = os.path.join(os.environ.get("DEFAULT_PATH"), "propusk.db")
    else:
        show_dialog(
            QMessageBox.Icon.Critical,
            "Путь к бд",
            "Не правильно указан путь к базе данных, или вообще отсутствует"
        )
        raise ValueError(F"Не правильно указан путь к базе данных, или вообще отсутствует")
    
print("q", FILE_NAME)
    
cam_setting = Table("сam_setting", meta,
                    Column('id', Integer, primary_key=True),
                    Column("selected_cam", String, nullable=False),
                    Column('created', DateTime, default=func.now()),
                    Column('update', DateTime,
                           onupdate=func.current_timestamp())
                    )

list_personal = Table("list_personal", meta,
                      Column('id', Integer, primary_key=True),
                      Column('lastname', String, nullable=False),
                      Column('firstname', String, nullable=False),
                      Column('middlename', String, nullable=False),
                      Column('created', DateTime, default=func.now()),
                      Column('update', DateTime,
                             onupdate=func.current_timestamp())
                      )

list_place = Table("list_place", meta,
                   Column('id', Integer, primary_key=True),
                   Column('name_place', String, nullable=False),
                   Column('created', DateTime, default=func.now()),
                   Column('update', DateTime, onupdate=func.current_timestamp())
                   )

list_propusk = Table("list_propusk", meta,
                     Column("id", Integer, primary_key=True),
                     Column("id_propusk", Integer, nullable=False),
                     Column("date_from", DateTime, nullable=False),
                     Column("date_to", DateTime, nullable=False),
                     Column("personal", Integer, ForeignKey("list_personal.id"), nullable=False),
                     Column("place", Integer, ForeignKey("list_place.id"), nullable=False),
                     Column("receiving_man", Text, nullable=False),
                     Column("purpose_visite", Text, nullable=False),
                     Column("face_photo", Text, nullable=False),
                     Column("pasport_photo", Text, nullable=False),
                     Column("created", DateTime, default=func.now()),
                     Column("update", DateTime, default=func.now(),
                            onupdate=func.current_timestamp()))


engine = create_engine(F"sqlite:///{FILE_NAME}", echo=True)


def init_db():
    print(FILE_NAME)
    if not os.path.exists(os.path.dirname(FILE_NAME)):
        os.mkdir(os.path.dirname(FILE_NAME))

    meta.create_all(engine)


def connect():
    return engine.connect()
