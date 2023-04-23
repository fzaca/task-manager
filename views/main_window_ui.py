# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.task_list = QListWidget(self.centralwidget)
        self.task_list.setObjectName(u"task_list")

        self.verticalLayout.addWidget(self.task_list)

        self.task_input_container = QWidget(self.centralwidget)
        self.task_input_container.setObjectName(u"task_input_container")
        self.horizontalLayout = QHBoxLayout(self.task_input_container)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.task_label = QLabel(self.task_input_container)
        self.task_label.setObjectName(u"task_label")

        self.horizontalLayout.addWidget(self.task_label)

        self.task_input = QLineEdit(self.task_input_container)
        self.task_input.setObjectName(u"task_input")

        self.horizontalLayout.addWidget(self.task_input)

        self.add_button = QPushButton(self.task_input_container)
        self.add_button.setObjectName(u"add_button")

        self.horizontalLayout.addWidget(self.add_button)


        self.verticalLayout.addWidget(self.task_input_container)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Task Manager", None))
        self.task_label.setText(QCoreApplication.translate("MainWindow", u"Task:", None))
        self.add_button.setText(QCoreApplication.translate("MainWindow", u"Add", None))
    # retranslateUi

