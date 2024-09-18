from db.connection import get_session
from db.models.customers import Customer

session = get_session()

def execute(customer_id):
    try:
        customer = session.query(Customer).where(Customer.id == customer_id).first()

        if customer == None:
            return 'Customer not found.'

        return customer
    finally:
        session.close()
    