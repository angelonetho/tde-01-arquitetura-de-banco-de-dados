from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute(name, cpf):
    try:
        employee = session.query(Employee).where(Employee.cpf == cpf).first()

        if employee:
            return 'Employee with same CPF already exists.'

        new_employee = Employee(name=name, cpf=cpf)
        session.add(new_employee)
        session.commit()

        return new_employee
    finally:
        session.close()