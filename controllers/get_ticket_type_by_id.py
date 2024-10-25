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

from use_cases import get_ticket_type_by_id


class GetTicketTypeByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Tipo de Ingresso pelo ID")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_type_id_input = QLineEdit()
        self.ticket_type_id_input.setPlaceholderText("Digite o ID do tipo de ingresso")

        self.form_layout.addRow("ID do Tipo de Ingresso:", self.ticket_type_id_input)

        layout.addLayout(self.form_layout)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText(
            "As informações do tipo de ingresso aparecerão aqui..."
        )
        layout.addWidget(self.result_display)

        self.search_button = QPushButton("Buscar Tipo de Ingresso")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        ticket_type_id = self.ticket_type_id_input.text()

        if not ticket_type_id:
            self.show_message(
                "Erro",
                "O campo ID do tipo de ingresso é obrigatório.",
                QMessageBox.Warning,
            )
            return

        try:
            result = get_ticket_type_by_id.execute(ticket_type_id)
            if result:
                self.result_display.setPlainText(
                    f"Tipo de Ingresso encontrado:\n\n"
                    f"ID: {result.id}\n"
                    f"Nome: {result.name}\n"
                    f"Descrição: {result.description}\n"
                    f"Preço: R${result.price:.2f}\n"
                    f"Evento Associado: {result.event.name if result.event else 'Desconhecido'}"
                )
            else:
                self.result_display.setPlainText("Tipo de ingresso não encontrado.")
        except Exception as e:
            self.show_message(
                "Erro",
                f"Erro ao buscar tipo de ingresso: {str(e)}",
                QMessageBox.Critical,
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
