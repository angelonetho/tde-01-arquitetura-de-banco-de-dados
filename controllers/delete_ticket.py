from use_cases import delete_ticket

def handle():

    ticket_id = input("id: ")

    result = delete_ticket.execute(ticket_id)

    print(result)