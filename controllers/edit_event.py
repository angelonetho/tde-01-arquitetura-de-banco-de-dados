from datetime import datetime
from use_cases import edit_event

def handle():

    event_id = input("id: ")
    name = input("name: ")
    description = input("description: ")
    avenue = input("avenue: ")
    event_time_str = input("Digite o event_time (formato: DD-MM-YYYY HH:MM:SS): ")
    
    try:
        event_time = datetime.strptime(event_time_str, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        print("Formato de data e hora inválido.")
        return

    result = edit_event.execute(event_id, name, description, avenue, event_time)

    print(result)