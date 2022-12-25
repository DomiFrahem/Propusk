from sqlalchemy import (MetaData, Table, Column, Integer,
                        DateTime, String, Text, ForeignKey,
                        create_engine, func)
import os
import appdirs

meta = MetaData()

PATH = os.path.join(appdirs.user_data_dir(), "propusk").replace('\\', '\\\\')
FILE_NAME = os.path.join(PATH, "propusk.db").replace('\\', '\\\\')

cam_setting = Table("сam_setting", meta,
                    Column('id', Integer, primary_key=True),
                    Column("selected_cam", Integer, nullable=False),
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
    if not os.path.exists(PATH):
        os.mkdir(PATH)

    meta.create_all(engine)


def connect():
    return engine.connect()
