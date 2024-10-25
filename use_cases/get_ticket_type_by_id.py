from db.connection import get_session
from sqlalchemy.orm import joinedload
from db.models.ticket_types import TicketType

session = get_session()


def execute(ticket_type_id):
    try:
        ticket_type = (
            session.query(TicketType)
            .options(joinedload(TicketType.event))
            .filter(TicketType.id == ticket_type_id)
            .first()
        )

        if not ticket_type:
            raise Exception("Ticket type not found.")

        return ticket_type
    finally:
        session.close()
