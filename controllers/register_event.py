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
from datetime import datetime

from use_cases import register_event


class RegisterEventWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Evento")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.description_input = QLineEdit()
        self.avenue_input = QLineEdit()
        self.event_time_input = QLineEdit()

        self.name_input.setPlaceholderText("Digite o nome do evento")
        self.description_input.setPlaceholderText("Digite a descrição")
        self.avenue_input.setPlaceholderText("Digite o local (avenue)")
        self.event_time_input.setPlaceholderText("DD-MM-YYYY HH:MM:SS")

        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("Descrição:", self.description_input)
        self.form_layout.addRow("Local:", self.avenue_input)
        self.form_layout.addRow("Data e Hora:", self.event_time_input)

        layout.addLayout(self.form_layout)

        self.register_button = QPushButton("Registrar Evento")
        self.register_button.clicked.connect(self.handle)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        name = self.name_input.text()
        description = self.description_input.text()
        avenue = self.avenue_input.text()
        event_time_str = self.event_time_input.text()

        if not name or not description or not avenue or not event_time_str:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            event_time = datetime.strptime(event_time_str, "%d-%m-%Y %H:%M:%S")
        except ValueError:
            self.show_message(
                "Erro",
                "Formato de data e hora inválido. Use DD-MM-YYYY HH:MM:SS.",
                QMessageBox.Warning,
            )
            return

        try:
            result = register_event.execute(name, description, avenue, event_time)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao registrar evento: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Evento registrado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
