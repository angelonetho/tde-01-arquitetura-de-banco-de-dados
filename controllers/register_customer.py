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
from datetime import datetime

from use_cases import register_customer


class RegisterCustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Cliente")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.cpf_input = QLineEdit()
        self.email_input = QLineEdit()
        self.password_input = QLineEdit()
        self.birth_date_input = QLineEdit()

        self.name_input.setPlaceholderText("Digite o nome do cliente")
        self.cpf_input.setPlaceholderText("Digite o CPF (somente números)")
        self.email_input.setPlaceholderText("Digite o e-mail")
        self.password_input.setPlaceholderText("Digite a senha")
        self.birth_date_input.setPlaceholderText("DD-MM-YYYY")

        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("CPF:", self.cpf_input)
        self.form_layout.addRow("Email:", self.email_input)
        self.form_layout.addRow("Senha:", self.password_input)
        self.form_layout.addRow("Data de Nascimento:", self.birth_date_input)

        layout.addLayout(self.form_layout)

        self.register_button = QPushButton("Registrar Cliente")
        self.register_button.clicked.connect(self.handle)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        name = self.name_input.text()
        cpf = self.cpf_input.text()
        email = self.email_input.text()
        password = self.password_input.text()
        birth_date_str = self.birth_date_input.text()

        if not name or not cpf or not email or not password or not birth_date_str:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            birth_date = datetime.strptime(birth_date_str, "%d-%m-%Y")
        except ValueError:
            self.show_message(
                "Erro", "Formato de data inválido. Use DD-MM-YYYY.", QMessageBox.Warning
            )
            return

        try:
            result = register_customer.execute(name, cpf, email, password, birth_date)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao registrar cliente: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message("Sucesso", str(result), QMessageBox.Information)

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
