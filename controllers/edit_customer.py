from datetime import datetime
from use_cases import edit_customer

def handle():

    customer_id = input("customer_id: ")
    name = input("name: ")
    email = input("email: ")
    phone_number = input("phone_number: ")
    birth_date_str = input("birth_date (formato: DD-MM-YYYY): ")

    try:
        birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
    except ValueError:
        print("Formato de data inválido.")
        return

    result = edit_customer.execute(customer_id, name, email, phone_number, birth_date)

    print(result)