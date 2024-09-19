from db.connection import get_session
from db.models.customers import Customer

session = get_session()

def execute():
    try:
        return session.query(Customer).all()
    finally:
        session.close()