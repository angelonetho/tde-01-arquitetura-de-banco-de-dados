from PyQt5.QtWidgets import (
    QApplication,
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

from use_cases import fetch_ticket_types_by_event_id


class FetchTicketTypesByEventIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Tipos de Ingresso pelo ID do Evento")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.event_id_input = QLineEdit()
        self.event_id_input.setPlaceholderText("Digite o ID do evento")

        self.form_layout.addRow("ID do Evento:", self.event_id_input)

        layout.addLayout(self.form_layout)

        self.ticket_type_table = QTableWidget()
        self.ticket_type_table.setColumnCount(4)
        self.ticket_type_table.setHorizontalHeaderLabels(
            ["ID Tipo Ingresso", "Nome", "Descrição", "Preço"]
        )
        layout.addWidget(self.ticket_type_table)

        self.search_button = QPushButton("Buscar Tipos de Ingresso")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        event_id = self.event_id_input.text()

        if not event_id:
            self.show_message(
                "Erro", "O campo ID do evento é obrigatório.", QMessageBox.Warning
            )
            return

        try:
            ticket_types = fetch_ticket_types_by_event_id.execute(event_id)
            if ticket_types:
                self.populate_table(ticket_types)
            else:
                self.ticket_type_table.setRowCount(0)
                self.show_message(
                    "Aviso",
                    "Nenhum tipo de ingresso encontrado para este evento.",
                    QMessageBox.Information,
                )
        except Exception as e:
            self.show_message(
                "Erro",
                f"Erro ao buscar tipos de ingresso: {str(e)}",
                QMessageBox.Critical,
            )

    def populate_table(self, ticket_types):
        self.ticket_type_table.setRowCount(len(ticket_types))

        for row, ticket_type in enumerate(ticket_types):
            self.ticket_type_table.setItem(row, 0, QTableWidgetItem(ticket_type.id))
            self.ticket_type_table.setItem(row, 1, QTableWidgetItem(ticket_type.name))
            self.ticket_type_table.setItem(
                row, 2, QTableWidgetItem(ticket_type.description)
            )
            self.ticket_type_table.setItem(
                row, 3, QTableWidgetItem(f"R${ticket_type.price:.2f}")
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
