from use_cases import register_employee

def handle():

    name = input("name: ")
    cpf = input("cpf: ")
    
    result = register_employee.execute(name, cpf)

    print(result)