from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()

def execute(name, description, price, event_id):
    try:
        new_ticket_type = TicketType(name=name, description=description, price=price, event_id=event_id)
        session.add(new_ticket_type)
        session.commit()
    finally:
        session.close()