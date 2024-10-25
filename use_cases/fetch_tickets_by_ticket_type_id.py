from db.connection import get_session
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket

session = get_session()

def execute(ticket_type_id):
    try:
        ticket_type = session.query(TicketType).where(TicketType.id == ticket_type_id).first()

        if not ticket_type:
            raise Exception('Ticket type not found.')

        return session.query(Ticket).where(Ticket.ticket_type_id == ticket_type_id).all()
    finally:
        session.close()