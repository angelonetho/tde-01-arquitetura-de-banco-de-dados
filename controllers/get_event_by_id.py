from use_cases import get_event_by_id

def handle():

    event_id = input("id: ")

    result = get_event_by_id.execute(event_id)

    print(result)