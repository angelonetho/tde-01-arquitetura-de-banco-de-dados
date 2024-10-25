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

from use_cases import edit_employee


class EditEmployeeWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Editar Funcionário")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()

        self.employee_id_input = QLineEdit()
        self.name_input = QLineEdit()

        self.employee_id_input.setPlaceholderText("Digite o ID do funcionário")
        self.name_input.setPlaceholderText("Digite o nome do funcionário")

        self.form_layout.addRow("ID do Funcionário:", self.employee_id_input)
        self.form_layout.addRow("Nome:", self.name_input)

        layout.addLayout(self.form_layout)

        self.edit_button = QPushButton("Editar Funcionário")
        self.edit_button.clicked.connect(self.handle)
        layout.addWidget(self.edit_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        employee_id = self.employee_id_input.text()
        name = self.name_input.text()

        if not employee_id or not name:
            self.show_message(
                "Erro", "Todos os campos são obrigatórios.", QMessageBox.Warning
            )
            return

        try:
            result = edit_employee.execute(employee_id, name)
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao editar funcionário: {str(e)}", QMessageBox.Critical
            )
            return

        self.show_message(
            "Sucesso",
            f"Funcionário atualizado com sucesso: {result.name}",
            QMessageBox.Information,
        )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
