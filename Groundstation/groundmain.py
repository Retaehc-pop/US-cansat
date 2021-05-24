import sys

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5 import QtWebEngineWidgets
from PyQt5.QtCore import QThread
from PyQt5.QtWidgets import QTableWidgetItem
from pyqtgraph import PlotWidget

import GNSS
import RTC
import map
import Datahandle
import mqtt
import Command as CMD


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(2123, 1005)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("../S__11739139.jpg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setToolTip("")
        MainWindow.setAutoFillBackground(False)
        MainWindow.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setStyleSheet("background-color: rgb(56,58,89);")
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.tabWidget.setFont(font)
        self.tabWidget.setStyleSheet("color: rgb(220, 220, 220);\n"
                                     "border-color: rgb(255, 255, 255);\n"
                                     "background-color: rgb(56, 58, 89);\n"
                                     "boarder-radius: 10px;")
        self.tabWidget.setObjectName("tabWidget")
        self.tab_1 = QtWidgets.QWidget()
        font = QtGui.QFont()
        self.tab_1.setFont(font)
        self.tab_1.setAutoFillBackground(False)
        self.tab_1.setStyleSheet("background-color: rgb(56, 58, 89);")
        self.tab_1.setObjectName("tab_1")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.tab_1)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.SP1_Temperature = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_Temperature.setFont(font)
        self.SP1_Temperature.setObjectName("SP1_Temperature")
        self.gridLayout_6.addWidget(self.SP1_Temperature, 23, 7, 1, 3)
        self.SP1_T = PlotWidget(self.tab_1)
        self.SP1_T.setAutoFillBackground(False)
        self.SP1_T.setObjectName("SP1_T")
        self.gridLayout_6.addWidget(self.SP1_T, 19, 7, 4, 7)
        self.TimeElapsed = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.TimeElapsed.setFont(font)
        self.TimeElapsed.setAlignment(QtCore.Qt.AlignCenter)
        self.TimeElapsed.setObjectName("TimeElapsed")
        self.gridLayout_6.addWidget(self.TimeElapsed, 34, 2, 1, 5)
        self.PC_Latitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_Latitude.setFont(font)
        self.PC_Latitude.setObjectName("PC_Latitude")
        self.gridLayout_6.addWidget(self.PC_Latitude, 20, 20, 1, 1)
        self.PC_GIS = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.PC_GIS.setFont(font)
        self.PC_GIS.setStyleSheet("\n"
                                  "color: rgb(255, 79, 82);")
        self.PC_GIS.setAlignment(QtCore.Qt.AlignCenter)
        self.PC_GIS.setObjectName("PC_GIS")
        self.gridLayout_6.addWidget(self.PC_GIS, 19, 20, 1, 2)
        self.PC_lon = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_lon.setFont(font)
        self.PC_lon.setStyleSheet("\n"
                                  "color: rgb(255, 255, 0);")
        self.PC_lon.setObjectName("PC_lon")
        self.gridLayout_6.addWidget(self.PC_lon, 21, 21, 1, 1)
        self.PC_Longtitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_Longtitude.setFont(font)
        self.PC_Longtitude.setObjectName("PC_Longtitude")
        self.gridLayout_6.addWidget(self.PC_Longtitude, 21, 20, 1, 1)
        self.PC_Gd = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_Gd.setFont(font)
        self.PC_Gd.setStyleSheet("\n"
                                 "color: rgb(255, 255, 0);")
        self.PC_Gd.setObjectName("PC_Gd")
        self.gridLayout_6.addWidget(self.PC_Gd, 22, 21, 1, 1)
        self.PC_la = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_la.setFont(font)
        self.PC_la.setStyleSheet("\n"
                                 "color: rgb(255, 255, 0);")
        self.PC_la.setObjectName("PC_la")
        self.gridLayout_6.addWidget(self.PC_la, 20, 21, 1, 1)
        self.PC_Gnddis = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PC_Gnddis.setFont(font)
        self.PC_Gnddis.setObjectName("PC_Gnddis")
        self.gridLayout_6.addWidget(self.PC_Gnddis, 22, 20, 1, 1)
        self.C_GIS = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.C_GIS.setFont(font)
        self.C_GIS.setStyleSheet("\n"
                                 "color: rgb(255, 79, 82);")
        self.C_GIS.setAlignment(QtCore.Qt.AlignCenter)
        self.C_GIS.setObjectName("C_GIS")
        self.gridLayout_6.addWidget(self.C_GIS, 11, 20, 1, 2)
        self.command_t = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.command_t.setFont(font)
        self.command_t.setStyleSheet("\n"
                                     "color: rgb(255, 79, 82);")
        self.command_t.setAlignment(QtCore.Qt.AlignCenter)
        self.command_t.setObjectName("command_t")
        self.gridLayout_6.addWidget(self.command_t, 0, 13, 1, 2)
        self.mqttactivation = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.mqttactivation.setFont(font)
        self.mqttactivation.setStyleSheet("background-color: rgb(98, 114, 164);")
        self.mqttactivation.setObjectName("mqttactivation")
        self.gridLayout_6.addWidget(self.mqttactivation, 4, 9, 1, 1)
        self.State_Prelaunch = QtWidgets.QProgressBar(self.tab_1)
        self.State_Prelaunch.setStyleSheet("QProgressBar{\n"
                                           "    backgroundcolor:rgb(98,114,164);\n"
                                           "    color:rgb(200,200,200);\n"
                                           "    boder-style: none;\n"
                                           "    boder-radius: 10px;\n"
                                           "}\n"
                                           "QProgressBar::chunk{\n"
                                           "    border-radius: 10px;\n"
                                           "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                           "}")
        self.State_Prelaunch.setMaximum(1)
        self.State_Prelaunch.setProperty("value", 1)
        self.State_Prelaunch.setTextVisible(False)
        self.State_Prelaunch.setObjectName("State_Prelaunch")
        self.gridLayout_6.addWidget(self.State_Prelaunch, 2, 0, 1, 1)
        self.SP1_Packetcount = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_Packetcount.setFont(font)
        self.SP1_Packetcount.setObjectName("SP1_Packetcount")
        self.gridLayout_6.addWidget(self.SP1_Packetcount, 20, 0, 1, 1)
        self.PORTSelecter = QtWidgets.QComboBox(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.PORTSelecter.setFont(font)
        self.PORTSelecter.setStyleSheet("background-color: rgb(98, 114, 164);")
        self.PORTSelecter.setObjectName("PORTSelecter")
        self.PORTSelecter.addItem("")
        self.gridLayout_6.addWidget(self.PORTSelecter, 4, 1, 1, 1)
        self.Launched = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Launched.setFont(font)
        self.Launched.setAlignment(QtCore.Qt.AlignCenter)
        self.Launched.setObjectName("Launched")
        self.gridLayout_6.addWidget(self.Launched, 3, 1, 1, 1)
        self.PRESSURE_INPUT = QtWidgets.QLineEdit(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(8)
        font.setBold(True)
        font.setWeight(75)
        self.PRESSURE_INPUT.setFont(font)
        self.PRESSURE_INPUT.setAutoFillBackground(False)
        self.PRESSURE_INPUT.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                          "color: rgb(0, 0, 0);")
        self.PRESSURE_INPUT.setObjectName("PRESSURE_INPUT")
        self.gridLayout_6.addWidget(self.PRESSURE_INPUT, 4, 18, 1, 2)
        self.PORT = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.PORT.setFont(font)
        self.PORT.setObjectName("PORT")
        self.gridLayout_6.addWidget(self.PORT, 4, 0, 1, 1)
        self.Time = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Time.setFont(font)
        self.Time.setObjectName("Time")
        self.gridLayout_6.addWidget(self.Time, 34, 9, 1, 4)
        self.Prelaunch = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Prelaunch.setFont(font)
        self.Prelaunch.setAlignment(QtCore.Qt.AlignCenter)
        self.Prelaunch.setObjectName("Prelaunch")
        self.gridLayout_6.addWidget(self.Prelaunch, 3, 0, 1, 1)
        self.SIMPRESSURE = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SIMPRESSURE.setFont(font)
        self.SIMPRESSURE.setStyleSheet("background-color: rgb(98, 114, 164);")
        self.SIMPRESSURE.setObjectName("SIMPRESSURE")
        self.gridLayout_6.addWidget(self.SIMPRESSURE, 4, 20, 1, 2)
        self.C_Galt = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_Galt.setFont(font)
        self.C_Galt.setStyleSheet("color: rgb(255, 255, 0);")
        self.C_Galt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.C_Galt.setObjectName("C_Galt")
        self.gridLayout_6.addWidget(self.C_Galt, 17, 18, 1, 2)
        self.C_echo = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_echo.setFont(font)
        self.C_echo.setAutoFillBackground(False)
        self.C_echo.setStyleSheet("color: rgb(255, 255, 0);")
        self.C_echo.setObjectName("C_echo")
        self.gridLayout_6.addWidget(self.C_echo, 4, 16, 1, 2)
        self.Start = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Start.setFont(font)
        self.Start.setStyleSheet("background-color: rgb(98, 114, 164);")
        self.Start.setObjectName("Start")
        self.gridLayout_6.addWidget(self.Start, 4, 7, 1, 1)
        self.ELAPSED = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.ELAPSED.setFont(font)
        self.ELAPSED.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ELAPSED.setObjectName("ELAPSED")
        self.gridLayout_6.addWidget(self.ELAPSED, 34, 0, 1, 2)
        self.C_Packetcount = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Packetcount.setFont(font)
        self.C_Packetcount.setObjectName("C_Packetcount")
        self.gridLayout_6.addWidget(self.C_Packetcount, 12, 0, 1, 1)
        self.State_launch = QtWidgets.QProgressBar(self.tab_1)
        self.State_launch.setStyleSheet("QProgressBar{\n"
                                        "    backgroundcolor:rgb(98,114,164);\n"
                                        "    color:rgb(200,200,200);\n"
                                        "    boder-style: none;\n"
                                        "    boder-radius: 10px;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                        "}")
        self.State_launch.setMaximum(1)
        self.State_launch.setProperty("value", 1)
        self.State_launch.setTextVisible(False)
        self.State_launch.setObjectName("State_launch")
        self.gridLayout_6.addWidget(self.State_launch, 2, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.gridLayout_6.addWidget(self.label, 12, 20, 1, 1)
        self.refresh = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.refresh.setFont(font)
        self.refresh.setStyleSheet("background-color: rgb(98, 114, 164);")
        self.refresh.setObjectName("refresh")
        self.gridLayout_6.addWidget(self.refresh, 4, 10, 1, 4)
        self.CXOFF = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CXOFF.setFont(font)
        self.CXOFF.setObjectName("CXOFF")
        self.gridLayout_6.addWidget(self.CXOFF, 3, 14, 1, 2)
        self.Lastcommand_t = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Lastcommand_t.setFont(font)
        self.Lastcommand_t.setAutoFillBackground(False)
        self.Lastcommand_t.setObjectName("Lastcommand_t")
        self.gridLayout_6.addWidget(self.Lastcommand_t, 4, 14, 1, 2)
        self.CXON = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.CXON.setFont(font)
        self.CXON.setObjectName("CXON")
        self.gridLayout_6.addWidget(self.CXON, 2, 14, 1, 2)
        self.SPX1OFF = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SPX1OFF.setFont(font)
        self.SPX1OFF.setObjectName("SPX1OFF")
        self.gridLayout_6.addWidget(self.SPX1OFF, 3, 16, 1, 2)
        self.ELEVATION = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.ELEVATION.setFont(font)
        self.ELEVATION.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.ELEVATION.setObjectName("ELEVATION")
        self.gridLayout_6.addWidget(self.ELEVATION, 27, 20, 1, 1)
        self.AZIMUTH = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.AZIMUTH.setFont(font)
        self.AZIMUTH.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.AZIMUTH.setObjectName("AZIMUTH")
        self.gridLayout_6.addWidget(self.AZIMUTH, 23, 20, 1, 1)
        self.Azim = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Azim.setFont(font)
        self.Azim.setStyleSheet("\n"
                                "color: rgb(255, 255, 0);")
        self.Azim.setObjectName("Azim")
        self.gridLayout_6.addWidget(self.Azim, 23, 21, 1, 1)
        self.SP2_Ro_2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Ro_2.setFont(font)
        self.SP2_Ro_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP2_Ro_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP2_Ro_2.setObjectName("SP2_Ro_2")
        self.gridLayout_6.addWidget(self.SP2_Ro_2, 32, 18, 1, 2)
        self.TEAM_ID = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.TEAM_ID.setFont(font)
        self.TEAM_ID.setStyleSheet("color: rgb(220, 220, 220);")
        self.TEAM_ID.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.TEAM_ID.setScaledContents(True)
        self.TEAM_ID.setAlignment(QtCore.Qt.AlignCenter)
        self.TEAM_ID.setObjectName("TEAM_ID")
        self.gridLayout_6.addWidget(self.TEAM_ID, 34, 20, 1, 2)
        self.SP1_Ro_2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_Ro_2.setFont(font)
        self.SP1_Ro_2.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP1_Ro_2.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP1_Ro_2.setObjectName("SP1_Ro_2")
        self.gridLayout_6.addWidget(self.SP1_Ro_2, 23, 18, 1, 2)
        self.C_Gt = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Gt.setFont(font)
        self.C_Gt.setStyleSheet("\n"
                                "color: rgb(255, 255, 0);")
        self.C_Gt.setObjectName("C_Gt")
        self.gridLayout_6.addWidget(self.C_Gt, 12, 21, 1, 1)
        self.Elev = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.Elev.setFont(font)
        self.Elev.setStyleSheet("\n"
                                "color: rgb(255, 255, 0);")
        self.Elev.setObjectName("Elev")
        self.gridLayout_6.addWidget(self.Elev, 27, 21, 1, 1)
        self.Currenttime = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.Currenttime.setFont(font)
        self.Currenttime.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.Currenttime.setObjectName("Currenttime")
        self.gridLayout_6.addWidget(self.Currenttime, 34, 7, 1, 1)
        self.SPX1ON = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SPX1ON.setFont(font)
        self.SPX1ON.setObjectName("SPX1ON")
        self.gridLayout_6.addWidget(self.SPX1ON, 2, 16, 1, 2)
        self.SIM_EN = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SIM_EN.setFont(font)
        self.SIM_EN.setObjectName("SIM_EN")
        self.gridLayout_6.addWidget(self.SIM_EN, 2, 21, 1, 1)
        self.line = QtWidgets.QFrame(self.tab_1)
        self.line.setStyleSheet("")
        self.line.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line.setLineWidth(5)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setObjectName("line")
        self.gridLayout_6.addWidget(self.line, 0, 15, 1, 7)
        self.SET_TIME = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SET_TIME.setFont(font)
        self.SET_TIME.setObjectName("SET_TIME")
        self.gridLayout_6.addWidget(self.SET_TIME, 2, 20, 1, 1)
        self.SPX2ON = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SPX2ON.setFont(font)
        self.SPX2ON.setObjectName("SPX2ON")
        self.gridLayout_6.addWidget(self.SPX2ON, 2, 18, 1, 2)
        self.SPX2OFF = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SPX2OFF.setFont(font)
        self.SPX2OFF.setObjectName("SPX2OFF")
        self.gridLayout_6.addWidget(self.SPX2OFF, 3, 18, 1, 2)
        self.SIM_AC = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SIM_AC.setFont(font)
        self.SIM_AC.setObjectName("SIM_AC")
        self.gridLayout_6.addWidget(self.SIM_AC, 3, 21, 1, 1)
        self.SIM_DIS = QtWidgets.QPushButton(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SIM_DIS.setFont(font)
        self.SIM_DIS.setObjectName("SIM_DIS")
        self.gridLayout_6.addWidget(self.SIM_DIS, 3, 20, 1, 1)
        self.logo = QtWidgets.QFrame(self.tab_1)
        self.logo.setStyleSheet("\n"
                                "image: url(Untitled-jhh1.png);")
        self.logo.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.logo.setFrameShadow(QtWidgets.QFrame.Raised)
        self.logo.setObjectName("logo")
        self.gridLayout_6.addWidget(self.logo, 28, 20, 5, 2)
        self.SP2_Packetcount = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Packetcount.setFont(font)
        self.SP2_Packetcount.setObjectName("SP2_Packetcount")
        self.gridLayout_6.addWidget(self.SP2_Packetcount, 28, 0, 1, 1)
        self.C_Gsats = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Gsats.setFont(font)
        self.C_Gsats.setObjectName("C_Gsats")
        self.gridLayout_6.addWidget(self.C_Gsats, 17, 20, 1, 1)
        self.State_cansat = QtWidgets.QProgressBar(self.tab_1)
        self.State_cansat.setStyleSheet("QProgressBar{\n"
                                        "    backgroundcolor:rgb(98,114,164);\n"
                                        "    color:rgb(200,200,200);\n"
                                        "    boder-style: none;\n"
                                        "    boder-radius: 10px;\n"
                                        "}\n"
                                        "QProgressBar::chunk{\n"
                                        "    border-radius: 10px;\n"
                                        "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                        "}")
        self.State_cansat.setMaximum(1)
        self.State_cansat.setProperty("value", 1)
        self.State_cansat.setTextVisible(False)
        self.State_cansat.setObjectName("State_cansat")
        self.gridLayout_6.addWidget(self.State_cansat, 2, 2, 1, 1)
        self.MODE = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setPointSize(16)
        self.MODE.setFont(font)
        self.MODE.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.MODE.setObjectName("MODE")
        self.gridLayout_6.addWidget(self.MODE, 4, 2, 1, 1)
        self.Cansat_realesed = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Cansat_realesed.setFont(font)
        self.Cansat_realesed.setAlignment(QtCore.Qt.AlignCenter)
        self.Cansat_realesed.setObjectName("Cansat_realesed")
        self.gridLayout_6.addWidget(self.Cansat_realesed, 3, 2, 1, 1)
        self.Mo = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.Mo.setFont(font)
        self.Mo.setObjectName("Mo")
        self.gridLayout_6.addWidget(self.Mo, 4, 3, 1, 4)
        self.SP1_released = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_released.setFont(font)
        self.SP1_released.setAlignment(QtCore.Qt.AlignCenter)
        self.SP1_released.setObjectName("SP1_released")
        self.gridLayout_6.addWidget(self.SP1_released, 3, 3, 1, 4)
        self.State_Sp1 = QtWidgets.QProgressBar(self.tab_1)
        self.State_Sp1.setStyleSheet("QProgressBar{\n"
                                     "    backgroundcolor:rgb(98,114,164);\n"
                                     "    color:rgb(200,200,200);\n"
                                     "    boder-style: none;\n"
                                     "    boder-radius: 10px;\n"
                                     "}\n"
                                     "QProgressBar::chunk{\n"
                                     "    border-radius: 10px;\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                     "}")
        self.State_Sp1.setMaximum(1)
        self.State_Sp1.setProperty("value", 1)
        self.State_Sp1.setTextVisible(False)
        self.State_Sp1.setObjectName("State_Sp1")
        self.gridLayout_6.addWidget(self.State_Sp1, 2, 3, 1, 4)
        self.Softwarestate = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.Softwarestate.setFont(font)
        self.Softwarestate.setStyleSheet("\n"
                                         "color: rgb(255, 79, 82);")
        self.Softwarestate.setAlignment(QtCore.Qt.AlignCenter)
        self.Softwarestate.setObjectName("Softwarestate")
        self.gridLayout_6.addWidget(self.Softwarestate, 0, 0, 1, 10)
        self.SP2_Temperature = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Temperature.setFont(font)
        self.SP2_Temperature.setObjectName("SP2_Temperature")
        self.gridLayout_6.addWidget(self.SP2_Temperature, 32, 7, 1, 3)
        self.SP2_T = PlotWidget(self.tab_1)
        self.SP2_T.setAutoFillBackground(False)
        self.SP2_T.setObjectName("SP2_T")
        self.gridLayout_6.addWidget(self.SP2_T, 27, 7, 5, 7)
        self.SP2_Rotation = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Rotation.setFont(font)
        self.SP2_Rotation.setObjectName("SP2_Rotation")
        self.gridLayout_6.addWidget(self.SP2_Rotation, 32, 14, 1, 4)
        self.SP1_Rotation = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_Rotation.setFont(font)
        self.SP1_Rotation.setObjectName("SP1_Rotation")
        self.gridLayout_6.addWidget(self.SP1_Rotation, 23, 14, 1, 4)
        self.SP2_Ro = PlotWidget(self.tab_1)
        self.SP2_Ro.setAutoFillBackground(False)
        self.SP2_Ro.setObjectName("SP2_Ro")
        self.gridLayout_6.addWidget(self.SP2_Ro, 27, 14, 5, 6)
        self.SP1_Ro = PlotWidget(self.tab_1)
        self.SP1_Ro.setAutoFillBackground(False)
        self.SP1_Ro.setObjectName("SP1_Ro")
        self.gridLayout_6.addWidget(self.SP1_Ro, 19, 14, 4, 6)
        self.Landed = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.Landed.setFont(font)
        self.Landed.setAlignment(QtCore.Qt.AlignCenter)
        self.Landed.setObjectName("Landed")
        self.gridLayout_6.addWidget(self.Landed, 3, 9, 1, 1)
        self.stat = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.stat.setFont(font)
        self.stat.setAlignment(QtCore.Qt.AlignCenter)
        self.stat.setObjectName("stat")
        self.stat.setStyleSheet("\n"
                                "color: rgb(235, 108, 228);")
        self.gridLayout_6.addWidget(self.stat, 3, 10, 1, 4)
        self.State_Land = QtWidgets.QProgressBar(self.tab_1)
        self.State_Land.setStyleSheet("QProgressBar{\n"
                                      "    backgroundcolor:rgb(98,114,164);\n"
                                      "    color:rgb(200,200,200);\n"
                                      "    boder-style: none;\n"
                                      "    boder-radius: 10px;\n"
                                      "}\n"
                                      "QProgressBar::chunk{\n"
                                      "    border-radius: 10px;\n"
                                      "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                      "}")
        self.State_Land.setMaximum(1)
        self.State_Land.setProperty("value", 1)
        self.State_Land.setTextVisible(False)
        self.State_Land.setObjectName("State_Land")
        self.gridLayout_6.addWidget(self.State_Land, 2, 9, 1, 1)
        self.State_Sp2 = QtWidgets.QProgressBar(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.State_Sp2.setFont(font)
        self.State_Sp2.setStyleSheet("QProgressBar{\n"
                                     "    backgroundcolor:rgb(98,114,164);\n"
                                     "    color:rgb(200,200,200);\n"
                                     "    boder-style: none;\n"
                                     "    boder-radius: 10px;\n"
                                     "}\n"
                                     "QProgressBar::chunk{\n"
                                     "    border-radius: 10px;\n"
                                     "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                     "}")
        self.State_Sp2.setMaximum(1)
        self.State_Sp2.setProperty("value", 1)
        self.State_Sp2.setTextVisible(False)
        self.State_Sp2.setObjectName("State_Sp2")
        self.gridLayout_6.addWidget(self.State_Sp2, 2, 7, 1, 1)
        self.C_Ga = PlotWidget(self.tab_1)
        self.C_Ga.setAutoFillBackground(False)
        self.C_Ga.setObjectName("C_Ga")
        self.gridLayout_6.addWidget(self.C_Ga, 11, 14, 6, 6)
        self.SP2_Released = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Released.setFont(font)
        self.SP2_Released.setAlignment(QtCore.Qt.AlignCenter)
        self.SP2_Released.setObjectName("SP2_Released")
        self.gridLayout_6.addWidget(self.SP2_Released, 3, 7, 1, 1)
        self.C_T = PlotWidget(self.tab_1)
        self.C_T.setAutoFillBackground(False)
        self.C_T.setObjectName("C_T")
        self.gridLayout_6.addWidget(self.C_T, 11, 7, 6, 7)
        self.C_Temperatue = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_Temperatue.setFont(font)
        self.C_Temperatue.setObjectName("C_Temperatue")
        self.gridLayout_6.addWidget(self.C_Temperatue, 17, 7, 1, 3)
        self.C_Gs = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Gs.setFont(font)
        self.C_Gs.setStyleSheet("\n"
                                "color: rgb(255, 255, 0);")
        self.C_Gs.setObjectName("C_Gs")
        self.gridLayout_6.addWidget(self.C_Gs, 17, 21, 1, 1)
        self.C_Glongtitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Glongtitude.setFont(font)
        self.C_Glongtitude.setObjectName("C_Glongtitude")
        self.gridLayout_6.addWidget(self.C_Glongtitude, 15, 20, 2, 1)
        self.C_Glo = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Glo.setFont(font)
        self.C_Glo.setStyleSheet("\n"
                                 "color: rgb(255, 255, 0);")
        self.C_Glo.setObjectName("C_Glo")
        self.gridLayout_6.addWidget(self.C_Glo, 15, 21, 2, 1)
        self.C_Glatitude_1 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Glatitude_1.setFont(font)
        self.C_Glatitude_1.setObjectName("C_Glatitude_1")
        self.gridLayout_6.addWidget(self.C_Glatitude_1, 13, 20, 2, 1)
        self.C_Gla = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Gla.setFont(font)
        self.C_Gla.setStyleSheet("\n"
                                 "color: rgb(255, 255, 0);")
        self.C_Gla.setObjectName("C_Gla")
        self.gridLayout_6.addWidget(self.C_Gla, 13, 21, 2, 1)
        self.Container = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Container.setFont(font)
        self.Container.setStyleSheet("\n"
                                     "color: rgb(255, 79, 82);")
        self.Container.setObjectName("Container")
        self.gridLayout_6.addWidget(self.Container, 11, 0, 1, 1)
        self.C_P = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_P.setFont(font)
        self.C_P.setObjectName("C_P")
        self.gridLayout_6.addWidget(self.C_P, 13, 0, 1, 1)
        self.C_Voltage = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_Voltage.setFont(font)
        self.C_Voltage.setObjectName("C_Voltage")
        self.gridLayout_6.addWidget(self.C_Voltage, 14, 0, 1, 1)
        self.C_V = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_V.setFont(font)
        self.C_V.setObjectName("C_V")
        self.gridLayout_6.addWidget(self.C_V, 15, 0, 1, 1)
        self.Payload1 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Payload1.setFont(font)
        self.Payload1.setStyleSheet("\n"
                                    "color: rgb(255, 79, 82);")
        self.Payload1.setObjectName("Payload1")
        self.gridLayout_6.addWidget(self.Payload1, 19, 0, 1, 1)
        self.SP1_RE = QtWidgets.QProgressBar(self.tab_1)
        self.SP1_RE.setStyleSheet("QProgressBar{\n"
                                  "    backgroundcolor:rgb(98,114,164);\n"
                                  "    color:rgb(200,200,200);\n"
                                  "    boder-style: none;\n"
                                  "    boder-radius: 10px;\n"
                                  "}\n"
                                  "QProgressBar::chunk{\n"
                                  "    border-radius: 10px;\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                  "}")
        self.SP1_RE.setMaximum(1)
        self.SP1_RE.setProperty("value", 1)
        self.SP1_RE.setTextVisible(False)
        self.SP1_RE.setObjectName("SP1_RE")
        self.gridLayout_6.addWidget(self.SP1_RE, 22, 0, 1, 1)
        self.SP1_P = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_P.setFont(font)
        self.SP1_P.setObjectName("SP1_P")
        self.gridLayout_6.addWidget(self.SP1_P, 21, 0, 1, 1)
        self.Payload2 = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(18)
        font.setBold(True)
        font.setUnderline(False)
        font.setWeight(75)
        self.Payload2.setFont(font)
        self.Payload2.setStyleSheet("\n"
                                    "color: rgb(255, 79, 82);")
        self.Payload2.setObjectName("Payload2")
        self.gridLayout_6.addWidget(self.Payload2, 27, 0, 1, 1)
        self.SP2_RE = QtWidgets.QProgressBar(self.tab_1)
        self.SP2_RE.setStyleSheet("QProgressBar{\n"
                                  "    backgroundcolor:rgb(98,114,164);\n"
                                  "    color:rgb(200,200,200);\n"
                                  "    boder-style: none;\n"
                                  "    boder-radius: 10px;\n"
                                  "}\n"
                                  "QProgressBar::chunk{\n"
                                  "    border-radius: 10px;\n"
                                  "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                  "}")
        self.SP2_RE.setMaximum(1)
        self.SP2_RE.setProperty("value", 1)
        self.SP2_RE.setTextVisible(False)
        self.SP2_RE.setObjectName("SP2_RE")
        self.gridLayout_6.addWidget(self.SP2_RE, 31, 0, 1, 1)
        self.SP2_P = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_P.setFont(font)
        self.SP2_P.setObjectName("SP2_P")
        self.gridLayout_6.addWidget(self.SP2_P, 30, 0, 1, 1)
        self.SP2_A = PlotWidget(self.tab_1)
        self.SP2_A.setAutoFillBackground(False)
        self.SP2_A.setObjectName("SP2_A")
        self.gridLayout_6.addWidget(self.SP2_A, 27, 1, 5, 6)
        self.SP1_A = PlotWidget(self.tab_1)
        self.SP1_A.setAutoFillBackground(False)
        self.SP1_A.setObjectName("SP1_A")
        self.gridLayout_6.addWidget(self.SP1_A, 19, 1, 4, 6)
        self.C_A = PlotWidget(self.tab_1)
        self.C_A.setAutoFillBackground(False)
        self.C_A.setObjectName("C_A")
        self.gridLayout_6.addWidget(self.C_A, 11, 1, 6, 6)
        self.C_Altitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_Altitude.setFont(font)
        self.C_Altitude.setObjectName("C_Altitude")
        self.gridLayout_6.addWidget(self.C_Altitude, 17, 1, 1, 1)
        self.SP1_Altitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_Altitude.setFont(font)
        self.SP1_Altitude.setObjectName("SP1_Altitude")
        self.gridLayout_6.addWidget(self.SP1_Altitude, 23, 1, 1, 1)
        self.SP2_Altitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_Altitude.setFont(font)
        self.SP2_Altitude.setObjectName("SP2_Altitude")
        self.gridLayout_6.addWidget(self.SP2_Altitude, 32, 1, 1, 1)
        self.SP2_alt = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_alt.setFont(font)
        self.SP2_alt.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP2_alt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP2_alt.setObjectName("SP2_alt")
        self.gridLayout_6.addWidget(self.SP2_alt, 32, 2, 1, 5)
        self.SP1_alt = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_alt.setFont(font)
        self.SP1_alt.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP1_alt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP1_alt.setObjectName("SP1_alt")
        self.gridLayout_6.addWidget(self.SP1_alt, 23, 2, 1, 5)
        self.C_alt = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_alt.setFont(font)
        self.C_alt.setStyleSheet("color: rgb(255, 255, 0);")
        self.C_alt.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.C_alt.setObjectName("C_alt")
        self.gridLayout_6.addWidget(self.C_alt, 17, 2, 1, 5)
        self.line_2 = QtWidgets.QFrame(self.tab_1)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Plain)
        self.line_2.setLineWidth(5)
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setObjectName("line_2")
        self.gridLayout_6.addWidget(self.line_2, 10, 0, 1, 22)
        self.copyright = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(6)
        font.setBold(True)
        font.setWeight(75)
        self.copyright.setFont(font)
        self.copyright.setObjectName("copyright")
        self.gridLayout_6.addWidget(self.copyright, 34, 13, 1, 7)
        self.SP2_temp = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP2_temp.setFont(font)
        self.SP2_temp.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP2_temp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP2_temp.setObjectName("SP2_temp")
        self.gridLayout_6.addWidget(self.SP2_temp, 32, 10, 1, 4)
        self.SP1_temp = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.SP1_temp.setFont(font)
        self.SP1_temp.setStyleSheet("color: rgb(255, 255, 0);")
        self.SP1_temp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.SP1_temp.setObjectName("SP1_temp")
        self.gridLayout_6.addWidget(self.SP1_temp, 23, 10, 1, 4)
        self.C_temp = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_temp.setFont(font)
        self.C_temp.setStyleSheet("color: rgb(255, 255, 0);")
        self.C_temp.setAlignment(QtCore.Qt.AlignRight | QtCore.Qt.AlignTrailing | QtCore.Qt.AlignVCenter)
        self.C_temp.setObjectName("C_temp")
        self.gridLayout_6.addWidget(self.C_temp, 17, 10, 1, 4)
        self.C_GpsAltitude = QtWidgets.QLabel(self.tab_1)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.C_GpsAltitude.setFont(font)
        self.C_GpsAltitude.setObjectName("C_GpsAltitude")
        self.gridLayout_6.addWidget(self.C_GpsAltitude, 17, 14, 1, 4)
        self.C_Re = QtWidgets.QProgressBar(self.tab_1)
        self.C_Re.setStyleSheet("QProgressBar{\n"
                                "    backgroundcolor:rgb(98,114,164);\n"
                                "    color:rgb(200,200,200);\n"
                                "    boder-style: none;\n"
                                "    boder-radius: 10px;\n"
                                "}\n"
                                "QProgressBar::chunk{\n"
                                "    border-radius: 10px;\n"
                                "    background-color: qlineargradient(spread:pad, x1:0,y1:0.511364,x2:1,y2:0.523,stop:0 rgba(254,121,199,255),stop:1 rgba(170,85,255,255))\n"
                                "}")
        self.C_Re.setMaximum(1)
        self.C_Re.setProperty("value", 1)
        self.C_Re.setTextVisible(False)
        self.C_Re.setObjectName("C_Re")
        self.gridLayout_6.addWidget(self.C_Re, 16, 0, 1, 1)
        self.tabWidget.addTab(self.tab_1, "")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.C_Map = QtWebEngineWidgets.QWebEngineView(self.tab)
        self.C_Map.setUrl(QtCore.QUrl("about:blank"))
        self.C_Map.setObjectName("C_Map")
        self.gridLayout.addWidget(self.C_Map, 0, 0, 2, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.C_table = QtWidgets.QTableWidget(self.tab_2)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.C_table.setFont(font)
        self.C_table.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.C_table.setStyleSheet("\n"
                                   "color: rgb(255, 255, 0);")
        self.C_table.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.C_table.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.C_table.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.C_table.setRowCount(1)
        self.C_table.setColumnCount(19)
        self.C_table.setObjectName("C_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        self.C_table.setItem(0, 6, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 7, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 8, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 9, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 10, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 11, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 12, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 13, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 14, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 15, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 16, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 17, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.C_table.setItem(0, 18, item)
        self.C_table.horizontalHeader().setVisible(False)
        self.C_table.horizontalHeader().setCascadingSectionResizes(True)
        self.C_table.horizontalHeader().setDefaultSectionSize(200)
        self.C_table.horizontalHeader().setStretchLastSection(True)
        self.C_table.verticalHeader().setVisible(False)
        self.gridLayout_4.addWidget(self.C_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_3)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.S1_table = QtWidgets.QTableWidget(self.tab_3)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S1_table.setFont(font)
        self.S1_table.setStyleSheet("\n"
                                    "color: rgb(255, 255, 0);")
        self.S1_table.setRowCount(1)
        self.S1_table.setColumnCount(7)
        self.S1_table.setObjectName("S1_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S1_table.setItem(0, 6, item)
        self.S1_table.horizontalHeader().setVisible(False)
        self.S1_table.horizontalHeader().setDefaultSectionSize(200)
        self.S1_table.horizontalHeader().setHighlightSections(False)
        self.S1_table.verticalHeader().setVisible(False)
        self.gridLayout_2.addWidget(self.S1_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_3, "")
        self.tab_4 = QtWidgets.QWidget()
        self.tab_4.setObjectName("tab_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.tab_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.S2_table = QtWidgets.QTableWidget(self.tab_4)
        font = QtGui.QFont()
        font.setFamily("Sukhumvit Set")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.S2_table.setFont(font)
        self.S2_table.setStyleSheet("\n"
                                    "color: rgb(255, 255, 0);")
        self.S2_table.setRowCount(1)
        self.S2_table.setColumnCount(7)
        self.S2_table.setObjectName("S2_table")
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 0, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 1, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 2, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 3, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 4, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 5, item)
        item = QtWidgets.QTableWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignCenter)
        self.S2_table.setItem(0, 6, item)
        self.S2_table.horizontalHeader().setVisible(False)
        self.S2_table.horizontalHeader().setDefaultSectionSize(200)
        self.S2_table.verticalHeader().setVisible(False)
        self.gridLayout_3.addWidget(self.S2_table, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_4, "")
        self.gridLayout_5.addWidget(self.tabWidget, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 2123, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionsave = QtWidgets.QAction(MainWindow)
        self.actionsave.setObjectName("actionsave")
        # Button function zone
        self.Start.clicked.connect(self.startp)
        self.mqttactivation.clicked.connect(self.activemqtt)
        self.refresh.clicked.connect(self.clear)
        self.CXON.clicked.connect(self.cxon)
        self.CXOFF.clicked.connect(self.cxoff)
        self.SPX1ON.clicked.connect(self.sp1on)
        self.SPX1OFF.clicked.connect(self.sp1off)
        self.SPX2ON.clicked.connect(self.sp2on)
        self.SPX2OFF.clicked.connect(self.sp2off)
        self.SET_TIME.clicked.connect(self.settime)
        self.SIM_DIS.clicked.connect(self.simdisable)
        self.SIM_EN.clicked.connect(self.simenable)
        self.SIM_AC.clicked.connect(self.simactivate)
        self.SIMPRESSURE.clicked.connect(self.simpressure)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.refreshport()
        self.defineValue()
        self.mqttsv = mqtt.Initialise_client()
        self.ismqtt = False

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "SPOROS#3751::GROUNDSTATION"))
        self.SP1_Temperature.setText(_translate("MainWindow", "TEMPERATURE (C)"))
        self.TimeElapsed.setText(_translate("MainWindow", "HH:MM:SS.ms"))
        self.PC_Latitude.setText(_translate("MainWindow", "Latitude"))
        self.PC_GIS.setText(_translate("MainWindow", "<html><head/><body><p>GROUND STATION</p></body></html>"))
        self.PC_lon.setText(_translate("MainWindow", "-"))
        self.PC_Longtitude.setText(_translate("MainWindow", "Longtitude"))
        self.PC_Gd.setText(_translate("MainWindow", "-"))
        self.PC_la.setText(_translate("MainWindow", "-"))
        self.PC_Gnddis.setText(_translate("MainWindow", "Ground distance:"))
        self.C_GIS.setText(_translate("MainWindow", "<strong>CONTAINER"))
        self.command_t.setText(_translate("MainWindow", "COMMAND"))
        self.mqttactivation.setText(_translate("MainWindow", "MQTT ON"))
        self.SP1_Packetcount.setText(_translate("MainWindow", "Packetcount"))
        self.PORTSelecter.setItemText(0, _translate("MainWindow", "COM 11"))
        self.Launched.setText(_translate("MainWindow", "Launched"))
        self.PORT.setText(_translate("MainWindow", "PORT"))
        self.Time.setText(_translate("MainWindow", "HH:MM:SS.ms"))
        self.Prelaunch.setText(_translate("MainWindow", "Prelaunch"))
        self.SIMPRESSURE.setText(_translate("MainWindow", "SIM PRESSURE"))
        self.C_Galt.setText(_translate("MainWindow", "-"))
        self.C_echo.setText(_translate("MainWindow", "-"))
        self.Start.setText(_translate("MainWindow", "Start"))
        self.ELAPSED.setText(_translate("MainWindow", "ELAPSED:"))
        self.C_Packetcount.setText(_translate("MainWindow", "Packetcount"))
        self.label.setText(_translate("MainWindow", "GPS Time:"))
        self.refresh.setText(_translate("MainWindow", "Refresh"))
        self.CXOFF.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.CXOFF.setText(_translate("MainWindow", "CX OFF"))
        self.Lastcommand_t.setText(_translate("MainWindow", "LAST COMMAND SEND:"))
        self.CXON.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.CXON.setText(_translate("MainWindow", "CX ON"))
        self.SPX1OFF.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SPX1OFF.setText(_translate("MainWindow", "PAYLOAD1 OFF"))
        self.ELEVATION.setText(_translate("MainWindow", "ELEVATION:"))
        self.AZIMUTH.setText(_translate("MainWindow", "AZIMUTH:"))
        self.Azim.setText(_translate("MainWindow", "-"))
        self.SP2_Ro_2.setText(_translate("MainWindow", "-"))
        self.TEAM_ID.setText(_translate("MainWindow", "<STRONG>SPOROS #3751"))
        self.SP1_Ro_2.setText(_translate("MainWindow", "-"))
        self.C_Gt.setText(_translate("MainWindow", "-"))
        self.Elev.setText(_translate("MainWindow", "-"))
        self.Currenttime.setText(_translate("MainWindow", "TIME:"))
        self.SPX1ON.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SPX1ON.setText(_translate("MainWindow", "PAYLOAD1 ON"))
        self.SIM_EN.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SIM_EN.setText(_translate("MainWindow", "SIM ENABLE"))
        self.SET_TIME.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SET_TIME.setText(_translate("MainWindow", "SET TIME"))
        self.SPX2ON.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SPX2ON.setText(_translate("MainWindow", "PAYLOAD2 ON"))
        self.SPX2OFF.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SPX2OFF.setText(_translate("MainWindow", "PAYLOAD2 OFF"))
        self.SIM_AC.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SIM_AC.setText(_translate("MainWindow", "SIM ACTIVATE"))
        self.SIM_DIS.setStyleSheet(_translate("MainWindow", "background-color: rgb(98, 114, 164);"))
        self.SIM_DIS.setText(_translate("MainWindow", "SIM DISABLE"))
        self.SP2_Packetcount.setText(_translate("MainWindow", "Packetcount"))
        self.C_Gsats.setText(_translate("MainWindow", "Sats:"))
        self.MODE.setText(_translate("MainWindow", "MODE:"))
        self.Cansat_realesed.setText(_translate("MainWindow", "Cansat released"))
        self.Mo.setStyleSheet(_translate("MainWindow", "\n"
                                                       "color: rgb(255, 255, 0);"))
        self.Mo.setText(_translate("MainWindow", "FLIGHT"))
        self.SP1_released.setText(_translate("MainWindow", "SP1_released"))
        self.Softwarestate.setText(_translate("MainWindow", "Software State"))
        self.SP2_Temperature.setText(_translate("MainWindow", "TEMPERATURE (C)"))
        self.SP2_Rotation.setText(_translate("MainWindow", "ROTATION RATE(rpm)"))
        self.SP1_Rotation.setText(_translate("MainWindow", "ROTATION RATE(rpm)"))
        self.Landed.setText(_translate("MainWindow", "Landed"))
        self.stat.setText(_translate("MainWindow", "stat"))
        self.SP2_Released.setText(_translate("MainWindow", "SP2_released"))
        self.C_Temperatue.setText(_translate("MainWindow", "TEMPERATURE (C)"))
        self.C_Gs.setText(_translate("MainWindow", "-"))
        self.C_Glongtitude.setText(_translate("MainWindow", "Longtitude"))
        self.C_Glo.setText(_translate("MainWindow", "-"))
        self.C_Glatitude_1.setText(_translate("MainWindow", "Latitude"))
        self.C_Gla.setText(_translate("MainWindow", "-"))
        self.Container.setText(_translate("MainWindow", "<html><head/><body><p>CONTAINER</p></body></html>"))
        self.C_P.setStyleSheet(_translate("MainWindow", "\n"
                                                        "color: rgb(255, 255, 0);"))
        self.C_P.setText(_translate("MainWindow", "-"))
        self.C_Voltage.setText(_translate("MainWindow", "Voltage"))
        self.C_V.setStyleSheet(_translate("MainWindow", "\n"
                                                        "color: rgb(255, 255, 0);"))
        self.C_V.setText(_translate("MainWindow", "-"))
        self.Payload1.setText(_translate("MainWindow", "<STRONG>PAYLOAD1"))
        self.SP1_P.setStyleSheet(_translate("MainWindow", "\n"
                                                          "color: rgb(255, 255, 0);"))
        self.SP1_P.setText(_translate("MainWindow", "-"))
        self.Payload2.setText(_translate("MainWindow", "<STRONG>PAYLOAD2"))
        self.SP2_P.setStyleSheet(_translate("MainWindow", "\n"
                                                          "color: rgb(255, 255, 0);"))
        self.SP2_P.setText(_translate("MainWindow", "-"))
        self.C_Altitude.setText(_translate("MainWindow", "ALTITUDE (m)"))
        self.SP1_Altitude.setText(_translate("MainWindow", "ALTITUDE (m)"))
        self.SP2_Altitude.setText(_translate("MainWindow", "ALTITUDE (m)"))
        self.SP2_alt.setText(_translate("MainWindow", "-"))
        self.SP1_alt.setText(_translate("MainWindow", "-"))
        self.C_alt.setText(_translate("MainWindow", "-"))
        self.copyright.setText(
            _translate("MainWindow", "USA CANSAT 2021 Groundcontrol station interface ver 0.1.0,Space AC"))
        self.SP2_temp.setText(_translate("MainWindow", "-"))
        self.SP1_temp.setText(_translate("MainWindow", "-"))
        self.C_temp.setText(_translate("MainWindow", "-"))
        self.C_GpsAltitude.setText(_translate("MainWindow", "GPS_ALTITUDE (m)"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_1), _translate("MainWindow", "MAIN"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "MAP"))
        __sortingEnabled = self.C_table.isSortingEnabled()
        self.C_table.setSortingEnabled(False)
        item = self.C_table.item(0, 0)
        item.setText(_translate("MainWindow", "TEAM_ID"))
        item = self.C_table.item(0, 1)
        item.setText(_translate("MainWindow", "MISSION_TIME"))
        item = self.C_table.item(0, 2)
        item.setText(_translate("MainWindow", "PACKETCOUNT"))
        item = self.C_table.item(0, 3)
        item.setText(_translate("MainWindow", "PACKET_TYPE"))
        item = self.C_table.item(0, 4)
        item.setText(_translate("MainWindow", "MODE"))
        item = self.C_table.item(0, 5)
        item.setText(_translate("MainWindow", "SP1_RELEASED"))
        item = self.C_table.item(0, 6)
        item.setText(_translate("MainWindow", "SP2_RELEASED"))
        item = self.C_table.item(0, 7)
        item.setText(_translate("MainWindow", "ALTITUDE"))
        item = self.C_table.item(0, 8)
        item.setText(_translate("MainWindow", "TEMP"))
        item = self.C_table.item(0, 9)
        item.setText(_translate("MainWindow", "VOLTAGE"))
        item = self.C_table.item(0, 10)
        item.setText(_translate("MainWindow", "GPS_TIME"))
        item = self.C_table.item(0, 11)
        item.setText(_translate("MainWindow", "GPS_LATITUDE"))
        item = self.C_table.item(0, 12)
        item.setText(_translate("MainWindow", "GPS_LONGTITUDE"))
        item = self.C_table.item(0, 13)
        item.setText(_translate("MainWindow", "GPS_ALTITUDE"))
        item = self.C_table.item(0, 14)
        item.setText(_translate("MainWindow", "GPS_SATS"))
        item = self.C_table.item(0, 15)
        item.setText(_translate("MainWindow", "SW_STATE"))
        item = self.C_table.item(0, 16)
        item.setText(_translate("MainWindow", "SP1_PACKETCOUNT"))
        item = self.C_table.item(0, 17)
        item.setText(_translate("MainWindow", "SP2PACKETCOUNT"))
        item = self.C_table.item(0, 18)
        item.setText(_translate("MainWindow", "CMD_ECHO"))
        self.C_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "CDATA"))
        __sortingEnabled = self.S1_table.isSortingEnabled()
        self.S1_table.setSortingEnabled(False)
        item = self.S1_table.item(0, 0)
        item.setText(_translate("MainWindow", "TEAMID"))
        item = self.S1_table.item(0, 1)
        item.setText(_translate("MainWindow", "MISSIONTIME"))
        item = self.S1_table.item(0, 2)
        item.setText(_translate("MainWindow", "PACKETCOUNT"))
        item = self.S1_table.item(0, 3)
        item.setText(_translate("MainWindow", "PACKETTYPE"))
        item = self.S1_table.item(0, 4)
        item.setText(_translate("MainWindow", "ALTITUDE"))
        item = self.S1_table.item(0, 5)
        item.setText(_translate("MainWindow", "TEMP"))
        item = self.S1_table.item(0, 6)
        item.setText(_translate("MainWindow", "ROTATION"))
        self.S1_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "SP1DATA"))
        __sortingEnabled = self.S2_table.isSortingEnabled()
        self.S2_table.setSortingEnabled(False)
        item = self.S2_table.item(0, 0)
        item.setText(_translate("MainWindow", "TEAMID"))
        item = self.S2_table.item(0, 1)
        item.setText(_translate("MainWindow", "MISSIONTIME"))
        item = self.S2_table.item(0, 2)
        item.setText(_translate("MainWindow", "PACKETCOUNT"))
        item = self.S2_table.item(0, 3)
        item.setText(_translate("MainWindow", "PACKETTYPE"))
        item = self.S2_table.item(0, 4)
        item.setText(_translate("MainWindow", "ALTITUDE"))
        item = self.S2_table.item(0, 5)
        item.setText(_translate("MainWindow", "TEMP"))
        item = self.S2_table.item(0, 6)
        item.setText(_translate("MainWindow", "ROTATION"))
        self.S2_table.setSortingEnabled(__sortingEnabled)
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "SP2DATA"))
        self.actionsave.setText(_translate("MainWindow", "save"))

    def startp(self):
        try:
            print("[startclicked]")
            self.State_Prelaunch.setProperty("value", 0)
            self.State_launch.setProperty("value", 0)
            self.State_cansat.setProperty("value", 0)
            self.State_Sp1.setProperty("value", 0)
            self.State_Sp2.setProperty("value", 0)
            self.State_Land.setProperty("value", 0)
            self.SP1_RE.setProperty("value", 0)
            self.SP2_RE.setProperty("value", 0)
            self.getvalue()
            self.ismqtt = False
        except:
            pass

    def connectport(self):
        try:
            self.devicecom = self.PORTSelecter.currentText()
            self.device = Datahandle.connect(self.devicecom)
            print(f"CONNECTING TO {self.devicecom} ...")
            print(self.device)
            self.stat.setText(f"CNT{self.devicecom}")
        except:
            print('ALREADY CONNECTED AT: ' + self.devicecom)
        finally:
            self.refreshport()

    def activemqtt(self, Data):
        if self.ismqtt:
            self.mqttactivation.setText("MQTT ON")
            self.stat.setText("MQTTOFF")
            try:
                self.stat.setText("MQTT S")
                mqtt.sendserver(self.mqttsv,Data)

            except:
                self.stat.setText("MQTT F")
                pass
            self.ismqtt = False
        else:
            self.mqttactivation.setText("MQTT OFF")
            self.stat.setText("MQTTON")
            self.ismqtt = True

    def refreshport(self):
        self.PORTSelecter.clear()
        for comlist in Datahandle.comlist():
            self.PORTSelecter.addItem(comlist)

    def clear(self):
        self.C_A.clear()
        self.C_T.clear()
        self.C_Ga.clear()
        self.SP1_A.clear()
        self.SP1_T.clear()
        self.SP1_Ro.clear()
        self.SP2_A.clear()
        self.SP2_T.clear()
        self.SP2_Ro.clear()

    def cxon(self):
        self.sendcommand('CX', 'ON')

    def cxoff(self):
        self.sendcommand('CX', 'OFF')

    def sp1on(self):
        self.sendcommand('SP1X', 'ON')

    def sp1off(self):
        self.sendcommand('SP1X', 'OFF')

    def sp2on(self):
        self.sendcommand('SP2X', 'ON')

    def sp2off(self):
        self.sendcommand('SP2X', 'OFF')

    def settime(self):
        ti = RTC.ST()
        self.sendcommand("ST", ti)

    def simdisable(self):
        self.sendcommand('SIM', 'DISABLE')

    def simenable(self):
        self.sendcommand('SIM', 'ENABLE')

    def simactivate(self):
        self.sendcommand('SIM', 'ACTIVATE')

    def simpressure(self):
        try:
            pressure = self.PRESSURE_INPUT.text()
            self.PRESSURE_INPUT.clear()
            self.sendcommand("SIMP", pressure)
            pass
        except:
            pass

    def sendcommand(self, cmdtype, cmd):
        if cmdtype == "SIMP":
            CMD.sim(cmdtype, cmd)
        else:
            CMD.sendcmd(self.device, cmdtype, cmd)

        # Normal function

    def defineValue(self):
        self.b = []
        self.c = []
        self.h = []
        self.i = []
        self.n = []
        self.q = []
        self.r = []
        self.t = []
        self.u = []
        self.v = []
        self.w = []
        self.x = []
        self.y = []
        self.coord = []

    def updatevalue(self, data):
        if data[3] == 'C':
            A = data[0]  # TEAMID
            B = data[1]  # Time
            C = data[2]  # pkgcount
            D = data[3]  # pkgtype
            E = data[4]  # mode
            F = data[5]  # sp1r
            G = data[6]  # sp2r
            H = data[7]  # alt
            I = data[8]  # temp
            J = data[9]  # voltage
            K = data[10]  # gpstime
            L = data[11]  # lat
            M = data[12]  # lon
            N = data[13]  # Galt
            O = data[14]  # Gsats
            P = data[15]  # sw state
            Q = data[16]  # sp1 count
            R = data[17]  # sp2count
            S = data[18]  # echo
            self.updatetable(self.C_table, [A, B, C, D, E, F, G, H, I, J, K, L, M, N, O, P, Q, R, S])
            F = 0 if F != 'R' else 1
            G = 0 if G != 'R' else 1
            E = 'FLIGHT' if E == 'F' else 'SIMULATION'
            if self.isplot(C):  # packet count
                self.c.append(float(C))
            if self.isplot(H):  # altitude
                self.h.append(float(H))
            if self.isplot(I):  # Temp
                self.i.append(float(I))
            if self.isplot(N):  # GPSALTUTYDE
                self.n.append(float(N))
            if self.isplot(L) and self.isplot(M):
                self.coord.append((float(L), float(M)))
            self.lat1 = L
            self.lon1 = M
            self.a1 = N
            self.C_echo.setText(S)
            self.C_P.setText(C)
            self.C_V.setText(J)
            self.C_alt.setText(H)
            self.C_temp.setText(I)
            self.C_Galt.setText(N)
            self.C_Gt.setText(K)
            self.C_Gt.setText(K)
            self.C_Gs.setText(O)
            self.C_Gla.setText(L)
            self.C_Glo.setText(M)
            self.Mo.setText(E)
            if P == 'PRELAUNCH':
                self.State_Prelaunch.setProperty("value", 1)
            if P == 'LAUNCH':
                self.State_launch.setProperty("value", 1)
            if P == 'CANSATRELEASED':
                self.State_cansat.setProperty("value", 1)
            if P == 'SP1RELEASED':
                self.State_Sp1.setProperty("value", 1)
            if P == 'SP2RELEASED':
                self.State_Sp2.setProperty("value", 1)
            if P == 'LAND':
                self.State_Land.setProperty("value", 1)
            self.SP1_RE.setProperty("value", F)
            self.SP2_RE.setProperty("value", G)
            self.updategraph()
            self.updateMap()
            try:
                self.compass()
            except:
                pass

    def updatevalue2(self, data):
        if data[3] == 'S1':
            A = data[0]
            B = data[1]
            Q = data[2]
            D = data[3]
            T = data[4]
            U = data[5]
            V = data[6]
            if self.isplot(Q):  # packet count
                self.q.append(float(Q))
            if self.isplot(T):  # SP1ALTITUDE
                self.t.append(float(T))
            if self.isplot(U):  # SP1TEMP
                self.u.append(float(U))
            if self.isplot(V):  # SP1ROTATION
                self.v.append(float(V))
            self.SP1_P.setText(Q)
            self.SP1_alt.setText(T)
            self.SP1_temp.setText(U)
            self.SP1_Ro_2.setText(V)
            self.updatetable(self.S1_table, [A, B, Q, D, T, U, V])
            self.updategraph()

    def updatevalue3(self, data):
        if data[3] == 'S2':
            A = data[0]
            B = data[1]
            R = data[2]
            D = data[3]
            W = data[4]
            X = data[5]
            Y = data[6]
            if self.isplot(R):  # packet count
                self.r.append(float(R))
            if self.isplot(W):  # SP2ALTITUDE
                self.w.append(float(W))
            if self.isplot(X):  # SP2TEMP
                self.x.append(float(X))
            if self.isplot(Y):  # SP2ROTATION
                self.y.append(float(Y))

            self.SP2_P.setText(R)
            self.SP2_alt.setText(W)
            self.SP2_temp.setText(X)
            self.SP2_Ro_2.setText(Y)
            self.updatetable(self.S2_table, [A, B, R, D, W, X, Y])

        self.updategraph()

    def updatevaluePC(self, data):
        if data[1] == 'P':
            C = data[2]  # Lat
            D = data[3]  # Lon
            E = data[4]  # alt
            F = data[5]  # orx
            G = data[6]  # ory
            H = data[7]  # orz
            self.stp = (float(C), float(D))
            self.PC_la.setText(C)
            self.PC_lon.setText(D)
            self.lat2 = C
            self.lon2 = D
            self.a2 = E
            self.gx = F
            self.gy = G
            self.gz = H
            try:
                self.compass()
            except:
                pass

    def compass(self):
        self.gyro = GNSS.coord(self.lat2, self.lon2, self.lat1, self.lon1, self.a2, self.a1, self.gx, self.gy, self.gz)
        print("compass")
        self.dist = self.gyro.dist()
        self.elevation = self.gyro.elevation()
        self.azimuth = self.gyro.azimuth()
        self.PC_Gd.setText(str(self.dist))
        self.Azim.setText(str(self.elevation))
        self.Elev.setText(str(self.azimuth))

    def updateMap(self):
        try:
            dt = map.getmap(self.stp, self.coord, self.h)
            self.C_Map.setHtml(dt.getvalue().decode())
            print("update map")
        except:
            pass

    def updategraph(self):
        # container graph
        print("updating graph")
        try:
            self.drawgraph(self.C_A, self.c, self.h)
            self.drawgraph(self.C_T, self.c, self.i)
            self.drawgraph(self.C_Ga, self.c, self.n)
            # sp1 graph
            self.drawgraph(self.SP1_A, self.q, self.t)
            self.drawgraph(self.SP1_T, self.q, self.u)
            self.drawgraph(self.SP1_Ro, self.q, self.v)
            # sp2 graph
            self.drawgraph(self.SP2_A, self.r, self.w)
            self.drawgraph(self.SP2_T, self.r, self.x)
            self.drawgraph(self.SP2_Ro, self.r, self.y)
        except:
            pass

    def updatetable(self, table, toadd):
        totalrow = table.rowCount()
        table.setRowCount(totalrow + 1)
        for col, data in enumerate(toadd):
            if data != 'N/A': self.addtableitem(table, totalrow, col, data)

    @staticmethod
    def addtableitem(table, row, column, value):
        table.setItem(row, column, QTableWidgetItem(value))

    @staticmethod
    def drawgraph(graphno, x, y):
        try:
            graphno.plot(x, y)
        except:
            pass

    @staticmethod
    def isplot(x):
        if x != 'N/A':
            return True
        else:
            return False

    def updateTime(self, time):
        self.Time.setText(time)

    def updateElaps(self, elaps):
        self.TimeElapsed.setText(elaps)

    def getvalue(self):

        self.connectport()

        self.worker1 = ThreadClass1(comport=self.devicecom, device=self.device)
        self.worker2 = ThreadClass2()
        self.worker1.carrier1.connect(self.updatevalue)
        self.worker1.carrier2.connect(self.updatevalue2)
        self.worker1.carrier3.connect(self.updatevalue3)
        self.worker1.carrier4.connect(self.updatevaluePC)
        self.worker2.carrier5.connect(self.updateTime)
        self.worker2.carrier6.connect(self.updateElaps)
        self.worker1.carrier7.connect(self.activemqtt)

        try:
            self.worker1.terminate()
        except:
            pass

        self.worker1.start()

        try:
            self.worker2.terminate()
        except:
            pass

        self.worker2.start()


class ThreadClass1(QThread):
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)
    carrier3 = QtCore.pyqtSignal(object)
    carrier4 = QtCore.pyqtSignal(object)
    carrier7 = QtCore.pyqtSignal(object)

    def __init__(self, comport, device, parent=None):
        super(ThreadClass1, self).__init__(parent)
        self.comport = comport
        self.device = device
        self.i = 0

    def __del__(self):
        self.wait()

    def run(self):
        print('[T1START]')
        while True:
            self.pkg = Datahandle.reading(self.device, self.i)
            print(self.pkg)
            PT = self.pkg[3]
            self.carrier7.emit(self.pkg)
            if PT == 'C':
                print('[CONTAINER]')
                self.pkg1 = self.pkg
                self.carrier1.emit(self.pkg1)
            elif PT == 'S1':
                print("[SP1]")
                self.pkg2 = self.pkg
                self.carrier2.emit(self.pkg2)
            elif PT == 'S2':
                print('[SP2]')
                self.pkg3 = self.pkg
                self.carrier3.emit(self.pkg3)
            elif self.pkg[1] == 'P':
                print('[PC]')
                self.pkg4 = self.pkg
                self.carrier4.emit(self.pkg4)
            else:
                pass
            self.i += 1

    def stop(self):
        self._isRunning = False


class ThreadClass2(QThread):
    carrier5 = QtCore.pyqtSignal(object)
    carrier6 = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        super(ThreadClass2, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        print('[T2 STARTED]')
        RTC.settime()
        while True:
            self.mytime = RTC.timenow()
            self.missiontime = RTC.elapstime()
            self.carrier5.emit(self.mytime)
            self.carrier6.emit(self.missiontime)


class Controller:
    def show(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        print('WINDOW OPENED!')


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Controller = Controller()
    Controller.show()
    sys.exit(app.exec_())
