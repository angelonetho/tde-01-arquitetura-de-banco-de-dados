from use_cases import delete_ticket_type
def handle():

    ticket_type_id = input("id: ")

    result = delete_ticket_type.execute(ticket_type_id)

    print(result)