from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QTableWidget,
    QTableWidgetItem,
    QMessageBox,
)
from PyQt5.QtGui import QIcon

from use_cases import fetch_events


class FetchEventsWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Todos os Eventos")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.event_table = QTableWidget()
        self.event_table.setColumnCount(4)
        self.event_table.setHorizontalHeaderLabels(
            ["ID", "Nome", "Descrição", "Data e Hora"]
        )
        layout.addWidget(self.event_table)

        self.fetch_button = QPushButton("Buscar Eventos")
        self.fetch_button.clicked.connect(self.handle)
        layout.addWidget(self.fetch_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        try:
            events = fetch_events.execute()
            if events:
                self.populate_table(events)
            else:
                self.event_table.setRowCount(0)
                self.show_message(
                    "Aviso", "Nenhum evento encontrado.", QMessageBox.Information
                )
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar eventos: {str(e)}", QMessageBox.Critical
            )

    def populate_table(self, events):
        self.event_table.setRowCount(len(events))

        for row, event in enumerate(events):
            self.event_table.setItem(row, 0, QTableWidgetItem(event.id))
            self.event_table.setItem(row, 1, QTableWidgetItem(event.name))
            self.event_table.setItem(row, 2, QTableWidgetItem(event.description))
            self.event_table.setItem(
                row, 3, QTableWidgetItem(event.event_time.strftime("%d-%m-%Y %H:%M:%S"))
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
