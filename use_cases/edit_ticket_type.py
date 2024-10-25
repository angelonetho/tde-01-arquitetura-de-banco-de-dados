from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()


def execute(ticket_type_id, name=None, description=None, price=None):
    try:
        ticket_type = (
            session.query(TicketType).where(TicketType.id == ticket_type_id).first()
        )

        if not ticket_type:
            raise Exception("Ticket type not found.")

        if name:
            ticket_type.name = name

        if description:
            ticket_type.description = description

        if price:
            ticket_type.price = price

        session.commit()

        return ticket_type
    finally:
        session.close()
