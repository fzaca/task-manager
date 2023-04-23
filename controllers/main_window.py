from PySide6.QtWidgets import QMainWindow

from views.main_window_ui import Ui_MainWindow

class MainWindowForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

    def hello(self):
        print('Hello World')