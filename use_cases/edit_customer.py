from db.connection import get_session
from db.models.customers import Customer

session = get_session()


def execute(customer_id, name=None, email=None, phone_number=None, birth_date=None):
    try:
        with session.begin():
            customer = session.query(Customer).where(Customer.id == customer_id).first()

            if not customer:
                raise Exception("Customer not found.")

            if name:
                customer.name = name

            if email:
                customer.email = email

            if phone_number:
                customer.phone_number = phone_number

            if birth_date:
                customer.birth_date = birth_date

            session.commit()

        return customer

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
