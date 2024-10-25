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

from use_cases import register_employee


class RegisterEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Registrar Funcionário")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.name_input = QLineEdit()
        self.cpf_input = QLineEdit()

        self.name_input.setPlaceholderText("Digite o nome do funcionário")
        self.cpf_input.setPlaceholderText("Digite o CPF (somente números)")

        self.form_layout.addRow("Nome:", self.name_input)
        self.form_layout.addRow("CPF:", self.cpf_input)

        layout.addLayout(self.form_layout)

        self.register_button = QPushButton("Registrar Funcionário")
        self.register_button.clicked.connect(self.handle)
        layout.addWidget(self.register_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        name = self.name_input.text()
        cpf = self.cpf_input.text()

        if not name or not cpf:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            result = register_employee.execute(name, cpf)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao registrar funcionário: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Funcionário registrado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
