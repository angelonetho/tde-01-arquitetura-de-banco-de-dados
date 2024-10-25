from db.connection import get_session
from db.models.tickets import Ticket
from sqlalchemy.orm import joinedload

session = get_session()


def execute(ticket_id):
    try:
        ticket = (
            session.query(Ticket)
            .options(
                joinedload(Ticket.ticket_type),
                joinedload(Ticket.customer),
                joinedload(Ticket.employee),
            )
            .filter(Ticket.id == ticket_id)
            .first()
        )

        if not ticket:
            raise Exception("Ticket not found.")

        return ticket
    finally:
        session.close()
