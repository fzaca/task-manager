from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QWidget, QHBoxLayout, QCheckBox, QLabel

from views.main_window_ui import Ui_MainWindow

from utils.database import create_connection

class MainWindowForm(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        # Set ui elements
        self.tasks_layout.setAlignment(Qt.AlignTop)

        self.conn = create_connection()
        self.cursor = self.conn.cursor()

        self.add_button.clicked.connect(self.add_task)

        self.render_tasks()

    def add_task(self):
        task = self.task_input.text()
        if not task: return
        self.cursor.execute('''
            INSERT INTO task (description, completed) VALUES (?, ?)
        ''', (task, False))
        self.conn.commit()
        self.task_input.clear()
        self.render_tasks()

    def render_tasks(self):
        while self.tasks_layout.count():
            self.tasks_layout.takeAt(0).widget().deleteLater()
        rows = self.cursor.execute('SELECT * FROM task').fetchall()
        for i, task in enumerate(rows):
            date = task[1]
            description = task[2]
            completed = task[3]

            task_widget = QWidget()
            task_layout = QHBoxLayout(task_widget)
            task_layout.setContentsMargins(0, 0, 0, 0)
            
            check_box = QCheckBox()
            task_layout.addWidget(check_box)
            
            label = QLabel(description)
            task_layout.addWidget(label)

            task_layout.setAlignment(Qt.AlignLeft)

            task_widget.setStyleSheet('''
                background-color: #FABD2F;
                border-radius: 5px;
                padding-left: 20px;
            ''')
            task_widget.setMinimumHeight(40)
            task_widget.setMaximumHeight(40)

            self.tasks_layout.addWidget(task_widget)