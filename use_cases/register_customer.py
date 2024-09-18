from db.connection import get_session
from db.models.customers import Customer

session = get_session()

def execute(name, cpf, email, password, birth_date):
    try:
        new_customer = Customer(name=name, cpf=cpf, email=email, password=password, birth_date=birth_date)
        session.add(new_customer)
        session.commit()
        session.close()
    finally:
        session.close()