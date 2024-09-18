from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute(employee_id):
    try:
        employee = session.query(Employee).where(Employee.id == employee_id).first()

        if employee is None:
            return 'Employee not found.'
        
        session.delete(employee)

        session.commit()
    finally:
        session.close()
    