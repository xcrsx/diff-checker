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
from PySide6.QtWidgets import (QApplication, QHBoxLayout, QLayout, QPushButton,
    QSizePolicy, QTextEdit, QVBoxLayout, QWidget)

class Ui_DiffChecker(object):
    def setupUi(self, DiffChecker):
        if not DiffChecker.objectName():
            DiffChecker.setObjectName(u"DiffChecker")
        DiffChecker.resize(1137, 660)
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(DiffChecker.sizePolicy().hasHeightForWidth())
        DiffChecker.setSizePolicy(sizePolicy)
        DiffChecker.setStyleSheet(u"background-color: #282A36;")
        self.verticalLayout = QVBoxLayout(DiffChecker)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(10)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setSizeConstraint(QLayout.SizeConstraint.SetDefaultConstraint)
        self.verticalLayout_2.setContentsMargins(10, 10, 10, 10)
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(-1, -1, 500, -1)
        self.openFile1_btn = QPushButton(DiffChecker)
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

        self.openFile2_btn = QPushButton(DiffChecker)
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

        self.clear_btn = QPushButton(DiffChecker)
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

        self.exit_btn = QPushButton(DiffChecker)
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


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.file1_form = QTextEdit(DiffChecker)
        self.file1_form.setObjectName(u"file1_form")

        self.horizontalLayout_2.addWidget(self.file1_form)

        self.file2_form = QTextEdit(DiffChecker)
        self.file2_form.setObjectName(u"file2_form")

        self.horizontalLayout_2.addWidget(self.file2_form)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.diff_view_form = QTextEdit(DiffChecker)
        self.diff_view_form.setObjectName(u"diff_view_form")
        self.diff_view_form.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.diff_view_form)


        self.verticalLayout.addLayout(self.verticalLayout_2)


        self.retranslateUi(DiffChecker)

        QMetaObject.connectSlotsByName(DiffChecker)
    # setupUi

    def retranslateUi(self, DiffChecker):
        DiffChecker.setWindowTitle(QCoreApplication.translate("DiffChecker", u"Diff Checker", None))
        self.openFile1_btn.setText(QCoreApplication.translate("DiffChecker", u"Open File 1", None))
        self.openFile2_btn.setText(QCoreApplication.translate("DiffChecker", u"Open File 2", None))
        self.clear_btn.setText(QCoreApplication.translate("DiffChecker", u"Clear", None))
        self.exit_btn.setText(QCoreApplication.translate("DiffChecker", u"Exit", None))
        self.diff_view_form.setPlaceholderText("")
    # retranslateUi

