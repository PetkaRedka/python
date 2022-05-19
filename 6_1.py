from PyQt5 import QtCore, QtGui, QtWidgets
import sys, threading
from time import sleep

from sympy import Q


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 442)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(150, 50, 121, 351))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.pushButton = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(".\\crosslight\\green_off.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton.setIcon(icon)
        self.pushButton.setIconSize(QtCore.QSize(100, 100))
        self.pushButton.setObjectName("pushButton")
        self.verticalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(".\\crosslight\\yellow_off.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_2.setIcon(icon1)
        self.pushButton_2.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.verticalLayoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Ignored)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(".\\crosslight\\red_off.PNG"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_3.setIcon(icon2)
        self.pushButton_3.setIconSize(QtCore.QSize(100, 100))
        self.pushButton_3.setObjectName("pushButton_3")
        self.verticalLayout.addWidget(self.pushButton_3)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 5, 424, 38))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "ВЫ МОЖЕТЕ УСКОРИТЬ ПРОЦЕСС, НАЖИМАЯ\nНА ЦВЕТА В НУЖНОМ ПОРЯДКЕ"))


class TrafficLight(QtWidgets.QMainWindow):
    
    __color = "red"
    __counter = 0
    thread_check = False

    def running(self):

        start_thread = threading.Thread(target = self.run_green, daemon = True)
        start_thread.start()


    def run_green(self):

        def off_green():
            self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\green_off.PNG")))
            self.run_yellow()

        # Светофор пройдет 10 кругов
        if self.__counter == 10:
            return
        else: self.__counter += 1

        self.__color = "green"
        self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\green.PNG")))

        for _ in range(10):

            if self.thread_check == True:

                self.ui.pushButton.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\green_off.PNG")))
                
                if self.__color != "yellow":
                    self.dead()
                    return
                
                else:
                    self.thread_check = False
                    break
                
            sleep(0.5)
        off_green()
    

    def run_yellow(self):

        def off_yellow():
            self.ui.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\yellow_off.PNG")))
            self.run_red()

        self.__color = "yellow"
        self.ui.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\yellow.PNG")))

        for _ in range(4):

            if self.thread_check == True:

                self.ui.pushButton_2.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\yellow_off.PNG")))
                
                if self.__color != "red":
                    self.dead()
                    return
                
                else:
                    self.thread_check = False
                    break

            sleep(0.5)
        off_yellow()

        
    def run_red(self):

        def off_red():
            self.ui.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\red_off.PNG")))
            self.run_green()
            
        self.__color = "red"
        self.ui.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\red.PNG")))

        for _ in range(14):

            if self.thread_check == True:

                self.ui.pushButton_3.setIcon(QtGui.QIcon(QtGui.QPixmap(".\\crosslight\\red_off.PNG")))

                if self.__color != "green":
                    self.dead()
                    return
                
                else:
                    self.thread_check = False
                    break

            sleep(0.5)
        off_red()


    def dead(self):
        self.ui.label.setText("ВЫ ОШИБЛИСЬ! СВЕТОФОР ТЕПЕРЬ СЛОМАН!")
        
        
    def check_green(self):

        self.__color = "green"
        self.thread_check = True


    def check_yellow(self):

        self.__color = "yellow"
        self.thread_check = True


    def check_red(self):

        self.__color = "red"
        self.thread_check = True


    def __init__(self):

        super(TrafficLight, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.pushButton.clicked.connect(self.check_green)
        self.ui.pushButton_2.clicked.connect(self.check_yellow)
        self.ui.pushButton_3.clicked.connect(self.check_red)

        self.running()


app = QtWidgets.QApplication([])
application = TrafficLight()
application.show()
sys.exit(app.exec())