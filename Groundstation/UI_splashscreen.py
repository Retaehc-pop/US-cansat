# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_splashscreen.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
f="Montserrat ExtraBold"
f1="Bahnschrift"
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(600, 400)
        MainWindow.setMinimumSize(QtCore.QSize(600, 400))
        MainWindow.setMaximumSize(QtCore.QSize(600, 400))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.Splashscreen = QtWidgets.QFrame(self.centralwidget)
        self.Splashscreen.setStyleSheet("background-color: rgb(255, 255, 255);\n"
        "border-radius: 20px;\n"
        "")
        self.Splashscreen.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Splashscreen.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Splashscreen.setObjectName("Splashscreen")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.Splashscreen)
        self.horizontalLayout_2.setContentsMargins(15, 15, 15, 15)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.Title = QtWidgets.QFrame(self.Splashscreen)
        self.Title.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.Title.setFrameShadow(QtWidgets.QFrame.Raised)
        self.Title.setObjectName("Title")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.Title)
        self.verticalLayout.setContentsMargins(8, 0, 0, 8)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lb_title = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily(f)
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.lb_title.setFont(font)
        self.lb_title.setStyleSheet("color: rgb(0, 0, 97);")
        self.lb_title.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lb_title.setObjectName("lb_title")
        self.verticalLayout.addWidget(self.lb_title)
        self.lb_version = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily(f)
        font.setPointSize(12)
        self.lb_version.setFont(font)
        self.lb_version.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.lb_version.setObjectName("lb_version")
        self.verticalLayout.addWidget(self.lb_version)
        self.blank1 = QtWidgets.QFrame(self.Title)
        self.blank1.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blank1.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blank1.setObjectName("blank1")
        self.verticalLayout.addWidget(self.blank1)
        self.lb_status = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily(f)
        font.setPointSize(12)
        self.lb_status.setFont(font)
        self.lb_status.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lb_status.setObjectName("lb_status")
        self.verticalLayout.addWidget(self.lb_status)
        self.blank2 = QtWidgets.QFrame(self.Title)
        self.blank2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.blank2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.blank2.setObjectName("blank2")
        self.verticalLayout.addWidget(self.blank2)
        self.lb_year = QtWidgets.QLabel(self.Title)
        font = QtGui.QFont()
        font.setFamily(f)
        font.setPointSize(12)
        self.lb_year.setFont(font)
        self.lb_year.setAlignment(QtCore.Qt.AlignBottom|QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft)
        self.lb_year.setObjectName("lb_year")
        self.verticalLayout.addWidget(self.lb_year)
        self.logo = QtWidgets.QFrame(self.Title)
        self.logo.setMaximumSize(QtCore.QSize(16777215, 40))
        self.logo.setStyleSheet("border-radius: 0px;\n"
        "background-image: url(:/Image/Image/SPACE_AC.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.verticalLayout.addWidget(self.logo)
        self.horizontalLayout_2.addWidget(self.Title)
        self.InfoBar = QtWidgets.QFrame(self.Splashscreen)
        self.InfoBar.setMinimumSize(QtCore.QSize(320, 0))
        self.InfoBar.setMaximumSize(QtCore.QSize(320, 16777215))
        self.InfoBar.setStyleSheet("background-image: url(:/Image/Image/SPACE_SPLASH2.png);\n"
        "border-radius: 12px;")
        self.InfoBar.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.InfoBar.setFrameShadow(QtWidgets.QFrame.Raised)
        self.InfoBar.setObjectName("InfoBar")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.InfoBar)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setSpacing(0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.horizontalLayout_2.addWidget(self.InfoBar)
        self.horizontalLayout.addWidget(self.Splashscreen)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.lb_title.setText(_translate("MainWindow", "ALIEN SAT GCS"))
        self.lb_version.setText(_translate("MainWindow", "Ver.0.1.0 (WAREDTANS)"))
        self.lb_status.setText(_translate("MainWindow", "Scanning all COM Ports..."))
        self.lb_year.setText(_translate("MainWindow", "2018 - 2021 : SPACE AC"))

import ui_splashscreen_resource_rc

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
