from use_cases import get_ticket_by_id

def handle():

    ticket_id = input("id: ")

    result = get_ticket_by_id.execute(ticket_id)

    print(result)