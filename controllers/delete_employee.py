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

from use_cases import delete_employee


class DeleteEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Excluir Funcionário")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.employee_id_input = QLineEdit()
        self.employee_id_input.setPlaceholderText("Digite o ID do funcionário")

        self.form_layout.addRow("ID do Funcionário:", self.employee_id_input)

        layout.addLayout(self.form_layout)

        self.delete_button = QPushButton("Excluir Funcionário")
        self.delete_button.clicked.connect(self.handle)
        layout.addWidget(self.delete_button)

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
            result = delete_employee.execute(employee_id)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao excluir funcionário: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso", f"Funcionário excluído com sucesso.", QMessageBox.Information
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
