from UI_Function import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from UI_main import Ui_MainWindow
import threading
from UI_splashscreen import Ui_MainWindow as UI_splashscreen

from RTC import GetTime
from pyqtgraph import PlotWidget

import web
import maps
import Datahandle
import mqtt
import time
import serial
import os

GLOBAL_SPLASH_COUNTER = 0


class MainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.setpg()
        self.ui.setupUi(self)
        self.connect_btn()
        self.clear()
        self.refresh()
        self.port = Datahandle.Port(self.ui.Portlist.currentText())

        def move_window(event):
            if UiFunctions.return_status(self) == 1:
                UiFunctions.maximize_restore(self)

            if event.buttons() == Qt.LeftButton:
                self.move(self.pos() + event.globalPos() - self.dragPos)
                self.dragPos = event.globalPos()
                event.accept()

        self.ui.TitleBar.mouseMoveEvent = move_window
        UiFunctions.ui_definitions(self)
        self.show()

    def mousePressEvent(self, event):
        self.dragPos = event.globalPos()

    def connect_btn(self):
        file = 'sim.txt'
        self.ui.filename.setText(file)
        self.ui.btn_refresh.clicked.connect(self.refresh)
        self.ui.btn_connect.clicked.connect(self.connect)
        self.ui.btn_mqtt.clicked.connect(self.thread2)
        self.ui.btn_clear.clicked.connect(Window.clear)
        self.ui.btn_map.clicked.connect(Window.update_map)

        self.ui.btn_s1on.clicked.connect(lambda: self.sendcmd('SP1X', 'ON'))
        self.ui.btn_s1off.clicked.connect(lambda: self.sendcmd('SP1X', 'OFF'))
        self.ui.btn_sp2on.clicked.connect(lambda: self.sendcmd('SP2X', 'ON'))
        self.ui.btn_s2off.clicked.connect(lambda: self.sendcmd('SP2X', 'OFF'))
        self.ui.btn_cxon.clicked.connect(lambda: self.sendcmd('CX', 'ON'))
        self.ui.btn_cxoff.clicked.connect(lambda: self.sendcmd('CX', 'OFF'))
        self.ui.btn_simactivate.clicked.connect(lambda: self.sendcmd('SIM', 'ACTIVATE'))
        self.ui.btn_simenable.clicked.connect(lambda: self.sendcmd('SIM', 'ENABLE'))
        self.ui.btn_simdisable.clicked.connect(lambda: self.sendcmd('SIM', 'DISABLE'))
        self.ui.btn_settime.clicked.connect(lambda: self.sendcmd('ST', GetTime.time_UTC()))
        self.ui.btn_sendpressure.clicked.connect(lambda: self.thread())

    def clear(self):
        self.ui.pkg_c.setText("-00.00-")
        self.ui.pkg_p1.setText("-00.00-")
        self.ui.pkg_p2.setText("-00.00-")
        self.ui.mode.setText("NONE")
        self.ui.battery_c.setText("-00.00-")
        self.ui.altitude_c.setText("-00.00-")
        self.ui.altitude_p1.setText("-00.00-")
        self.ui.altitude_p2.setText("-00.00-")
        self.ui.temp_c.setText("-00.00-")
        self.ui.temp_p1.setText("-00.00-")
        self.ui.temp_p2.setText("-00.00-")
        self.ui.gpsalt_c.setText("-00.00-")
        self.ui.rotation_p1.setText("-00.00-")
        self.ui.rotation_p2.setText("-00.00-")

        self.ui.StateBar.setProperty('value', 0)
        self.ui.ContainerBar.setProperty('value', 0)
        self.ui.PL1Bar.setProperty('value', 0)
        self.ui.PL2Bar.setProperty('value', 0)

    def refresh(self):
        self.ui.Portlist.clear()
        for com in Datahandle.Port.list_ports():
            self.ui.Portlist.addItem(com)

    def sendcmd(self, cmdtype, cmd):
        self.device.write(f"CMD,3751,{cmdtype},{cmd}$".encode())
        print(f"CMD,3751,{cmdtype},{cmd}$")

    def thread(self):
        self.x = threading.Thread(target=self.sim)
        self.x.start()

    def thread2(self):
        self.x1 = threading.Thread(target=web.open_browser)
        self.x1.start()

    def sim(self):
        Window.clear()
        file = 'sim.txt'
        self.ui.filename.setText(file)
        print(f"simulating : {file}")
        if os.path.exists(f"SIM/{file}"):
            with open(f'SIM/{file}', 'r') as f:
                simdata = f.readlines()
            for data in simdata:
                x = data.find("CMD")
                if x == 0:
                    data = data.replace('$', '3751')
                    data = data.replace('\n', '')
                    self.device.write((data + "$").encode())
                    time.sleep(0.95)
                    print(data)
        else:
            print("ERROR NO FILE!")

    def connect(self):
        Window.connectserver()
        self.A = self.ui.Portlist.currentText()
        try:
            self.device = serial.Serial(self.A, baudrate=int(9600), timeout=60)
            Window.start_serial(self.device)
            Window.start_clock()
        except:
            print("[Cannot connect port]")

        self.refresh()

    @staticmethod
    def setpg():
        pg.setConfigOption('background', (56, 58, 89))
        pg.setConfigOption('foreground', 'w')


class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = UI_splashscreen()
        self.ui.setupUi(self)
        self.ui.lb_title.setText(" ")
        SplashScreenFunctions.ui_definitions(self)
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        self.timer.start(10)
        self.show()

    def progress(self):
        global GLOBAL_SPLASH_COUNTER
        status_text = str(GLOBAL_SPLASH_COUNTER) + '%'
        if GLOBAL_SPLASH_COUNTER <= 17:
            self.ui.lb_status.setText('Loading Assets...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 29:
            self.ui.lb_status.setText('Scanning all COM Ports...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 42:
            self.ui.lb_status.setText('Connecting to WAREDTANAS...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 54:
            self.ui.lb_status.setText('Verifying WAREDTANS...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 64:
            self.ui.lb_status.setText('Verifying Devices...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 75:
            self.ui.lb_status.setText('Preparing Interface...\n' + status_text)
        elif GLOBAL_SPLASH_COUNTER <= 100:
            self.ui.lb_status.setText('Done.\n' + status_text)
        else:
            self.timer.stop()
            Window.show_ui()
            self.close()

        GLOBAL_SPLASH_COUNTER += 1


class ThreadMain(QThread):
    carrier1 = QtCore.pyqtSignal(object)
    carrier2 = QtCore.pyqtSignal(object)
    carrier3 = QtCore.pyqtSignal(object)

    def __init__(self, device, parent=None):
        super(ThreadMain, self).__init__(parent)
        self.device = device
        self.port = Datahandle.Port(device=self.device)
        # self.startread.connect_port(9600)

    def __del__(self):
        self.wait()

    def run(self):
        print('[THREAD_MAIN_START]')
        while True:
            self.pkg = self.port.reading()
            print(f"[THREAD_IN] : {self.pkg}")
            if self.pkg[3] == 'C':
                print('[CANSAT]', end="")
                self.pkg1 = self.pkg[:]  # pkgc
                self.carrier1.emit(self.pkg1)
            elif self.pkg[3] == 'SP1':
                print('[PAYLOAD1]', end="")
                self.pkg2 = self.pkg[:]  # pkgc
                self.carrier2.emit(self.pkg2)
            elif self.pkg[3] == 'SP2':
                print('[PAYLOAD2]', end="")
                self.pkg3 = self.pkg[:]  # pkgc
                self.carrier3.emit(self.pkg3)

    def stop(self):
        self._isRunning = False


class ThreadGraph(QThread):
    Isgraph = QtCore.pyqtSignal(object, list, list)

    def __init__(self, graph, x, y, parent=None):
        self._isRunning = True
        super(ThreadGraph, self).__init__(parent)
        self.graph = graph
        self.x = x
        self.y = y

    def __del__(self):
        self.wait()

    def run(self):
        self.Isgraph.emit(self.graph, self.x, self.y)

    def stop(self):
        self._isRunning = False
        self.terminate()


class ThreadTimer(QThread):
    time_carrier = QtCore.pyqtSignal(object)
    elapsed_carrier = QtCore.pyqtSignal(object)

    def __init__(self, parent=None):
        self._isRunning = True
        super(ThreadTimer, self).__init__(parent)

    def __del__(self):
        self.wait()

    def run(self):
        clock = GetTime()
        while True:
            self.time_carrier.emit(clock.time_pc())
            self.elapsed_carrier.emit(clock.time_elapsed())

    def stop(self):
        self._isRunning = False
        self.terminate()


class ScreenActivation:
    def __init__(self):
        self.show_splash()

        self.send = False

    def clear(self):

        self.teamid = "3751"
        self.c_time = "HH:MM:SS.MS"
        self.c_pkg = 0
        self.c_pkg_graph = []
        self.c_alt_graph = []
        self.c_temp_graph = []
        self.c_galt_graph = []
        self.c_type = 'C'
        self.c_filghtmode = ""
        self.c_sp1r = "N"
        self.c_sp2r = "N"
        self.c_altitude = 0
        self.c_temp = 0
        self.c_battery = 0
        self.c_gpstime = "HH:MM:SS.MS"
        self.c_coord = []
        self.c_gpsalt = 0
        self.c_gpssat = 0
        self.c_state = "PRELAUNCH"
        self.c_echo = "NONE"
        self.altitude = []

        self.s1_time = "HH:MM:SS.MS"
        self.s1_type = 'S1'
        self.s1_pkg = 0
        self.s1_altitude = 0
        self.s1_temp = 0
        self.s1_rotation = 0
        self.s1_latitude = 0
        self.s1_longitude = 0
        self.s1_pkg_graph = []
        self.s1_alt_graph = []
        self.s1_temp_graph = []
        self.s1_rot_graph = []

        self.s2_time = "HH:MM:SS.MS"
        self.s2_type = 'S2'
        self.s2_pkg = 0
        self.s2_altitude = 0
        self.s2_temp = 0
        self.s2_rotation = 0
        self.s2_latitude = 0
        self.s2_longitude = 0
        self.s2_pkg_graph = []
        self.s2_alt_graph = []
        self.s2_temp_graph = []
        self.s2_rot_graph = []

        self.ui_main.ui.C_AltitudeGraph.clear()
        self.ui_main.ui.C_TempGraph.clear()
        self.ui_main.ui.C_GpsAltitudeGraph.clear()
        self.ui_main.ui.P1_TempGraph.clear()
        self.ui_main.ui.P1_RotationGraph.clear()
        self.ui_main.ui.P1_AltitudeGraph.clear()
        self.ui_main.ui.P2_AltitudeGraph.clear()
        self.ui_main.ui.P2_TempGraph.clear()
        self.ui_main.ui.P2_RotationGraph.clear()
        self.ui_main.ui.ContainerBar.setMaximum(1)
        self.ui_main.ui.PL1Bar.setMaximum(1)
        self.ui_main.ui.PL2Bar.setMaximum(1)

    def show_splash(self):
        self.window_splash = QtWidgets.QMainWindow()
        self.ui_ui = SplashScreen()
        print('[SPLASHSCREEN]', end="")

    def show_ui(self):
        self.window_ui = QtWidgets.QMainWindow()
        self.ui_main = MainWindow()
        self.clear()
        self.table = (
            self.ui_main.ui.IN_0, self.ui_main.ui.IN_1, self.ui_main.ui.IN_2, self.ui_main.ui.IN_3,
            self.ui_main.ui.IN_4,
            self.ui_main.ui.IN_5, self.ui_main.ui.IN_6, self.ui_main.ui.IN_7, self.ui_main.ui.IN_8,
            self.ui_main.ui.IN_9,
            self.ui_main.ui.IN_10, self.ui_main.ui.IN_11, self.ui_main.ui.IN_12, self.ui_main.ui.IN_13,
            self.ui_main.ui.IN_14,
            self.ui_main.ui.IN_15, self.ui_main.ui.IN_16, self.ui_main.ui.IN_17, self.ui_main.ui.IN_18,
            self.ui_main.ui.IN_19,)
        print('[MAINWINDOW]', end="")

    def start_clock(self):
        self.worker_time = ThreadTimer()
        self.worker_time.time_carrier.connect(self.update_time)
        self.worker_time.elapsed_carrier.connect(self.update_elapsed)
        self.worker_time.start()

    def start_serial(self, device):
        self.worker_serial = ThreadMain(device)
        self.worker_serial.carrier1.connect(self.update_container)
        self.worker_serial.carrier2.connect(self.update_payload1)
        self.worker_serial.carrier3.connect(self.update_payload2)
        self.worker_serial.start()

    def connectserver(self):
        try:
            self.MQTT = mqtt.Initialise_client()
            self.send = True
        except TimeoutError:
            print("***************[MQTT ERROR]***************")
            self.send = False

    def update_time(self, time):
        self.ui_main.ui.time_clock.setText(time)

    def update_elapsed(self, time):
        self.ui_main.ui.elapsed_clock.setText(time)

    def update_container(self, data):
        print("[UPDATE_CONTAINER]", end="")
        self.c_time = GetTime.time_pc()
        self.c_pkg = int(data[2])
        self.c_pkg_graph.append(self.c_pkg)
        self.c_filghtmode = str(data[4])
        self.c_sp1r = str(data[5])
        self.c_sp2r = str(data[6])
        self.c_altitude = float(data[7])
        self.c_alt_graph.append(self.c_altitude)
        self.altitude.append(float(data[7]))
        self.c_temp = (float(data[8]))
        self.c_temp_graph.append(self.c_temp)
        self.c_battery = float(data[9])
        self.c_gpstime = data[10]
        self.c_coord.append((float(data[11]), float(data[12])))
        self.c_gpsalt = float(data[13])
        self.c_galt_graph.append(self.c_gpsalt)
        self.c_gpssat = float(data[14])
        self.c_state = str(data[15])
        self.c_echo = str(data[18])
        self.update_main()

        if self.c_state == "PRELAUNCH":
            self.ui_main.ui.StateBar.setProperty('value', 0)
        elif self.c_state == "LAUNCH":
            self.ui_main.ui.StateBar.setProperty('value', 1)
        elif self.c_state == "EJECTED":
            self.ui_main.ui.StateBar.setProperty('value', 2)
        elif self.c_state == "RELEASED_1":
            self.ui_main.ui.StateBar.setProperty('value', 3)
        elif self.c_state == "RELEASED_2":
            self.ui_main.ui.StateBar.setProperty('value', 4)
        elif self.c_state == "LAND":
            self.ui_main.ui.StateBar.setProperty('value', 5)

        if len(self.c_pkg_graph) >= 30:
            self.ui_main.ui.C_AltitudeGraph.clear()
            self.ui_main.ui.C_TempGraph.clear()
            self.ui_main.ui.C_GpsAltitudeGraph.clear()
            self.start_graph(self.ui_main.ui.C_AltitudeGraph, self.c_pkg_graph[-30:-1], self.c_alt_graph[-30:-1])
            self.start_graph(self.ui_main.ui.C_TempGraph, self.c_pkg_graph[-30:-1], self.c_temp_graph[-30:-1])
            self.start_graph(self.ui_main.ui.C_GpsAltitudeGraph, self.c_pkg_graph[-30:-1], self.c_galt_graph[-30:-1])
        else:
            self.start_graph(self.ui_main.ui.C_AltitudeGraph, self.c_pkg_graph, self.c_alt_graph)
            self.start_graph(self.ui_main.ui.C_TempGraph, self.c_pkg_graph, self.c_temp_graph)
            self.start_graph(self.ui_main.ui.C_GpsAltitudeGraph, self.c_pkg_graph, self.c_galt_graph)
        self.ui_main.ui.ContainerBar.setProperty("value", 1)
        self.update_table(data[:])
        if self.send:
            mqtt.sendserver(self.MQTT, data)

    def update_payload1(self, data):
        print("[UPDATE_SP1]", end="")
        self.s1_time = GetTime.time_pc()
        self.s1_pkg = int(data[2])
        self.s1_pkg_graph.append(self.s1_pkg)
        self.s1_altitude = round(float(data[4]), 2)
        self.s1_alt_graph.append(self.s1_altitude)
        self.s1_temp = round(float(data[5]), 2)
        self.s1_temp_graph.append(self.s1_temp)
        self.s1_rotation = round(float(data[6]), 2)
        self.s1_rot_graph.append(self.s1_rotation)
        self.s1_latitude = data[7]
        self.s1_longitude = data[8]
        self.update_main()
        if len(self.s1_pkg_graph) >= 30:
            self.ui_main.ui.P1_AltitudeGraph.clear()
            self.ui_main.ui.P1_TempGraph.clear()
            self.ui_main.ui.P1_RotationGraph.clear()
            self.start_graph(self.ui_main.ui.P1_AltitudeGraph, self.s1_pkg_graph[-30:-1], self.s1_alt_graph[-30:-1])
            self.start_graph(self.ui_main.ui.P1_TempGraph, self.s1_pkg_graph[-30:-1], self.s1_temp_graph[-30:-1])
            self.start_graph(self.ui_main.ui.P1_RotationGraph, self.s1_pkg_graph[-30:-1], self.s1_rot_graph[-30:-1])
        else:
            self.start_graph(self.ui_main.ui.P1_AltitudeGraph, self.s1_pkg_graph, self.s1_alt_graph)
            self.start_graph(self.ui_main.ui.P1_TempGraph, self.s1_pkg_graph, self.s1_temp_graph)
            self.start_graph(self.ui_main.ui.P1_RotationGraph, self.s1_pkg_graph, self.s1_rot_graph)
        self.ui_main.ui.PL1Bar.setProperty('value', 1)
        self.update_table(data[:])
        if self.send:
            mqtt.sendserver(self.MQTT, data)

    def update_payload2(self, data):
        print("[UPDATE_SP2]", end="")
        self.s2_time = GetTime.time_pc()
        self.s2_pkg = int(data[2])
        self.s2_pkg_graph.append(self.s2_pkg)
        self.s2_altitude = round(float(data[4]), 2)
        self.s2_alt_graph.append(self.s2_altitude)
        self.s2_temp = round(float(data[5]), 2)
        self.s2_temp_graph.append(self.s2_temp)
        self.s2_rotation = round(float(data[6]), 2)
        self.s2_rot_graph.append(self.s2_rotation)
        self.update_main()
        self.s2_latitude = data[7]
        self.s2_longitude = data[8]

        if len(self.s2_pkg_graph) >= 30:
            self.ui_main.ui.P2_AltitudeGraph.clear()
            self.ui_main.ui.P2_TempGraph.clear()
            self.ui_main.ui.P2_RotationGraph.clear()
            self.start_graph(self.ui_main.ui.P2_AltitudeGraph, self.s2_pkg_graph[-30:-1], self.s2_alt_graph[-30:-1])
            self.start_graph(self.ui_main.ui.P2_TempGraph, self.s2_pkg_graph[-30:-1], self.s2_temp_graph[-30:-1])
            self.start_graph(self.ui_main.ui.P2_RotationGraph, self.s2_pkg_graph[-30:-1], self.s2_rot_graph[-30:-1])
        else:
            self.start_graph(self.ui_main.ui.P2_AltitudeGraph, self.s2_pkg_graph, self.s2_alt_graph)
            self.start_graph(self.ui_main.ui.P2_TempGraph, self.s2_pkg_graph, self.s2_temp_graph)
            self.start_graph(self.ui_main.ui.P2_RotationGraph, self.s2_pkg_graph, self.s2_rot_graph)
        self.ui_main.ui.PL2Bar.setProperty('value', 1)
        self.update_table(data[:])
        if self.send:
            mqtt.sendserver(self.MQTT, data)

    def update_main(self):
        print("[UPDATEMAIN]")
        self.ui_main.ui.pkg_c.setText(str(self.c_pkg))
        self.ui_main.ui.battery_c.setText(str(self.c_battery))
        self.ui_main.ui.altitude_c.setText(str(self.c_altitude))
        self.ui_main.ui.temp_c.setText(str(self.c_temp))
        self.ui_main.ui.gpsalt_c.setText(str(self.c_gpsalt))
        self.ui_main.ui.mode.setText(str(self.c_filghtmode))
        self.ui_main.ui.CMD.setText(str(self.c_echo))

        self.ui_main.ui.pkg_p1.setText(str(self.s1_pkg))
        self.ui_main.ui.altitude_p1.setText(str(self.s1_altitude))
        self.ui_main.ui.temp_p1.setText(str(self.s1_temp))
        self.ui_main.ui.rotation_p1.setText(str(self.s1_rotation))

        self.ui_main.ui.pkg_p2.setText(str(self.s2_pkg))
        self.ui_main.ui.altitude_p2.setText(str(self.s2_altitude))
        self.ui_main.ui.temp_p2.setText(str(self.s2_temp))
        self.ui_main.ui.rotation_p2.setText(str(self.s2_rotation))

    def start_graph(self, graph, x, y):
        self.worker_graph = ThreadGraph(graph, x, y)
        self.worker_graph.Isgraph.connect(self.update_graph)
        self.worker_graph.start()

    def update_graph(self, graph, x, y):
        try:
            graph.plot(x, y)
        except:
            pass
        else:
            self.worker_graph.terminate()

    def update_table(self, data):
        try:
            l = len(self.table) - len(data)
            for i in range(len(data)):
                self.table[i].setText(str(data[i]))
            for i in range(l):
                self.table[len(data) + i].setText(" ")
        except:
            for i in range(len(self.table)):
                self.table[len(data) + i].setText(" ")

    def update_map(self):
        print("[UPDATEMAP]")
        self.ui_main.ui.latitude_c.setText(str(self.c_coord[-1][0]))
        self.ui_main.ui.longitude_c.setText(str(self.c_coord[-1][0]))
        self.ui_main.ui.latitude_p1.setText(str(self.s1_latitude))
        self.ui_main.ui.longitude_p1.setText(str(self.s1_longitude))
        self.ui_main.ui.latitude_p2.setText(str(self.s2_latitude))
        self.ui_main.ui.longitude_p2.setText(str(self.s2_longitude))
        dt = maps.getmap(self.c_coord[-1], self.c_coord, self.altitude)
        self.ui_main.ui.MAP.setHtml(dt.getvalue().decode())


if __name__ == "__main__":
    app = QApplication(sys.argv)
    Window = ScreenActivation()
    sys.exit(app.exec_())
