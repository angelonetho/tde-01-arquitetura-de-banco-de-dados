from db.connection import get_session
from db.models.events import Event
from db.models.ticket_types import TicketType

session = get_session()

def execute(name, description, price, event_id):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if not event:
            return 'Event not found.'

        new_ticket_type = TicketType(name=name, description=description, price=price, event_id=event_id)
        
        session.add(new_ticket_type)

        session.commit()

        return new_ticket_type
    finally:
        session.close()