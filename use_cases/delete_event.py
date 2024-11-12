from db.connection import get_session
from db.models.events import Event

session = get_session()


def execute(event_id):
    try:
        with session.begin():
            event = session.query(Event).where(Event.id == event_id).first()

            if event is None:
                raise Exception("Event not found.")

            session.delete(event)

            session.commit()

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
