from use_cases import edit_ticket

def handle():

    ticket_id = input("ticket__id: ")
    ticket_type_id = input("ticket_type_id: ")

    result = edit_ticket.execute(ticket_id, ticket_type_id)

    print(result)