from db.connection import get_session
from db.models.events import Event
from db.models.ticket_types import TicketType

session = get_session()


def execute(event_id):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if not event:
            raise Exception("Event not found.")

        return session.query(TicketType).where(TicketType.event_id == event_id).all()
    finally:
        session.close()
