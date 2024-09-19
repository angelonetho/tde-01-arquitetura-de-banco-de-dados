from use_cases import delete_employee

def handle():

    employee_id = input("id: ")

    result = delete_employee.execute(employee_id)

    print(result)