from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFormLayout,
    QMessageBox,
    QTextEdit,
)
from PyQt5.QtGui import QIcon
from datetime import datetime

from use_cases import get_ticket_by_id


class GetTicketByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Ingresso pelo ID")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_id_input = QLineEdit()
        self.ticket_id_input.setPlaceholderText("Digite o ID do ingresso")

        self.form_layout.addRow("ID do Ingresso:", self.ticket_id_input)

        layout.addLayout(self.form_layout)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText(
            "As informações do ingresso aparecerão aqui..."
        )
        layout.addWidget(self.result_display)

        self.search_button = QPushButton("Buscar Ingresso")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

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
            result = get_ticket_by_id.execute(ticket_id)
            if result:
                ticket_info = (
                    f"Ingresso encontrado:\n\n"
                    f"ID: {result.id}\n"
                    f"Data de Criação: {result.created_at.strftime('%d-%m-%Y %H:%M:%S')}\n"
                )

                if result.validated_at:
                    ticket_info += f"Data de Validação: {result.validated_at.strftime('%d-%m-%Y %H:%M:%S')}\n"
                else:
                    ticket_info += "Data de Validação: Não validado\n"

                ticket_info += (
                    f"ID do Tipo de Ingresso: {result.ticket_type_id}\n"
                    f"Tipo de Ingresso: {result.ticket_type.name if result.ticket_type else 'Desconhecido'}\n"
                    f"ID do Cliente: {result.customer_id}\n"
                    f"Nome do Cliente: {result.customer.name if result.customer else 'Desconhecido'}\n"
                )

                if result.employee:
                    ticket_info += (
                        f"Validado por (Funcionário): {result.employee.name}\n"
                    )
                else:
                    ticket_info += "Validado por (Funcionário): Não disponível\n"

                self.result_display.setPlainText(ticket_info)
            else:
                self.result_display.setPlainText("Ingresso não encontrado.")
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar ingresso: {str(e)}", QMessageBox.Critical
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
