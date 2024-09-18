from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()

def execute(event_id):
    try:
        return session.query(Ticket).where(Ticket.customer_id == event_id)
    finally:
        session.close()