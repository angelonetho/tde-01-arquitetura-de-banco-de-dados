from use_cases import delete_customer

def handle():

    customer_id = input("id: ")

    result = delete_customer.execute(customer_id)

    print(result)