from use_cases import validate_ticket

def handle():

    ticket_id = input("id: ")
    employee_id = input("id: ")

    result = validate_ticket.execute(ticket_id, employee_id)

    print(result)