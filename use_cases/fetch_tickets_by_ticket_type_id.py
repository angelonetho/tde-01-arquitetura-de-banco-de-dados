from db.connection import get_session
from db.models.events import Event
from db.models.tickets import Ticket

session = get_session()

def execute(ticket_type_id):
    try:
        event = session.query(Event).where(Event.id == ticket_type_id).first()

        if not event:
            return 'Ticket type not found.'

        return session.query(Ticket).where(Ticket.ticket_type == ticket_type_id).all()
    finally:
        session.close()