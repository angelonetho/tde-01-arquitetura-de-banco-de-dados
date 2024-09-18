from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute(employee_id):
    try:
        employee = session.delete(Employee).where(Employee.id == employee_id).first()

        if employee == None:
            return 'Employee not found.'

        session.commit()
    finally:
        session.close()
    