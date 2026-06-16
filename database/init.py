from sqlmodel import SQLModel
from database.connection import engine

def init_db():
    SQLModel.metadata.create_all(engine)