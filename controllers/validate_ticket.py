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

from use_cases import validate_ticket


class ValidateTicketWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Validar Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_id_input = QLineEdit()
        self.employee_id_input = QLineEdit()

        self.ticket_id_input.setPlaceholderText("Digite o ID do ingresso")
        self.employee_id_input.setPlaceholderText("Digite o ID do funcionário")

        self.form_layout.addRow("ID do Ingresso:", self.ticket_id_input)
        self.form_layout.addRow("ID do Funcionário:", self.employee_id_input)

        layout.addLayout(self.form_layout)

        self.validate_button = QPushButton("Validar Ingresso")
        self.validate_button.clicked.connect(self.handle)
        layout.addWidget(self.validate_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_id = self.ticket_id_input.text()
        employee_id = self.employee_id_input.text()

        if not ticket_id or not employee_id:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            result = validate_ticket.execute(ticket_id, employee_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao validar ingresso: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Ingresso validado com sucesso: {result}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
