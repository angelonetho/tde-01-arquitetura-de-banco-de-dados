from use_cases import fetch_events

def handle():

    result = fetch_events.execute()

    print(result)