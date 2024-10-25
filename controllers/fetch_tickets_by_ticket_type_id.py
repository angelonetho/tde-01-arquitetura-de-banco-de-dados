from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFormLayout,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
)
from PyQt5.QtGui import QIcon

from use_cases import fetch_tickets_by_ticket_type_id


class FetchTicketsByTicketTypeIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Ingressos pelo ID do Tipo de Ingresso")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.ticket_type_id_input = QLineEdit()
        self.ticket_type_id_input.setPlaceholderText("Digite o ID do tipo de ingresso")

        self.form_layout.addRow("ID do Tipo de Ingresso:", self.ticket_type_id_input)

        layout.addLayout(self.form_layout)

        self.ticket_table = QTableWidget()
        self.ticket_table.setColumnCount(6)
        self.ticket_table.setHorizontalHeaderLabels(
            [
                "ID Ingresso",
                "Data Criação",
                "Data Validação",
                "Tipo de Ingresso",
                "Nome do Cliente",
                "Funcionário Validador",
            ]
        )
        layout.addWidget(self.ticket_table)

        self.search_button = QPushButton("Buscar Ingressos")
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
            tickets = fetch_tickets_by_ticket_type_id.execute(ticket_type_id)
            if tickets:
                self.populate_table(tickets)
            else:
                self.ticket_table.setRowCount(0)
                self.show_message(
                    "Aviso",
                    "Nenhum ingresso encontrado para este tipo de ingresso.",
                    QMessageBox.Information,
                )
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar ingressos: {str(e)}", QMessageBox.Critical
            )

    def populate_table(self, tickets):
        self.ticket_table.setRowCount(len(tickets))

        for row, ticket in enumerate(tickets):
            self.ticket_table.setItem(row, 0, QTableWidgetItem(ticket.id))
            self.ticket_table.setItem(
                row,
                1,
                QTableWidgetItem(ticket.created_at.strftime("%d-%m-%Y %H:%M:%S")),
            )
            self.ticket_table.setItem(
                row,
                2,
                QTableWidgetItem(
                    ticket.validated_at.strftime("%d-%m-%Y %H:%M:%S")
                    if ticket.validated_at
                    else "Não Validado"
                ),
            )
            self.ticket_table.setItem(
                row,
                3,
                QTableWidgetItem(
                    ticket.ticket_type.name if ticket.ticket_type else "Desconhecido"
                ),
            )
            self.ticket_table.setItem(
                row,
                4,
                QTableWidgetItem(
                    ticket.customer.name if ticket.customer else "Desconhecido"
                ),
            )
            self.ticket_table.setItem(
                row,
                5,
                QTableWidgetItem(
                    ticket.employee.name if ticket.employee else "Não Validado"
                ),
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
