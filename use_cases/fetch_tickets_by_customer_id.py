from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()

def execute(customer_id):
    try:
        return session.query(Ticket).where(Ticket.customer_id == customer_id)
    finally:
        session.close()