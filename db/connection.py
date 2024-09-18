from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy import create_engine

Base = declarative_base()

engine = create_engine("sqlite:///db/harutickets.db", echo=False)

def create_tables():
    Base.metadata.create_all(engine)

SessionFactory = sessionmaker(bind=engine)

def get_session():
    return SessionFactory() 