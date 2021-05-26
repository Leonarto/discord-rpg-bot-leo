import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, sessionmaker

# Database configuration
DB = settings.TEST_DB if settings.TESTING else settings.DB
engine = create_engine(DB, echo=False)
Session = sessionmaker()
Session.configure(bind=engine)
session = Session()

Base = declarative_base()

from models import *
import initial_data


def drop_db():
    Base.metadata.drop_all(engine)


def fill_db_with_starting_data():
    Base.metadata.create_all(engine)
    initial_data.add_hero_classes()


def db_from_scratch():
    drop_db()
    fill_db_with_starting_data()
