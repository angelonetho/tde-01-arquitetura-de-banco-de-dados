from db.connection import get_session
from db.models.employees import Employee

session = get_session()


def execute(employee_id):
    try:
        with session.begin():
            employee = session.query(Employee).where(Employee.id == employee_id).first()

            if employee is None:
                raise Exception("Employee not found.")

            session.delete(employee)

            session.commit()

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
