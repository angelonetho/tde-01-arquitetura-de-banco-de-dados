from db.connection import get_session
from db.models.customers import Customer

session = get_session()


def execute(customer_id):
    try:
        with session.begin():
            customer = session.query(Customer).where(Customer.id == customer_id).first()

            if customer is None:
                raise Exception("Customer not found.")

            session.delete(customer)

            session.commit()

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
