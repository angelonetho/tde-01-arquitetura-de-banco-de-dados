from db.connection import get_session
from db.models.customers import Customer
from db.models.tickets import Ticket
from sqlalchemy.orm import joinedload

session = get_session()


def execute(customer_id):
    try:
        customer = session.query(Customer).where(Customer.id == customer_id).first()

        if not customer:
            raise Exception("Customer not found.")

        return (
            session.query(Ticket)
            .options(
                joinedload(Ticket.ticket_type),
                joinedload(Ticket.customer),
                joinedload(Ticket.employee),
            )
            .filter(Ticket.customer_id == customer_id)
            .all()
        )
    finally:
        session.close()
