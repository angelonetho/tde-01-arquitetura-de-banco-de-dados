from db.connection import get_session
from db.models.tickets import Ticket

session = get_session()


def execute(ticket_id):
    try:
        with session.begin():
            ticket = session.query(Ticket).where(Ticket.id == ticket_id).first()

            if ticket is None:
                raise Exception("Ticket not found.")

            session.delete(ticket)

            session.commit()

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
