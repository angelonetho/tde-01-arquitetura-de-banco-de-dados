from use_cases import get_employee_by_id

def handle():

    employee_id = input("id: ")

    result = get_employee_by_id.execute(employee_id)

    print(result)