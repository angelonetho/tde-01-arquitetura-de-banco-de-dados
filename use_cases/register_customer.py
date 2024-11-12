from db.connection import get_session
from db.models.customers import Customer

session = get_session()


def execute(name, cpf, email, password, birth_date):
    try:
        with session.begin():
            customer = (
                session.query(Customer)
                .where((Customer.cpf == cpf) | (Customer.email == email))
                .first()
            )

            if customer:
                raise Exception("Customer with same e-mail or CPF already exists.")

            new_customer = Customer(
                name=name,
                cpf=cpf,
                email=email,
                password=password,
                birth_date=birth_date,
            )
            session.add(new_customer)

            session.commit()

        return new_customer

    except Exception as exception:
        session.rollback()
        raise exception

    finally:
        session.close()
