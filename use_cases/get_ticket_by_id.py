from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()

def execute(ticket_id):
    try:
        ticket = session.query(Ticket).where(Ticket.id == ticket_id).first()
        return ticket
    finally:
        session.close()
    