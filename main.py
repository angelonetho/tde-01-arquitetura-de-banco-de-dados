from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
)
from PyQt5.QtGui import QIcon

import sys

from controllers import (
    create_ticket,
    delete_customer,
    delete_employee,
    delete_event,
    delete_ticket,
    delete_ticket_type,
    edit_customer,
    edit_employee,
    edit_event,
    edit_ticket,
    edit_ticket_type,
    fetch_customers,
    fetch_employees,
    fetch_events,
    fetch_ticket_types_by_event_id,
    fetch_tickets_by_customer_id,
    fetch_tickets_by_ticket_type_id,
    get_customer_by_id,
    get_employee_by_id,
    get_event_by_id,
    get_ticket_by_id,
    get_ticket_type_by_id,
    register_customer,
    register_employee,
    register_event,
    register_ticket_type,
    validate_ticket,
)

from db.connection import create_tables

create_tables()

class CreateOperationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Haru Tickets 0.0.1 - Operações de Criação")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.btn_register_client = QPushButton("Registar Cliente")
        self.btn_register_employee = QPushButton("Registrar Funcionário")
        self.btn_register_event = QPushButton("Registrar Evento")
        self.btn_register_ticket_type = QPushButton("Registrar Tipo de Ingresso")
        self.btn_create_ticket = QPushButton("Emitir Ingresso")

        self.btn_register_client.clicked.connect(self.handle_register_client)
        self.btn_register_employee.clicked.connect(self.handle_register_employee)
        self.btn_register_event.clicked.connect(self.handle_register_event)
        self.btn_register_ticket_type.clicked.connect(self.handle_register_ticket_type)
        self.btn_create_ticket.clicked.connect(self.handle_create_ticket)

        layout.addWidget(self.btn_register_client)
        layout.addWidget(self.btn_register_employee)
        layout.addWidget(self.btn_register_event)
        layout.addWidget(self.btn_register_ticket_type)
        layout.addWidget(self.btn_create_ticket)

        self.setMinimumSize(64 * 8, 6 * 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_register_client(self):
        self.register_customer_window = register_customer.RegisterCustomerWindow()
        self.register_customer_window.show()

    def handle_register_employee(self):
        self.register_employee_window = register_employee.RegisterEmployeeWindow()
        self.register_employee_window.show()

    def handle_register_event(self):
        self.register_event_window = register_event.RegisterEventWindow()
        self.register_event_window.show()

    def handle_register_ticket_type(self):
        self.register_ticket_type_window = (
            register_ticket_type.RegisterTicketTypeWindow()
        )
        self.register_ticket_type_window.show()

    def handle_create_ticket(self):
        self.create_ticket_window = create_ticket.RegisterTicketWindow()
        self.create_ticket_window.show()


class ReadOperationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Haru Tickets 0.0.1 - Operações de Leitura")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.btn_get_customer_by_id = QPushButton("Obter Cliente por Id")
        self.btn_get_employee_by_id = QPushButton("Obter Funcionário por Id")
        self.btn_get_event_by_id = QPushButton("Obter Evento por Id")
        self.btn_get_ticket_by_id = QPushButton("Obter Ingresso por Id")
        self.btn_get_ticket_type_by_id = QPushButton("Obter Tipo de Ingresso por Id")
        self.btn_fetch_customers = QPushButton("Buscar todos os Clientes")
        self.btn_fetch_employees = QPushButton("Buscar todos os Funcionários")
        self.btn_fetch_events = QPushButton("Buscar todos os Eventos")
        self.btn_fetch_ticket_types_by_event_id = QPushButton(
            "Buscar Tipos de Ingresso por Evento"
        )
        self.btn_fetch_tickets_by_customer_id = QPushButton(
            "Buscar Ingressos por Cliente"
        )
        self.btn_fetch_tickets_by_ticket_type_id = QPushButton(
            "Buscar Ingressos por Tipo de Ingresso"
        )

        self.btn_get_customer_by_id.clicked.connect(self.handle_get_customer_by_id)
        self.btn_get_employee_by_id.clicked.connect(self.handle_get_employee_by_id)
        self.btn_get_event_by_id.clicked.connect(self.handle_get_event_by_id)
        self.btn_get_ticket_by_id.clicked.connect(self.handle_get_ticket_by_id)
        self.btn_get_ticket_type_by_id.clicked.connect(
            self.handle_get_ticket_type_by_id
        )
        self.btn_fetch_customers.clicked.connect(self.handle_fetch_customers)
        self.btn_fetch_employees.clicked.connect(self.handle_fetch_employees)
        self.btn_fetch_events.clicked.connect(self.handle_fetch_events)
        self.btn_fetch_ticket_types_by_event_id.clicked.connect(
            self.handle_fetch_ticket_types_by_event_id
        )
        self.btn_fetch_tickets_by_customer_id.clicked.connect(
            self.handle_fetch_tickets_by_customer_id
        )
        self.btn_fetch_tickets_by_ticket_type_id.clicked.connect(
            self.handle_fetch_tickets_by_ticket_type_id
        )

        layout.addWidget(self.btn_get_customer_by_id)
        layout.addWidget(self.btn_get_employee_by_id)
        layout.addWidget(self.btn_get_event_by_id)
        layout.addWidget(self.btn_get_ticket_by_id)
        layout.addWidget(self.btn_get_ticket_type_by_id)
        layout.addWidget(self.btn_fetch_customers)
        layout.addWidget(self.btn_fetch_employees)
        layout.addWidget(self.btn_fetch_events)
        layout.addWidget(self.btn_fetch_ticket_types_by_event_id)
        layout.addWidget(self.btn_fetch_tickets_by_customer_id)
        layout.addWidget(self.btn_fetch_tickets_by_ticket_type_id)

        self.setMinimumSize(64 * 8, 6 * 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_get_customer_by_id(self):
        self.new_window = get_customer_by_id.GetCustomerByIdWindow()
        self.new_window.show()

    def handle_get_employee_by_id(self):
        self.new_window = get_employee_by_id.GetEmployeeByIdWindow()
        self.new_window.show()

    def handle_get_event_by_id(self):
        self.new_window = get_event_by_id.GetEventByIdWindow()
        self.new_window.show()

    def handle_get_ticket_by_id(self):
        self.new_window = get_ticket_by_id.GetTicketByIdWindow()
        self.new_window.show()

    def handle_get_ticket_type_by_id(self):
        self.new_window = get_ticket_type_by_id.GetTicketTypeByIdWindow()
        self.new_window.show()

    def handle_fetch_customers(self):
        self.new_window = fetch_customers.FetchCustomersWindow()
        self.new_window.show()

    def handle_fetch_employees(self):
        self.new_window = fetch_employees.FetchEmployeesWindow()
        self.new_window.show()

    def handle_fetch_events(self):
        self.new_window = fetch_events.FetchEventsWindow()
        self.new_window.show()

    def handle_fetch_ticket_types_by_event_id(self):
        self.new_window = (
            fetch_ticket_types_by_event_id.FetchTicketTypesByEventIdWindow()
        )
        self.new_window.show()

    def handle_fetch_tickets_by_customer_id(self):
        self.new_window = fetch_tickets_by_customer_id.FetchTicketsByCustomerIdWindow()
        self.new_window.show()

    def handle_fetch_tickets_by_ticket_type_id(self):
        self.new_window = (
            fetch_tickets_by_ticket_type_id.FetchTicketsByTicketTypeIdWindow()
        )
        self.new_window.show()


class UpdateOperationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Haru Tickets 0.0.1 - Operações de Atualização")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.btn_update_customer = QPushButton("Atualizar Cliente")
        self.btn_update_employee = QPushButton("Atualizar Funcionário")
        self.btn_update_event = QPushButton("Atualizar Evento")
        self.btn_update_ticket_type = QPushButton("Atualizar Tipo de Ingresso")
        self.btn_update_ticket = QPushButton("Atualizar Ingresso")
        self.btn_validate_ticket = QPushButton("Validar Ingresso")

        self.btn_update_customer.clicked.connect(self.handle_update_customer)
        self.btn_update_employee.clicked.connect(self.handle_update_employee)
        self.btn_update_event.clicked.connect(self.handle_update_event)
        self.btn_update_ticket_type.clicked.connect(self.handle_update_ticket_type)
        self.btn_update_ticket.clicked.connect(self.handle_update_ticket)
        self.btn_validate_ticket.clicked.connect(self.handle_validate_ticket)

        layout.addWidget(self.btn_update_customer)
        layout.addWidget(self.btn_update_employee)
        layout.addWidget(self.btn_update_event)
        layout.addWidget(self.btn_update_ticket_type)
        layout.addWidget(self.btn_update_ticket)
        layout.addWidget(self.btn_validate_ticket)

        self.setMinimumSize(64 * 8, 6 * 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_update_customer(self):
        self.new_window = edit_customer.EditCustomerWindow()
        self.new_window.show()

    def handle_update_employee(self):
        self.new_window = edit_employee.EditEmployeeWindow()
        self.new_window.show()

    def handle_update_event(self):
        self.new_window = edit_event.EditEventWindow()
        self.new_window.show()

    def handle_update_ticket_type(self):
        self.new_window = edit_ticket_type.EditTicketTypeWindow()
        self.new_window.show()

    def handle_update_ticket(self):
        self.new_window = edit_ticket.EditTicketWindow()
        self.new_window.show()

    def handle_validate_ticket(self):
        self.new_window = validate_ticket.ValidateTicketWindow()
        self.new_window.show()


class DeleteOperationsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Haru Tickets 0.0.1 - Operações de Exclusão")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.btn_delete_customer = QPushButton("Excluir Cliente")
        self.btn_delete_employee = QPushButton("Excluir Funcionário")
        self.btn_delete_event = QPushButton("Excluir Evento")
        self.btn_delete_ticket_type = QPushButton("Excluir Tipo de Ingresso")
        self.btn_delete_ticket = QPushButton("Excluir Ingresso")

        self.btn_delete_customer.clicked.connect(self.handle_delete_customer)
        self.btn_delete_employee.clicked.connect(self.handle_delete_employee)
        self.btn_delete_event.clicked.connect(self.handle_delete_event)
        self.btn_delete_ticket_type.clicked.connect(self.handle_delete_ticket_type)
        self.btn_delete_ticket.clicked.connect(self.handle_delete_ticket)

        layout.addWidget(self.btn_delete_customer)
        layout.addWidget(self.btn_delete_employee)
        layout.addWidget(self.btn_delete_event)
        layout.addWidget(self.btn_delete_ticket_type)
        layout.addWidget(self.btn_delete_ticket)

        self.setMinimumSize(64 * 8, 6 * 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_delete_customer(self):
        self.new_window = delete_customer.DeleteCustomerWindow()
        self.new_window.show()

    def handle_delete_employee(self):
        self.new_window = delete_employee.DeleteEmployeeWindow()
        self.new_window.show()

    def handle_delete_event(self):
        self.new_window = delete_event.DeleteEventWindow()
        self.new_window.show()

    def handle_delete_ticket_type(self):
        self.new_window = delete_ticket_type.DeleteTicketTypeWindow()
        self.new_window.show()

    def handle_delete_ticket(self):
        self.new_window = delete_ticket.DeleteTicketWindow()
        self.new_window.show()


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Haru Tickets 0.0.1")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.btn_create = QPushButton("Operações de Criação")
        self.btn_read = QPushButton("Operações de Leitura")
        self.btn_update = QPushButton("Operações de Atualização")
        self.btn_delete = QPushButton("Operações de Exclusão")

        self.btn_create.clicked.connect(self.handle_create)
        self.btn_read.clicked.connect(self.handle_read)
        self.btn_update.clicked.connect(self.handle_update)
        self.btn_delete.clicked.connect(self.handle_delete)

        layout.addWidget(self.btn_create)
        layout.addWidget(self.btn_read)
        layout.addWidget(self.btn_update)
        layout.addWidget(self.btn_delete)

        self.setMinimumSize(64 * 8, 6 * 8)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle_create(self):
        self.create_operations_window = CreateOperationsWindow()
        self.create_operations_window.show()

    def handle_read(self):
        self.read_operations_window = ReadOperationsWindow()
        self.read_operations_window.show()

    def handle_update(self):
        self.update_operations_window = UpdateOperationsWindow()
        self.update_operations_window.show()

    def handle_delete(self):
        self.delete_operations_window = DeleteOperationsWindow()
        self.delete_operations_window.show()


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec()
