#Setup the connection to the database using SQLAlchemy. The database URL is specified in the DATABASE_URL variable, which points to a SQLite
#  database file named "database.db". The create_engine function is used to create a database engine, and the sessionmaker function is used
# to create a session factory that will be used to interact with the database. The Base class is imported from the models module, which contains the ORM models for the application.
#  Finally, the Base.metadata.create_all function is called to create the necessary tables in the database based on the defined models.

from unittest.mock import Base #unittest.mock is used 

from fastapi import Depends

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session, declarative_base

engine = create_engine("sqlite:///database.db", connect_args={"check_same_thread": False})
sessionlocal = sessionmaker(bind=engine, autoflush=False, autocommit=False)
Base = declarative_base()

