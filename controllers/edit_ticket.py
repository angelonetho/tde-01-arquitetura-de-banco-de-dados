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

from use_cases import edit_ticket


class EditTicketWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editar Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_id_input = QLineEdit()
        self.ticket_type_id_input = QLineEdit()

        self.ticket_id_input.setPlaceholderText("Digite o ID do ingresso")
        self.ticket_type_id_input.setPlaceholderText("Digite o ID do tipo de ingresso")

        self.form_layout.addRow("ID do Ingresso:", self.ticket_id_input)
        self.form_layout.addRow("ID do Tipo de Ingresso:", self.ticket_type_id_input)

        layout.addLayout(self.form_layout)

        self.edit_button = QPushButton("Editar Ingresso")
        self.edit_button.clicked.connect(self.handle)
        layout.addWidget(self.edit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_id = self.ticket_id_input.text()
        ticket_type_id = self.ticket_type_id_input.text()

        if not ticket_id or not ticket_type_id:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            result = edit_ticket.execute(ticket_id, ticket_type_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao editar ingresso: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Ingresso atualizado com sucesso: {result}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
