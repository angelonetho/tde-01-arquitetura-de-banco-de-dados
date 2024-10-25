from db.connection import get_session
from db.models.events import Event

session = get_session()


def execute(event_id, name=None, description=None, avenue=None, event_time=None):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if not event:
            raise Exception("Event not found.")

        if name:
            event.name = name

        if description:
            event.description = description

        if avenue:
            event.avenue = avenue

        if event_time:
            event.event_time = event_time

        session.commit()

        return event
    finally:
        session.close()
