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

from use_cases import edit_ticket_type


class EditTicketTypeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editar Tipo de Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_type_id_input = QLineEdit()
        self.name_input = QLineEdit()
        self.description_input = QLineEdit()
        self.price_input = QLineEdit()

        self.ticket_type_id_input.setPlaceholderText("Digite o ID do tipo de ingresso")
        self.name_input.setPlaceholderText("Digite o nome do tipo de ingresso")
        self.description_input.setPlaceholderText("Digite a descrição")
        self.price_input.setPlaceholderText("Digite o preço (somente números)")

        self.form_layout.addRow("ID do Tipo de Ingresso:", self.ticket_type_id_input)
        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("Descrição:", self.description_input)
        self.form_layout.addRow("Preço:", self.price_input)

        layout.addLayout(self.form_layout)

        self.edit_button = QPushButton("Editar Tipo de Ingresso")
        self.edit_button.clicked.connect(self.handle)
        layout.addWidget(self.edit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_type_id = self.ticket_type_id_input.text()
        name = self.name_input.text()
        description = self.description_input.text()
        price = self.price_input.text()

        if not ticket_type_id or not name or not description or not price:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            price = float(price)
        except ValueError:
            self.show_message(
                "Erro", "O preço deve ser um número válido.", QMessageBox.Warning
            )
            return

        try:
            result = edit_ticket_type.execute(ticket_type_id, name, description, price)
        except Exception as e:
            self.show_message(
                "Erro",
                f"Erro ao editar tipo de ingresso: {str(e)}",
                QMessageBox.Critical,
            )
            return

        self.show_message(
            "Sucesso",
            f"Tipo de ingresso atualizado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
