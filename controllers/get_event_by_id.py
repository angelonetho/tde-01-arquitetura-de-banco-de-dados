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

from use_cases import get_event_by_id


class GetEventByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Evento pelo ID")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.event_id_input = QLineEdit()
        self.event_id_input.setPlaceholderText("Digite o ID do evento")

        self.form_layout.addRow("ID do Evento:", self.event_id_input)

        layout.addLayout(self.form_layout)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText(
            "As informações do evento aparecerão aqui..."
        )
        layout.addWidget(self.result_display)

        self.search_button = QPushButton("Buscar Evento")
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
            result = get_event_by_id.execute(event_id)
            if result:
                self.result_display.setPlainText(
                    f"Evento encontrado:\n\n"
                    f"Nome: {result.name}\n"
                    f"Descrição: {result.description}\n"
                    f"Local: {result.avenue}\n"
                    f"Data e Hora: {result.event_time}"
                )
            else:
                self.result_display.setPlainText("Evento não encontrado.")
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar evento: {str(e)}", QMessageBox.Critical
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
