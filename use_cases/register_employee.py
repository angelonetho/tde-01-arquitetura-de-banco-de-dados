from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute(name, cpf):
    new_employee = Employee(name=name, cpf=cpf)
    session.add(new_employee)
    session.commit()
    session.close()