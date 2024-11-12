from db.connection import get_session
from db.models.employees import Employee

session = get_session()


def execute(name, cpf):
    try:
        with session.begin():
            employee = session.query(Employee).where(Employee.cpf == cpf).first()

            if employee:
                raise Exception("Employee with same CPF already exists.")

            new_employee = Employee(name=name, cpf=cpf)
            session.add(new_employee)

            session.commit()

        return new_employee

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
