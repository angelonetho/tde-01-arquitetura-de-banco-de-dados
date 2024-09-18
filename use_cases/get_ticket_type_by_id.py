from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()

def execute(ticket_type_id):
    try:
        ticket_type = session.query(TicketType).where(TicketType.id == ticket_type_id).first()

        if not ticket_type:
            return 'Ticket type not found.'

        return ticket_type
    finally:
        session.close()
    