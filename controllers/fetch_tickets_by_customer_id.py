from use_cases import fetch_tickets_by_customer_id

def handle():

    customer_id = input("id: ")

    result = fetch_tickets_by_customer_id.execute(customer_id)

    print(result)