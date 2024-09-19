from use_cases import edit_ticket_type

def handle():

    ticket_type_id = input("id: ")
    name = input("name: ")
    description = input("description: ")
    price = input("price: ")

    result = edit_ticket_type.execute(ticket_type_id, name, description, price)

    print(result)