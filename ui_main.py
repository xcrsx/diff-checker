# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QHeaderView, QPushButton,
    QSizePolicy, QTableView, QTextEdit, QWidget)

class Ui_DiffChecker(object):
    def setupUi(self, DiffChecker):
        if not DiffChecker.objectName():
            DiffChecker.setObjectName(u"DiffChecker")
        DiffChecker.resize(1128, 652)
        DiffChecker.setStyleSheet(u"background-color: #282A36;")
        self.diff_view = QTableView(DiffChecker)
        self.diff_view.setObjectName(u"diff_view")
        self.diff_view.setGeometry(QRect(0, 300, 1131, 351))
        self.diff_view.setMaximumSize(QSize(1131, 16777215))
        self.layoutWidget = QWidget(DiffChecker)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 428, 34))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.openFile1_btn = QPushButton(self.layoutWidget)
        self.openFile1_btn.setObjectName(u"openFile1_btn")
        self.openFile1_btn.setStyleSheet(u"QPushButton{\n"
"	color: #F8F8F2;\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius:7px;\n"
"	background-color:RGB(98, 114, 164);\n"
"	width: 100;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(98, 114, 164,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(98, 114, 164,70);\n"
"}")

        self.horizontalLayout.addWidget(self.openFile1_btn)

        self.openFile2_btn = QPushButton(self.layoutWidget)
        self.openFile2_btn.setObjectName(u"openFile2_btn")
        self.openFile2_btn.setStyleSheet(u"QPushButton{\n"
"	color: #F8F8F2;\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius:7px;\n"
"	background-color:RGB(98, 114, 164);\n"
"	width: 100;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(98, 114, 164,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(98, 114, 164,70);\n"
"}")

        self.horizontalLayout.addWidget(self.openFile2_btn)

        self.clear_btn = QPushButton(self.layoutWidget)
        self.clear_btn.setObjectName(u"clear_btn")
        self.clear_btn.setStyleSheet(u"QPushButton{\n"
"	color: #F8F8F2;\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius:7px;\n"
"	background-color:RGB(98, 114, 164);\n"
"	width: 100;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(98, 114, 164,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(98, 114, 164,70);\n"
"}")

        self.horizontalLayout.addWidget(self.clear_btn)

        self.exit_btn = QPushButton(self.layoutWidget)
        self.exit_btn.setObjectName(u"exit_btn")
        self.exit_btn.setStyleSheet(u"QPushButton{\n"
"	color: #F8F8F2;\n"
"	border: 1px solid rgba(255,255,255,40);\n"
"	border-radius:7px;\n"
"	background-color:RGB(98, 114, 164);\n"
"	width: 100;\n"
"	height: 30;\n"
"}\n"
"QPushButton:hover{\n"
"	background-color:rgba(98, 114, 164,30);\n"
"}\n"
"QPushButton:pressed{\n"
"	background-color:rgba(98, 114, 164,70);\n"
"}")

        self.horizontalLayout.addWidget(self.exit_btn)

        self.layoutWidget1 = QWidget(DiffChecker)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(0, 40, 1131, 251))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.file1_content = QTextEdit(self.layoutWidget1)
        self.file1_content.setObjectName(u"file1_content")

        self.horizontalLayout_2.addWidget(self.file1_content)

        self.file2_content = QTextEdit(self.layoutWidget1)
        self.file2_content.setObjectName(u"file2_content")

        self.horizontalLayout_2.addWidget(self.file2_content)


        self.retranslateUi(DiffChecker)

        QMetaObject.connectSlotsByName(DiffChecker)
    # setupUi

    def retranslateUi(self, DiffChecker):
        DiffChecker.setWindowTitle(QCoreApplication.translate("DiffChecker", u"Diff Checker", None))
        self.openFile1_btn.setText(QCoreApplication.translate("DiffChecker", u"Open File 1", None))
        self.openFile2_btn.setText(QCoreApplication.translate("DiffChecker", u"Open File 2", None))
        self.clear_btn.setText(QCoreApplication.translate("DiffChecker", u"Clear", None))
        self.exit_btn.setText(QCoreApplication.translate("DiffChecker", u"Exit", None))
    # retranslateUi

