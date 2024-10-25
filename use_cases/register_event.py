from db.connection import get_session
from db.models.events import Event

session = get_session()


def execute(name, description, avenue, event_time):
    try:
        new_event = Event(
            name=name, description=description, avenue=avenue, event_time=event_time
        )
        session.add(new_event)
        session.commit()

        return new_event
    finally:
        session.close()
