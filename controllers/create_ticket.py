from use_cases import create_ticket

def handle():

    ticket_type_id = input("Digite o ticket_type_id: ")
    customer_id = input("Digite o customer_id? ")

    result = create_ticket.execute(ticket_type_id, customer_id)

    print(result)