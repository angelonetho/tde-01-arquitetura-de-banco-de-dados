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

from use_cases import register_ticket_type


class RegisterTicketTypeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Tipo de Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.description_input = QLineEdit()
        self.price_input = QLineEdit()
        self.event_id_input = QLineEdit()

        self.name_input.setPlaceholderText("Digite o nome do tipo de ingresso")
        self.description_input.setPlaceholderText("Digite a descrição")
        self.price_input.setPlaceholderText("Digite o preço (somente números)")
        self.event_id_input.setPlaceholderText("Digite o ID do evento")

        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("Descrição:", self.description_input)
        self.form_layout.addRow("Preço:", self.price_input)
        self.form_layout.addRow("ID do Evento:", self.event_id_input)

        layout.addLayout(self.form_layout)

        self.register_button = QPushButton("Registrar Tipo de Ingresso")
        self.register_button.clicked.connect(self.handle)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        name = self.name_input.text()
        description = self.description_input.text()
        price = self.price_input.text()
        event_id = self.event_id_input.text()

        if not name or not description or not price or not event_id:
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
            result = register_ticket_type.execute(name, description, price, event_id)
        except Exception as e:
            self.show_message(
                "Erro",
                f"Erro ao registrar tipo de ingresso: {str(e)}",
                QMessageBox.Critical,
            )
            return

        self.show_message(
            "Sucesso",
            f"Tipo de ingresso registrado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
