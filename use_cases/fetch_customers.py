from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()

def execute():
    try:
        return session.query(TicketType).all()
    finally:
        session.close()