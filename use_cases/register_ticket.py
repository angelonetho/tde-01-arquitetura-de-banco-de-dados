from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()

def execute(ticket_type_id, customer_id):
    try:
        new_ticket = Ticket(ticket_type_id=ticket_type_id, customer_id=customer_id)
        session.add(new_ticket)
        session.commit()
    finally:
        session.close()