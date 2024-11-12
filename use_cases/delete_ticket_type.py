from db.connection import get_session
from db.models.ticket_types import TicketType

session = get_session()


def execute(ticket_type_id):
    try:
        with session.begin():
            ticket_type = (
                session.query(TicketType).where(TicketType.id == ticket_type_id).first()
            )

            if ticket_type is None:
                raise Exception("Ticket type not found.")

            session.delete(ticket_type)

            session.commit()

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
