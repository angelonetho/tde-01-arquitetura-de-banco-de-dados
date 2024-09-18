from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute():
    try:
        return session.query(Employee).all()
    finally:
        session.close()