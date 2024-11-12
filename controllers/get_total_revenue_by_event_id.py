from PyQt5.QtWidgets import (
    QMainWindow,
    QPushButton,
    QVBoxLayout,
    QWidget,
    QLineEdit,
    QFormLayout,
    QMessageBox,
    QLabel,
)
from PyQt5.QtGui import QIcon

from use_cases import get_total_revenue_by_event_id


class GetTotalRevenueByEventIdWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Calcular Faturamento Total do Evento")
        self.setWindowIcon(QIcon("haru.ico"))

        layout = QVBoxLayout()

        self.form_layout = QFormLayout()
        self.event_id_input = QLineEdit()
        self.event_id_input.setPlaceholderText("Digite o ID do evento")
        self.form_layout.addRow("ID do Evento:", self.event_id_input)

        layout.addLayout(self.form_layout)

        self.revenue_label = QLabel("Faturamento Total: R$ 0,00")
        layout.addWidget(self.revenue_label)

        self.search_button = QPushButton("Calcular Faturamento")
        self.search_button.clicked.connect(self.handle)
        layout.addWidget(self.search_button)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def handle(self):
        event_id = self.event_id_input.text()

        if not event_id:
            self.show_message(
                "Erro",
                "O campo ID do evento é obrigatório.",
                QMessageBox.Warning,
            )
            return

        try:
            total_revenue = get_total_revenue_by_event_id.execute(event_id)
            self.revenue_label.setText(f"Faturamento Total: R$ {total_revenue:,.2f}")
        except Exception as e:
            self.show_message(
                "Erro", f"Erro ao calcular faturamento: {str(e)}", QMessageBox.Critical
            )

    def show_message(self, title, message, icon):
        msg_box = QMessageBox()
        msg_box.setWindowTitle(title)
        msg_box.setText(message)
        msg_box.setIcon(icon)
        msg_box.exec_()
