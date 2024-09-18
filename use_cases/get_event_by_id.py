from db.connection import get_session
from db.models.events import Event

session = get_session()

def execute(event_id):
    try:
        event = session.query(Event).where(Event.id == event_id).first()
        return event
    finally:
        session.close()
    