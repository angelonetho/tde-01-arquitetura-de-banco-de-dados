from db.connection import get_session
from db.models.employees import Employee

session = get_session()


def execute(employee_id, name=None):
    try:
        with session.begin():
            employee = session.query(Employee).where(Employee.id == employee_id).first()

            if not employee:
                raise Exception("Employee not found.")

            if name:
                employee.name = name

            session.commit()

        return employee

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
