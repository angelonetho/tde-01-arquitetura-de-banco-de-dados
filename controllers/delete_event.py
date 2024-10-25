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

from use_cases import delete_event


class DeleteEventWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excluir Evento")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.event_id_input = QLineEdit()
        self.event_id_input.setPlaceholderText("Digite o ID do evento")

        self.form_layout.addRow("ID do Evento:", self.event_id_input)

        layout.addLayout(self.form_layout)

        self.delete_button = QPushButton("Excluir Evento")
        self.delete_button.clicked.connect(self.handle)
        layout.addWidget(self.delete_button)

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
            result = delete_event.execute(event_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao excluir evento: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso", "Evento excluído com sucesso.", QMessageBox.Information
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
