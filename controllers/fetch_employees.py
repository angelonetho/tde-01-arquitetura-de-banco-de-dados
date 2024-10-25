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

from use_cases import fetch_employees


class FetchEmployeesWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Todos os Funcionários")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.employee_table = QTableWidget()
        self.employee_table.setColumnCount(3)
        self.employee_table.setHorizontalHeaderLabels(["ID", "Nome", "CPF"])
        layout.addWidget(self.employee_table)

        self.fetch_button = QPushButton("Buscar Funcionários")
        self.fetch_button.clicked.connect(self.handle)
        layout.addWidget(self.fetch_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):

        try:
            employees = fetch_employees.execute()
            if employees:
                self.populate_table(employees)
            else:
                self.employee_table.setRowCount(0)
                self.show_message(
                    "Aviso", "Nenhum funcionário encontrado.", QMessageBox.Information
                )
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar funcionários: {str(e)}", QMessageBox.Critical
            )

    def populate_table(self, employees):

        self.employee_table.setRowCount(len(employees))

        for row, employee in enumerate(employees):

            self.employee_table.setItem(row, 0, QTableWidgetItem(employee.id))
            self.employee_table.setItem(row, 1, QTableWidgetItem(employee.name))
            self.employee_table.setItem(row, 2, QTableWidgetItem(employee.cpf))

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
