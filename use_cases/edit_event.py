from db.connection import get_session
from db.models.events import Event

session = get_session()

def execute(event_id, name=None, description=None, avenue=None, event_time=None):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if name != None:
            event.name = name

        if description != None:
            event.description = description

        if avenue != None:
            event.avenue = avenue

        if event_time != None:
            event.event_time = event_time

        session.commit()
        
        return event
    finally:
        session.close()
    