from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFormLayout,
    QMessageBox,
)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal

from use_cases import authenticate_employee


class AuthenticateEmployeeWindow(QMainWindow):
    login_success = pyqtSignal(object)

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Login de Funcionário")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.employee_id_input = QLineEdit()
        self.employee_id_input.setPlaceholderText("Digite o ID do funcionário")

        self.cpf_input = QLineEdit()
        self.cpf_input.setPlaceholderText("Digite o CPF do funcionário")

        self.form_layout.addRow("ID do Funcionário:", self.employee_id_input)
        self.form_layout.addRow("CPF do Funcionário:", self.cpf_input)

        layout.addLayout(self.form_layout)

        self.login_button = QPushButton("Login")
        self.login_button.clicked.connect(self.handle)
        layout.addWidget(self.login_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        employee_id = self.employee_id_input.text().strip()
        cpf = self.cpf_input.text().strip()

        if not employee_id or not cpf:
            self.show_message(
                "Erro", "ID e CPF do funcionário são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            employee = authenticate_employee.execute(employee_id, cpf)
            if employee:
                self.show_message(
                    "Sucesso",
                    f"Funcionário {employee.name} autenticado com sucesso!",
                    QMessageBox.Information,
                )
                self.login_success.emit(
                    employee
                )  # Emite o sinal com as informações do funcionário
                self.close()  # Fecha a janela de login
            else:
                self.show_message(
                    "Erro",
                    "Funcionário não encontrado ou credenciais inválidas.",
                    QMessageBox.Warning,
                )
        except Exception as e:
            self.show_message(
                "Erro",
                f"Erro ao autenticar funcionário: {str(e)}",
                QMessageBox.Critical,
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
