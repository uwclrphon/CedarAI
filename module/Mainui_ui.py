# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Mainui.ui'
##
## Created by: Qt User Interface Compiler version 6.10.2
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
from PySide6.QtWidgets import (QApplication, QFrame, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)
import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(691, 430)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(10, 10, 671, 411))
        self.frame.setStyleSheet(u"#frame {\n"
"background-color:rgb(255, 255, 255);\n"
"border-radius:20px;\n"
"box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);\n"
"}")
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.frame_2 = QFrame(self.frame)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 0, 671, 51))
        self.frame_2.setStyleSheet(u"#frame_2{\n"
"background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357ae8);\n"
"border-top-right-radius:20px;\n"
"border-top-left-radius:20px;\n"
"}")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(20, 10, 91, 26))
        self.pushButton.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	border-radius: 8px;\n"
"	padding: 4px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	padding-top: 5px;\n"
"	padding-left: 5px;\n"
"}")
        self.pushButton_5 = QPushButton(self.frame_2)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(120, 10, 91, 26))
        self.pushButton_5.setStyleSheet(u"QPushButton {\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	font: 12pt \"Microsoft YaHei UI\";\n"
"	border-radius: 8px;\n"
"	padding: 4px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	padding-top: 5px;\n"
"	padding-left: 5px;\n"
"}")
        self.pushButton_2 = QPushButton(self.frame_2)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(630, 10, 21, 26))
        self.pushButton_2.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	padding-bottom: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"}")
        icon = QIcon()
        icon.addFile(u":/icons/image/close.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_3 = QPushButton(self.frame_2)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(600, 10, 21, 26))
        self.pushButton_3.setStyleSheet(u"QPushButton{\n"
"	border:none;\n"
"	background-color: rgba(255, 255, 255, 0.1);\n"
"	border-radius: 4px;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	padding-bottom: 5px;\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"}")
        icon1 = QIcon()
        icon1.addFile(u":/icons/image/minimize.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon1)
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(30, 354, 581, 31))
        self.lineEdit.setStyleSheet(u"background-color: rgba(255, 255, 255, 0.9);\n"
"border: 2px solid #4a90e2;\n"
"border-radius: 10px;\n"
"padding: 5px 12px;\n"
"font-size: 11pt;")
        self.textBrowser = QTextBrowser(self.frame)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(30, 60, 621, 271))
        self.textBrowser.setStyleSheet(u"border: none;\n"
"background-color: #f5f5f5;\n"
"border-radius: 10px;\n"
"padding: 10px;")
        self.pushButton_4 = QPushButton(self.frame)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(620, 355, 41, 31))
        self.pushButton_4.setStyleSheet(u"QPushButton {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357ae8);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	font-size: 11pt;\n"
"}\n"
"QPushButton:hover {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5a9cf2, stop:1 #478af8);\n"
"	box-shadow: 0 2px 8px rgba(53, 122, 232, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3a80d2, stop:1 #276ac8);\n"
"	padding-top: 2px;\n"
"	padding-left: 2px;\n"
"}")
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.pushButton_3.clicked.connect(MainWindow.showMinimized)
        self.pushButton_2.clicked.connect(MainWindow.close)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u6e05\u7a7a\u6d88\u606f", None))
        self.pushButton_5.setText(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e", None))
        self.pushButton_2.setText("")
        self.pushButton_3.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u53d1\u6d88\u606f...", None))
        self.textBrowser.setHtml(QCoreApplication.translate("MainWindow", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.pushButton_4.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
    # retranslateUi

