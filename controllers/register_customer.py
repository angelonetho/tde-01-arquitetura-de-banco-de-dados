from datetime import datetime
from use_cases import register_customer

def handle():

    name = input("name: ")
    cpf = input("cpf: ")
    email = input("email: ")
    password = input("password: ")
    birth_date_str = input("birth_date (formato: DD-MM-YYYY): ")

    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    except ValueError:
        print("Formato de data inválido.")
        return

    
    result = register_customer.execute(name, cpf, email, password, birth_date)

    print(result)