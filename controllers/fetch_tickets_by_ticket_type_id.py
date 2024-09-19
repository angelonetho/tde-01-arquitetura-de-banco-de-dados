from use_cases import fetch_tickets_by_ticket_type_id

def handle():

    ticket_type_id = input("id: ")

    result = fetch_tickets_by_ticket_type_id.execute(ticket_type_id)

    print(result)