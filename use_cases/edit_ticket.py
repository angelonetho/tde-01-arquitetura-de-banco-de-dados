from db.connection import get_session
from db.models.tickets import Ticket
from db.models.ticket_types import TicketType

session = get_session()

def execute(ticket_id, ticket_type_id=None):
    try:
        ticket = session.query(Ticket).where(Ticket.id == ticket_id).first()

        if not ticket:
            raise Exception('Ticket not found.')

        if ticket_type_id:

            ticket_type = session.query(TicketType).where(TicketType.id == ticket_type_id).first()

            if not ticket_type: raise Exception('Ticket type not found.')

            ticket.ticket_type_id = ticket_type_id

        session.commit()
        
        return ticket
    finally:
        session.close()
    