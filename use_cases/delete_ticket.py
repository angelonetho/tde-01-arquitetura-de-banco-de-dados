from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()

def execute(ticket_id):
    try:
        ticket = session.delete(Ticket).where(Ticket.id == ticket_id).first()

        if ticket == None:
            return 'Ticket not found.'

        session.commit()
    finally:
        session.close()
    