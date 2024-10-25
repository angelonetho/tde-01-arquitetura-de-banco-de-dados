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

from use_cases import get_employee_by_id


class GetEmployeeByIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Buscar Funcionário pelo ID")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.employee_id_input = QLineEdit()
        self.employee_id_input.setPlaceholderText("Digite o ID do funcionário")

        self.form_layout.addRow("ID do Funcionário:", self.employee_id_input)

        layout.addLayout(self.form_layout)

        self.result_display = QTextEdit()
        self.result_display.setReadOnly(True)
        self.result_display.setPlaceholderText(
            "As informações do funcionário aparecerão aqui..."
        )
        layout.addWidget(self.result_display)

        self.search_button = QPushButton("Buscar Funcionário")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        employee_id = self.employee_id_input.text()

        if not employee_id:
            self.show_message(
                "Erro", "O campo ID do funcionário é obrigatório.", QMessageBox.Warning
            )
            return

        try:
            result = get_employee_by_id.execute(employee_id)
            if result:
                self.result_display.setPlainText(
                    f"Funcionário encontrado:\n\n"
                    f"Nome: {result.name}\n"
                    f"CPF: {result.cpf}\n"
                )
            else:
                self.result_display.setPlainText("Funcionário não encontrado.")
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao buscar funcionário: {str(e)}", QMessageBox.Critical
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
