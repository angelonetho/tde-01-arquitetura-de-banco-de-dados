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

from use_cases import delete_ticket


class DeleteTicketWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excluir Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_id_input = QLineEdit()
        self.ticket_id_input.setPlaceholderText("Digite o ID do ingresso")

        self.form_layout.addRow("ID do Ingresso:", self.ticket_id_input)

        layout.addLayout(self.form_layout)

        self.delete_button = QPushButton("Excluir Ingresso")
        self.delete_button.clicked.connect(self.handle)
        layout.addWidget(self.delete_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_id = self.ticket_id_input.text()

        if not ticket_id:
            self.show_message(
                "Erro", "O campo ID do ingresso é obrigatório.", QMessageBox.Warning
            )
            return

        try:
            result = delete_ticket.execute(ticket_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao excluir ingresso: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso", "Ingresso excluído com sucesso.", QMessageBox.Information
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
