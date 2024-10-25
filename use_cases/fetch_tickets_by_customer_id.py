from db.connection import get_session
from db.models.customers import Customer
from db.models.tickets import Ticket

session = get_session()

def execute(customer_id):
    try:
        customer = session.query(Customer).where(Customer.id == customer_id).first()

        if not customer:
            raise Exception('Customer not found.')

        return session.query(Ticket).where(Ticket.customer_id == customer_id).all()
    finally:
        session.close()