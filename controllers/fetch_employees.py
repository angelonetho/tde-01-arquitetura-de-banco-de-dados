from use_cases import fetch_employees

def handle():

    result = fetch_employees.execute()

    print(result)