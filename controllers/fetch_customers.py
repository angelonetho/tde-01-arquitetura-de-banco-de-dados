from use_cases import fetch_customers

def handle():

    result = fetch_customers.execute()

    print(result)