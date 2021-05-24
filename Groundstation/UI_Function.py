from main import *
from pyqtgraph import PlotWidget, opengl
import pyqtgraph as pg

GLOBAL_STATE = 0
GLOBAL_STATE_TABLE = 0
GLOBAL_STATE_MAP = 0


class UiFunctions(MainWindow):
    def maximize_restore(self):
        global GLOBAL_STATE
        status = GLOBAL_STATE

        if status == 0:
            self.showMaximized()
            GLOBAL_STATE = 1
            self.ui.btn_restore.setToolTip('Restore')
        else:
            GLOBAL_STATE = 0
            self.showNormal()
            self.resize(self.width(), self.height())
            self.ui.btn_restore.setToolTip('Maximize')

    def ui_definitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.BG.setGraphicsEffect(self.shadow)

        self.ui.btn_restore.clicked.connect(lambda: UiFunctions.maximize_restore(self))
        self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
        self.ui.btn_close.clicked.connect(lambda: sys.exit())

        # self.sizegrip = QSizeGrip(self.ui.frame_grip)
        # self.sizegrip.setStyleSheet('QSizeGrip {width: 30px; height: 30px; margin: 5px}')
        # self.sizegrip.setToolTip('Resize Window')

    def return_status(self):
        return GLOBAL_STATE


class SplashScreenFunctions(SplashScreen):
    def ui_definitions(self):
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setAttribute(Qt.WA_TranslucentBackground)

        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 100))

        self.ui.Splashscreen.setGraphicsEffect(self.shadow)


# class TableFunctions(TableWindow):
#     def maximize_restore(self):
#         global GLOBAL_STATE_TABLE
#         status = GLOBAL_STATE_TABLE
#
#         if status == 0:
#             self.showMaximized()
#             GLOBAL_STATE_TABLE = 1
#             self.ui.btn_restore.setToolTip('Restore')
#
#         else:
#             GLOBAL_STATE_TABLE = 0
#             self.showNormal()
#             self.resize(self.width(), self.height())
#             self.ui.btn_restore.setToolTip('Maximize')
#
#     def ui_definitions(self):
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(20)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 100))
#
#         self.ui.BG.setGraphicsEffect(self.shadow)
#
#         self.ui.btn_restore.clicked.connect(lambda: TableFunctions.maximize_restore(self))
#         self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
#         self.ui.btn_close.clicked.connect(lambda: self.close())
#
#     def return_status(self):
#         return GLOBAL_STATE_TABLE
#
#
# class MapFunctions(MapWindow):
#     def maximize_restore(self):
#         global GLOBAL_STATE_MAP
#         status = GLOBAL_STATE_MAP
#
#         if status == 0:
#             self.showMaximized()
#             GLOBAL_STATE_MAP = 1
#             self.ui.btn_restore.setToolTip('Restore')
#
#         else:
#             GLOBAL_STATE_MAP = 0
#             self.showNormal()
#             self.resize(self.width(), self.height())
#             self.ui.btn_restore.setToolTip('Maximize')
#
#     def ui_definitions(self):
#         self.setWindowFlag(Qt.FramelessWindowHint)
#         self.setAttribute(Qt.WA_TranslucentBackground)
#
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(20)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 100))
#
#         self.ui.BG.setGraphicsEffect(self.shadow)
#
#         self.ui.btn_restore.clicked.connect(lambda: MapFunctions.maximize_restore(self))
#         self.ui.btn_minimize.clicked.connect(lambda: self.showMinimized())
#         self.ui.btn_close.clicked.connect(lambda: self.close())
#
#     def return_status(self):
#         return GLOBAL_STATE_MAP
