from datetime import datetime
from use_cases import register_ticket_type

def handle():

    name = input("name: ")
    description = input("description: ")
    price = input("price: ")
    event_id = input("event_id:")

    result = register_ticket_type.execute(name, description, price, event_id)

    print(result)