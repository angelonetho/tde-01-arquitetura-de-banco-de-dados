from db.connection import get_session
from db.models.events import Event
from db.models.tickets import Ticket
from db.models.ticket_types import TicketType
from sqlalchemy.orm import joinedload

session = get_session()


def execute(event_id):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if not event:
            raise Exception("Event not found.")

        tickets = (
            session.query(Ticket)
            .options(
                joinedload(Ticket.ticket_type),
                joinedload(Ticket.customer),
                joinedload(Ticket.employee),
            )
            .join(TicketType, Ticket.ticket_type_id == TicketType.id)
            .filter(TicketType.event_id == event_id)
            .all()
        )
        return tickets
    finally:
        session.close()
