from use_cases import get_ticket_type_by_id

def handle():

    ticket_type_id = input("id: ")

    result = get_ticket_type_by_id.execute(ticket_type_id)

    print(result)