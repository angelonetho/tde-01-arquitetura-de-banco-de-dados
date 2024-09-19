import time
from controllers import create_ticket, delete_customer, delete_employee, delete_event, delete_ticket, delete_ticket_type, edit_customer, edit_employee, edit_event, edit_ticket, edit_ticket_type, fetch_customers, fetch_employees, fetch_events, fetch_ticket_types_by_event_id, fetch_tickets_by_customer_id, fetch_tickets_by_ticket_type_id, get_customer_by_id, get_employee_by_id, get_event_by_id, get_ticket_by_id, get_ticket_type_by_id, register_customer, register_employee, register_event, register_ticket_type, validate_ticket
from db.connection import create_tables
from db.models.customers import Customer
from db.models.employees import Employee
from db.models.events import Event
from db.models.ticket_types import TicketType
from db.models.tickets import Ticket

create_tables()

operation_type_message = "\n[HaruOS]: Escolha um tipo de operação: "

operation_type = -1
sub_operation_type = -1

def print_header():
    print("""
        _    _               _______ _      _        _       
        | |  | |             |__   __(_)    | |      | |      
        | |__| | __ _ _ __ _   _| |   _  ___| | _____| |_ ___ 
        |  __  |/ _` | '__| | | | |  | |/ __| |/ / _ \ __/ __|
        | |  | | (_| | |  | |_| | |  | | (__|   <  __/ |_\__ \\
        |_|  |_|\__,_|_|   \__,_|_|  |_|\___|_|\_\___|\__|___/
                                                            
                                                            """)

    print(" 1 - Operações de Criação")
    print(" 2 - Operações de Leitura")
    print(" 3 - Operações de Atualização")
    print(" 4 - Operações de Exclusão")
    print(" 0 - Sair")

def print_create_options():
    print("\n Operações de Criação:")
    print("  1 - Registrar Cliente")
    print("  2 - Registrar Funcionário")
    print("  3 - Registrar Evento")
    print("  4 - Registrar Tipo de Ingresso")
    print("  5 - Criar Ingresso")
    
def print_read_options():
    print("\n Operações de Leitura:")
    print("  1 - Obter Cliente por Id")
    print("  2 - Obter Funcionário por Id")
    print("  3 - Obter Evento por Id")
    print("  4 - Obter Ingresso por Id")
    print("  5 - Obter Tipo de Ingresso por Id")
    print("  6 - Buscar todos os Clientes")
    print("  7 - Buscar todos os Funcionários")
    print("  8 - Buscar todos os Eventos")
    print("  9 - Buscar todos os Tipos de Ingresso pelo Id do Evento")
    print("  10 - Buscar todos os Ingressos pelo Id do Cliente")
    print("  11 - Buscar todos os Ingressos pelo Id do Tipo de Ingresso")

def print_edit_options():
    print("\n Operações de Atualização:")
    print("  1 - Atualizar Cliente")
    print("  2 - Atualizar Funcionário")
    print("  3 - Atualizar Evento")
    print("  4 - Atualizar Tipo de Ingresso")
    print("  5 - Atualizar Ingresso")
    print("  6 - Validar Ingresso")

def print_delete_options():
    print("  1 - Excluir Cliente")
    print("  2 - Excluir Funcionário")
    print("  3 - Excluir Evento")
    print("  4 - Excluir Tipo de Ingresso")
    print("  5 - Excluir Ingresso")

while operation_type != 0 and sub_operation_type != 0:

    print_header()
    operation_type = int(input(operation_type_message))

    if operation_type == 1:
        print_create_options()
        sub_operation_type = int(input(operation_type_message))

        if sub_operation_type == 1: register_customer.handle()
        if sub_operation_type == 2: register_employee.handle()
        if sub_operation_type == 3: register_event.handle()
        if sub_operation_type == 4: register_ticket_type.handle()
        if sub_operation_type == 5: create_ticket.handle()

    elif operation_type == 2:
        print_read_options()
        sub_operation_type = int(input(operation_type_message))

        if sub_operation_type == 1: get_customer_by_id.handle()
        if sub_operation_type == 2: get_employee_by_id.handle()
        if sub_operation_type == 3: get_event_by_id.handle()
        if sub_operation_type == 4: get_ticket_by_id.handle()
        if sub_operation_type == 5: get_ticket_type_by_id.handle()
        if sub_operation_type == 6: fetch_customers.handle()
        if sub_operation_type == 7: fetch_employees.handle()
        if sub_operation_type == 8: fetch_events.handle()
        if sub_operation_type == 9: fetch_ticket_types_by_event_id.handle()
        if sub_operation_type == 10: fetch_tickets_by_customer_id.handle()
        if sub_operation_type == 11: fetch_tickets_by_ticket_type_id.handle()

    elif operation_type == 3:
        print_edit_options()
        sub_operation_type = int(input(operation_type_message))

        if sub_operation_type == 1: edit_customer.handle()
        if sub_operation_type == 2: edit_employee.handle()
        if sub_operation_type == 3: edit_event.handle()
        if sub_operation_type == 4: edit_ticket_type.handle()
        if sub_operation_type == 5: edit_ticket.handle()
        if sub_operation_type == 6: validate_ticket.handle()

    elif operation_type == 4:
        print_delete_options()
        sub_operation_type = int(input(operation_type_message))

        if sub_operation_type == 1: delete_customer.handle()
        if sub_operation_type == 2: delete_employee.handle()
        if sub_operation_type == 3: delete_event.handle()
        if sub_operation_type == 4: delete_ticket_type.handle()
        if sub_operation_type == 5: delete_ticket.handle()
    
    time.sleep(2)
    print(sub_operation_type)
