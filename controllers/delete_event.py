from use_cases import delete_event

def handle():

    event_id = input("id: ")

    result = delete_event.execute(event_id)

    print(result)