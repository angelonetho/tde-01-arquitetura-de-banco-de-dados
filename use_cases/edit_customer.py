from db.connection import get_session
from db.models.customers import Customer

session = get_session()

def execute(customer_id, name=None, email=None, phone_number=None, birth_date=None):
    try:
        customer = session.query(Customer).where(Customer.id == customer_id).first()

        if customer == None:
            return 'Customer not found'
        
        if name != None:
            customer.name = name

        if email != None:
            customer.email = email

        if phone_number != None:
            customer.phone_number = phone_number

        if birth_date != None:
            customer.name = birth_date

        session.commit()

        return customer
    finally:
        session.close()
    