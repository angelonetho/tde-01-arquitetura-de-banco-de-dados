from use_cases import get_customer_by_id

def handle():

    customer_id = input("id: ")

    result = get_customer_by_id.execute(customer_id)

    print(result)