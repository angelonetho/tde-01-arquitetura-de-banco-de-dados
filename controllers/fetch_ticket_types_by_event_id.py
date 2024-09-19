from use_cases import fetch_ticket_types_by_event_id

def handle():

    event_id = input("id: ")

    result = fetch_ticket_types_by_event_id.execute(event_id)

    print(result)