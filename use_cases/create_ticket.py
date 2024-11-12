from db.connection import get_session
from db.models.tickets import Ticket
from db.models.ticket_types import TicketType
from db.models.customers import Customer

session = get_session()


def execute(ticket_type_id, customer_id):
    try:
        with session.begin():
            ticket_type = (
                session.query(TicketType).where(TicketType.id == ticket_type_id).first()
            )
            if not ticket_type:
                raise Exception("Ticket Type not found.")

            customer = session.query(Customer).where(Customer.id == customer_id).first()
            if not customer:
                raise Exception("Customer not found.")

            new_ticket = Ticket(ticket_type_id=ticket_type_id, customer_id=customer_id)
            session.add(new_ticket)

            session.commit()

        return new_ticket

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
