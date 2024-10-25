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

from use_cases import edit_customer


class EditCustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editar Cliente")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.customer_id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.email_input = QLineEdit()
        self.phone_number_input = QLineEdit()
        self.birth_date_input = QLineEdit()

        self.customer_id_input.setPlaceholderText("Digite o ID do cliente")
        self.name_input.setPlaceholderText("Digite o nome do cliente")
        self.email_input.setPlaceholderText("Digite o e-mail do cliente")
        self.phone_number_input.setPlaceholderText("Digite o número de telefone")
        self.birth_date_input.setPlaceholderText("DD-MM-YYYY")

        self.form_layout.addRow("ID do Cliente:", self.customer_id_input)
        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("E-mail:", self.email_input)
        self.form_layout.addRow("Telefone:", self.phone_number_input)
        self.form_layout.addRow("Data de Nascimento:", self.birth_date_input)

        layout.addLayout(self.form_layout)

        self.edit_button = QPushButton("Editar Cliente")
        self.edit_button.clicked.connect(self.handle)
        layout.addWidget(self.edit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        customer_id = self.customer_id_input.text()
        name = self.name_input.text()
        email = self.email_input.text()
        phone_number = self.phone_number_input.text()
        birth_date_str = self.birth_date_input.text()

        if (
            not customer_id
            or not name
            or not email
            or not phone_number
            or not birth_date_str
        ):
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
            result = edit_customer.execute(
                customer_id, name, email, phone_number, birth_date
            )
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao editar cliente: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Cliente atualizado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
