from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()

def execute(event_id):
    try:
        return session.query(TicketType).where(TicketType.event_id == event_id)
    finally:
        session.close()