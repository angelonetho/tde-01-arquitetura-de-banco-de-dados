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

from use_cases import create_ticket


class RegisterTicketWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_type_id_input = QLineEdit()
        self.customer_id_input = QLineEdit()

        self.ticket_type_id_input.setPlaceholderText("Digite o ID do tipo de ingresso")
        self.customer_id_input.setPlaceholderText("Digite o ID do cliente")

        self.form_layout.addRow("ID do Tipo de Ingresso:", self.ticket_type_id_input)
        self.form_layout.addRow("ID do Cliente:", self.customer_id_input)

        layout.addLayout(self.form_layout)

        self.register_button = QPushButton("Registrar Ingresso")
        self.register_button.clicked.connect(self.handle)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_type_id = self.ticket_type_id_input.text()
        customer_id = self.customer_id_input.text()

        if not ticket_type_id or not customer_id:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            result = create_ticket.execute(ticket_type_id, customer_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao registrar ingresso: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Ingresso registrado com sucesso: {result}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
