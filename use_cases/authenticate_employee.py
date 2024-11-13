from db.connection import get_session
from db.models.employees import Employee

session = get_session()


def execute(employee_id, cpf):
    try:
        employee = (
            session.query(Employee)
            .filter(Employee.id == employee_id, Employee.cpf == cpf)
            .first()
        )

        if not employee:
            raise Exception("Employee not found or credentials are incorrect.")

        return employee
    finally:
        session.close()
