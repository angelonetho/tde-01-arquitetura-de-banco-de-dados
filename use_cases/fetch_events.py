from db.connection import get_session
from db.models.events import Event

session = get_session()


def execute():
    try:
        return session.query(Event).all()
    finally:
        session.close()
