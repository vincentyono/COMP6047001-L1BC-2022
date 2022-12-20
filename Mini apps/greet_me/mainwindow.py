from PySide6.QtWidgets import QMainWindow
from ui_mainwindow import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.greet_button.clicked.connect(
            lambda: print(f"Hello, {self.ui.name_input.text()}"))
