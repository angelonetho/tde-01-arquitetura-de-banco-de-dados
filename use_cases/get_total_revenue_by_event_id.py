from db.connection import get_session
from db.models.events import Event
from db.models.tickets import Ticket
from db.models.ticket_types import TicketType
from sqlalchemy import func

session = get_session()


def execute(event_id):
    try:
        event = session.query(Event).where(Event.id == event_id).first()

        if not event:
            raise Exception("Event not found.")

        total_revenue = (
            session.query(func.sum(TicketType.price))
            .join(Ticket, Ticket.ticket_type_id == TicketType.id)
            .filter(TicketType.event_id == event_id)
            .scalar()  # `scalar` retorna o valor em vez de uma lista
        )
        return total_revenue or 0  # Retorna 0 se não houver ingressos para o evento
    finally:
        session.close()
