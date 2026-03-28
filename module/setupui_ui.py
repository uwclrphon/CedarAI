# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'setupui.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QListWidget, QListWidgetItem, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QWidget)
import res_rc

class Ui_SetupWindow(object):
    def setupUi(self, SetupWindow):
        if not SetupWindow.objectName():
            SetupWindow.setObjectName(u"SetupWindow")
        SetupWindow.resize(689, 496)
        self.centralwidget = QWidget(SetupWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(30, 30, 181, 441))
        self.frame.setStyleSheet(u"#frame {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357ae8);\n"
"border-radius:20px;\n"
"box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);\n"
"}")
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget = QStackedWidget(self.frame)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(20, 20, 141, 421))
        self.stackedWidget.setStyleSheet(u"QPushButton {\n"
"	background-color: rgba(255, 255, 255, 0.2);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	padding: 6px 12px;\n"
"	font-size: 11pt;\n"
"	margin: 4px 0;\n"
"}\n"
"QPushButton:hover {\n"
"	background-color: rgba(255, 255, 255, 0.3);\n"
"	box-shadow: 0 2px 8px rgba(0, 0, 0, 0.2);\n"
"}\n"
"QPushButton:pressed {\n"
"	background-color: rgba(255, 255, 255, 0.4);\n"
"	padding-top: 7px;\n"
"	padding-left: 7px;\n"
"}\n"
"#stackedWidget{\n"
"	background-color:rgba(255, 255, 255,0);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(20, 60, 101, 41))
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 30, 131, 31))
        self.label.setStyleSheet(u"background-color:rgba(255, 255, 255,0);\n"
"color:rgb(255, 255, 255);\n"
"font: 15pt \"Microsoft YaHei UI\";")
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(20, 100, 101, 41))
        self.pushButton_4 = QPushButton(self.page)
        self.pushButton_4.setObjectName(u"pushButton_4")
        self.pushButton_4.setGeometry(QRect(20, 140, 101, 41))
        self.pushButton_5 = QPushButton(self.page)
        self.pushButton_5.setObjectName(u"pushButton_5")
        self.pushButton_5.setGeometry(QRect(20, 180, 101, 41))
        self.pushButton_6 = QPushButton(self.page)
        self.pushButton_6.setObjectName(u"pushButton_6")
        self.pushButton_6.setGeometry(QRect(20, 220, 101, 41))
        self.pushButton_7 = QPushButton(self.page)
        self.pushButton_7.setObjectName(u"pushButton_7")
        self.pushButton_7.setGeometry(QRect(20, 260, 101, 41))
        self.pushButton_8 = QPushButton(self.page)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setGeometry(QRect(20, 300, 101, 41))
        self.pushButton_9 = QPushButton(self.page)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setGeometry(QRect(20, 340, 101, 41))
        self.pushButton_12 = QPushButton(self.page)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setGeometry(QRect(20, 380, 101, 41))
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.stackedWidget.addWidget(self.page_2)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(210, 90, 361, 351))
        self.frame_2.setStyleSheet(u"background-color:rgb(255, 255, 255);\n"
"border-top-right-radius:20px;\n"
"border-bottom-right-radius:20px;\n"
"box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.pushButton = QPushButton(self.frame_2)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(330, 10, 21, 26))
        self.pushButton.setStyleSheet(u"QPushButton{\n"
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
        self.pushButton.setIcon(icon)
        self.stackedWidget_2 = QStackedWidget(self.frame_2)
        self.stackedWidget_2.setObjectName(u"stackedWidget_2")
        self.stackedWidget_2.setGeometry(QRect(40, 30, 281, 281))
        self.stackedWidget_2.setStyleSheet(u"QPushButton {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #4a90e2, stop:1 #357ae8);\n"
"	color: rgb(255, 255, 255);\n"
"	border-radius: 10px;\n"
"	font-weight: bold;\n"
"	font-size: 11pt;\n"
"	padding: 6px 12px;\n"
"}\n"
"QPushButton:hover {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #5a9cf2, stop:1 #478af8);\n"
"	box-shadow: 0 2px 8px rgba(53, 122, 232, 0.4);\n"
"}\n"
"QPushButton:pressed {\n"
"	background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #3a80d2, stop:1 #276ac8);\n"
"	padding-top: 7px;\n"
"	padding-left: 7px;\n"
"}\n"
"QLineEdit{\n"
"	background-color: rgba(255, 255, 255, 0.9);\n"
"	border: 2px solid #4a90e2;\n"
"	border-radius: 8px;\n"
"	padding: 5px 10px;\n"
"	font-size: 11pt;\n"
"}\n"
"QLineEdit:focus {\n"
"	border: 2px solid #357ae8;\n"
"	background-color: white;\n"
"	box-shadow: 0 0 5px rgba(53, 122, 232, 0.5);\n"
"}\n"
"background-color:rgba(255, 255, 255,0);")
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.lineEdit = QLineEdit(self.page_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(20, 30, 241, 31))
        self.lineEdit_2 = QLineEdit(self.page_3)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(20, 120, 241, 31))
        self.pushButton_10 = QPushButton(self.page_3)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setGeometry(QRect(30, 220, 221, 26))
        self.label_2 = QLabel(self.page_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(60, 170, 191, 16))
        self.stackedWidget_2.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.lineEdit_3 = QLineEdit(self.page_4)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setGeometry(QRect(20, 150, 241, 31))
        self.lineEdit_4 = QLineEdit(self.page_4)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setGeometry(QRect(20, 90, 241, 31))
        self.pushButton_11 = QPushButton(self.page_4)
        self.pushButton_11.setObjectName(u"pushButton_11")
        self.pushButton_11.setGeometry(QRect(30, 220, 221, 26))
        self.lineEdit_5 = QLineEdit(self.page_4)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setGeometry(QRect(20, 30, 241, 31))
        self.stackedWidget_2.addWidget(self.page_4)
        self.page_7 = QWidget()
        self.page_7.setObjectName(u"page_7")
        self.listWidget = QListWidget(self.page_7)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(20, 30, 241, 201))
        self.pushButton_13 = QPushButton(self.page_7)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setGeometry(QRect(30, 240, 221, 26))
        self.stackedWidget_2.addWidget(self.page_7)
        self.stackedWidget_3 = QStackedWidget(self.frame_2)
        self.stackedWidget_3.setObjectName(u"stackedWidget_3")
        self.stackedWidget_3.setGeometry(QRect(70, 320, 221, 31))
        self.stackedWidget_3.setStyleSheet(u"color: rgb(170, 0, 0);")
        self.page_5 = QWidget()
        self.page_5.setObjectName(u"page_5")
        self.stackedWidget_3.addWidget(self.page_5)
        self.page_6 = QWidget()
        self.page_6.setObjectName(u"page_6")
        self.label_3 = QLabel(self.page_6)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(60, 10, 101, 16))
        self.stackedWidget_3.addWidget(self.page_6)
        SetupWindow.setCentralWidget(self.centralwidget)
        self.frame_2.raise_()
        self.frame.raise_()

        self.retranslateUi(SetupWindow)
        self.pushButton.clicked.connect(SetupWindow.close)

        self.stackedWidget.setCurrentIndex(0)
        self.stackedWidget_2.setCurrentIndex(1)
        self.stackedWidget_3.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(SetupWindow)
    # setupUi

    def retranslateUi(self, SetupWindow):
        SetupWindow.setWindowTitle(QCoreApplication.translate("SetupWindow", u"MainWindow", None))
        self.pushButton_2.setText(QCoreApplication.translate("SetupWindow", u"openai", None))
        self.label.setText(QCoreApplication.translate("SetupWindow", u"\u8bf7\u9009\u62e9\u6a21\u578b", None))
        self.pushButton_3.setText(QCoreApplication.translate("SetupWindow", u"gemini", None))
        self.pushButton_4.setText(QCoreApplication.translate("SetupWindow", u"deepseek", None))
        self.pushButton_5.setText(QCoreApplication.translate("SetupWindow", u"claude", None))
        self.pushButton_6.setText(QCoreApplication.translate("SetupWindow", u"\u7845\u57fa\u6d41\u52a8", None))
        self.pushButton_7.setText(QCoreApplication.translate("SetupWindow", u"\u6708\u4e4b\u6697\u9762", None))
        self.pushButton_8.setText(QCoreApplication.translate("SetupWindow", u"\u901a\u4e49\u5343\u95ee", None))
        self.pushButton_9.setText(QCoreApplication.translate("SetupWindow", u"\u81ea\u5b9a\u4e49\u5e73\u53f0", None))
        self.pushButton_12.setText(QCoreApplication.translate("SetupWindow", u"mod\u7ba1\u7406", None))
        self.pushButton.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("SetupWindow", u"API\u5bc6\u94a5", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("SetupWindow", u"\u6a21\u578b", None))
        self.pushButton_10.setText(QCoreApplication.translate("SetupWindow", u"\u786e\u8ba4", None))
        self.label_2.setText(QCoreApplication.translate("SetupWindow", u"\u5f53\u524d\u9009\u62e9\u6a21\u578b\u63d0\u4f9b\u5546\uff1aopenai", None))
        self.lineEdit_3.setPlaceholderText(QCoreApplication.translate("SetupWindow", u"\u6a21\u578b", None))
        self.lineEdit_4.setPlaceholderText(QCoreApplication.translate("SetupWindow", u"API\u5bc6\u94a5", None))
        self.pushButton_11.setText(QCoreApplication.translate("SetupWindow", u"\u786e\u8ba4", None))
        self.lineEdit_5.setPlaceholderText(QCoreApplication.translate("SetupWindow", u"\u63d0\u4f9b\u5546url", None))
        self.pushButton_13.setText(QCoreApplication.translate("SetupWindow", u"\u4fdd\u5b58mod\u914d\u7f6e", None))
        self.label_3.setText(QCoreApplication.translate("SetupWindow", u"\u5bc6\u94a5\u6216\u6a21\u578b\u4e0d\u53ef\u7528", None))
    # retranslateUi

