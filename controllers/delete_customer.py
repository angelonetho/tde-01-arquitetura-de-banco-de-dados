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

from use_cases import delete_customer


class DeleteCustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excluir Cliente")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.customer_id_input = QLineEdit()
        self.customer_id_input.setPlaceholderText("Digite o ID do cliente")

        self.form_layout.addRow("ID do Cliente:", self.customer_id_input)

        layout.addLayout(self.form_layout)

        self.delete_button = QPushButton("Excluir Cliente")
        self.delete_button.clicked.connect(self.handle)
        layout.addWidget(self.delete_button)

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
            result = delete_customer.execute(customer_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao excluir cliente: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso", f"Cliente excluído com sucesso.", QMessageBox.Information
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
