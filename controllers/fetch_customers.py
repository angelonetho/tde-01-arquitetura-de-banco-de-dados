from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt5.QtGui import QIcon

from use_cases import fetch_customers


class FetchCustomersWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Todos os Clientes")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.customer_table = QTableWidget()
        self.customer_table.setColumnCount(4)
        self.customer_table.setHorizontalHeaderLabels(
            ["ID", "Nome", "Email", "Data de Nascimento"]
        )
        layout.addWidget(self.customer_table)

        self.fetch_button = QPushButton("Buscar Clientes")
        self.fetch_button.clicked.connect(self.handle)
        layout.addWidget(self.fetch_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):

        try:
            customers = fetch_customers.execute()
            if customers:
                self.populate_table(customers)
            else:
                self.customer_table.setRowCount(0)
                self.show_message(
                    "Aviso", "Nenhum cliente encontrado.", QMessageBox.Information
                )
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar clientes: {str(e)}", QMessageBox.Critical
            )

    def populate_table(self, customers):

        self.customer_table.setRowCount(len(customers))

        for row, customer in enumerate(customers):

            self.customer_table.setItem(row, 0, QTableWidgetItem(customer.id))
            self.customer_table.setItem(row, 1, QTableWidgetItem(customer.name))
            self.customer_table.setItem(row, 2, QTableWidgetItem(customer.email))
            self.customer_table.setItem(
                row, 3, QTableWidgetItem(customer.birth_date.strftime("%d-%m-%Y"))
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
