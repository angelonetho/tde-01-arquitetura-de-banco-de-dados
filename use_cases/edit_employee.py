from db.connection import get_session
from db.models.employees import Employee

session = get_session()

def execute(employee_id, name=None):
    try:
        employee = session.query(Employee).where(Employee.id == employee_id).first()

        if not employee:
            return 'Employee not found.'

        if name:
            employee.name = name

        session.commit()
        
        return employee
    finally:
        session.close()
    