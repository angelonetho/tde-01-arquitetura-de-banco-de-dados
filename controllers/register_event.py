from datetime import datetime
from use_cases import register_event

def handle():

    name = input("Digite o name: ")
    description = input("Digite a description: ")
    avenue = input("Digite a avenue: ")
    event_time_str = input("Digite o event_time (formato: DD-MM-YYYY HH:MM:SS): ")
    
    try:
        event_time = datetime.strptime(event_time_str, "%d-%m-%Y %H:%M:%S")
    except ValueError:
        print("Formato de data e hora inválido.")
        return

    result = register_event.execute(name, description, avenue, event_time)

    print(result)