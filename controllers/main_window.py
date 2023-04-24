from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QMainWindow, QWidget, QHBoxLayout, QCheckBox, 
    QLabel, QPushButton, QSpacerItem, QSizePolicy
)

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
            task_id = task[0]
            date = task[1]
            description = task[2]
            completed = task[3]

            task_widget = QWidget()
            task_layout = QHBoxLayout(task_widget)
            task_layout.setContentsMargins(0, 0, 0, 0)

            checkbox = QCheckBox()
            checkbox.setChecked(completed)
            checkbox.setObjectName(f"task_{task_id}")
            checkbox.stateChanged.connect(self.update_task)

            description_label = QLabel(description)
            description_label.setObjectName(f"description_{task_id}")
            if completed:
                description_label.setStyleSheet("color: gray; text-decoration: line-through;")

            delete_button = QPushButton("Eliminar")
            delete_button.setObjectName(f"delete_{task_id}")
            delete_button.clicked.connect(self.delete_task)

            task_layout.addWidget(checkbox)
            task_layout.addWidget(description_label)

            spacer_item = QSpacerItem(10000, 0, QSizePolicy.Expanding, QSizePolicy.Minimum)
            task_layout.addItem(spacer_item)

            task_layout.addWidget(delete_button)
            task_layout.addStretch(1)

            task_widget.setStyleSheet('''
                QWidget{
                    background-color: #ccc;
                    padding: 10px;
                    border-radius: 5px;
                    color: gray;
                }
            ''')

            self.tasks_layout.addWidget(task_widget)

    def update_task(self):
        checkbox = self.sender()
        task_id = int(checkbox.objectName().split("_")[1])
        completed = checkbox.isChecked()
        description_label = self.findChild(QLabel, f"description_{task_id}")
        if completed:
            description_label.setStyleSheet("color: gray; text-decoration: line-through;")
        else:
            description_label.setStyleSheet("color: gray; text-decoration: none;")
        self.cursor.execute('''
            UPDATE task SET completed = ? WHERE id = ?
        ''', (completed, task_id))
        self.conn.commit()

    def delete_task(self):
        button = self.sender()
        task_id = int(button.objectName().split("_")[1])
        self.cursor.execute('''
            DELETE FROM task WHERE id = ?
        ''', (task_id,))
        self.conn.commit()
        self.render_tasks()
