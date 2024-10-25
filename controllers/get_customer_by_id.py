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

from use_cases import get_customer_by_id


class GetCustomerByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Cliente pelo ID")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.customer_id_input = QLineEdit()
        self.customer_id_input.setPlaceholderText("Digite o ID do cliente")

        self.form_layout.addRow("ID do Cliente:", self.customer_id_input)

        layout.addLayout(self.form_layout)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText(
            "As informações do cliente aparecerão aqui..."
        )
        layout.addWidget(self.result_display)

        self.search_button = QPushButton("Buscar Cliente")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        customer_id = self.customer_id_input.text()

        if not customer_id:
            self.show_message(
                "Erro", "O campo ID do cliente é obrigatório.", QMessageBox.Warning
            )
            return

        try:
            result = get_customer_by_id.execute(customer_id)
            if result:
                self.result_display.setPlainText(
                    f"Cliente encontrado:\n\n"
                    f"Nome: {result.name}\n"
                    f"Email: {result.email}\n"
                    f"CPF: {result.cpf}\n"
                    f"Data de Nascimento: {result.birth_date}"
                )
            else:
                self.result_display.setPlainText("Cliente não encontrado.")
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar cliente: {str(e)}", QMessageBox.Critical
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
