from use_cases import edit_employee

def handle():

    employee_id = input("id: ")
    name = input("name: ")

    result = edit_employee.execute(employee_id, name)

    print(result)