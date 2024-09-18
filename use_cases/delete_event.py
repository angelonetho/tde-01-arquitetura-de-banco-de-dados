from db.connection import get_session
from db.models.events import Event

session = get_session()

def execute(event_id):
    try:
        event = session.delete(Event).where(Event.id == event_id).first()

        if event == None:
            return 'Event not found.'

        session.commit()
    finally:
        session.close()
    