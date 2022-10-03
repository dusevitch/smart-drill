# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from csv import writer, reader
import numpy as np
from qwt import QwtPlot

class Ui_SmartDrill(object):
    def setupUi(self, SmartDrill):
        SmartDrill.setObjectName("SmartDrill")
        SmartDrill.resize(1186, 707)
        self.centralwidget = QtWidgets.QWidget(SmartDrill)
        self.centralwidget.setObjectName("centralwidget")
        self.textBrowserInfo = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserInfo.setGeometry(QtCore.QRect(20, 560, 1151, 121))
        self.textBrowserInfo.setObjectName("textBrowserInfo")
        self.pushButtonRecord = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonRecord.setGeometry(QtCore.QRect(610, 440, 231, 101))
        font = QtGui.QFont()
        font.setPointSize(37)
        self.pushButtonRecord.setFont(font)
        self.pushButtonRecord.setObjectName("pushButtonRecord")
        self.showFrequency = QtWidgets.QLabel(self.centralwidget)
        self.showFrequency.setGeometry(QtCore.QRect(20, 430, 141, 17))
        self.showFrequency.setObjectName("showFrequency")
        self.pushButtonStartInitialize = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonStartInitialize.setGeometry(QtCore.QRect(270, 490, 131, 51))
        self.pushButtonStartInitialize.setObjectName("pushButtonStartInitialize")
        self.textBrowserHzSetting = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowserHzSetting.setGeometry(QtCore.QRect(20, 450, 221, 101))
        self.textBrowserHzSetting.setObjectName("textBrowserHzSetting")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(20, 10, 1141, 411))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.graphicsLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.graphicsLayout.setContentsMargins(0, 0, 0, 0)
        self.graphicsLayout.setObjectName("graphicsLayout")
        self.graphicsView = QtWidgets.QGraphicsView(self.gridLayoutWidget)
        self.graphicsView.setObjectName("graphicsView")
        self.graphicsLayout.addWidget(self.graphicsView, 0, 0, 1, 1)
        self.pushButtonTest = QtWidgets.QPushButton(self.centralwidget)
        self.pushButtonTest.setGeometry(QtCore.QRect(440, 490, 131, 51))
        self.pushButtonTest.setObjectName("pushButtonTest")
        self.timer = QtWidgets.QLabel(self.centralwidget)
        self.timer.setGeometry(QtCore.QRect(910, 480, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(18)
        self.timer.setFont(font)
        self.timer.setObjectName("timer")
        SmartDrill.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(SmartDrill)
        self.statusbar.setObjectName("statusbar")
        SmartDrill.setStatusBar(self.statusbar)
        self.menubar = QtWidgets.QMenuBar(SmartDrill)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1186, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        SmartDrill.setMenuBar(self.menubar)
        self.actionSave = QtWidgets.QAction(SmartDrill)
        self.actionSave.setObjectName("actionSave")
        self.actionLoad = QtWidgets.QAction(SmartDrill)
        self.actionLoad.setObjectName("actionLoad")
        self.actionMicrophoneActive = QtWidgets.QAction(SmartDrill)
        self.actionMicrophoneActive.setCheckable(True)
        self.actionMicrophoneActive.setChecked(True)
        self.actionMicrophoneActive.setObjectName("actionMicrophoneActive")
        self.actionIMUActive = QtWidgets.QAction(SmartDrill)
        self.actionIMUActive.setCheckable(True)
        self.actionIMUActive.setChecked(True)
        self.actionIMUActive.setObjectName("actionIMUActive")
        self.actionCurrentActive = QtWidgets.QAction(SmartDrill)
        self.actionCurrentActive.setCheckable(True)
        self.actionCurrentActive.setChecked(True)
        self.actionCurrentActive.setObjectName("actionCurrentActive")
        self.actionF_t_SensorActive = QtWidgets.QAction(SmartDrill)
        self.actionF_t_SensorActive.setCheckable(True)
        self.actionF_t_SensorActive.setChecked(True)
        self.actionF_t_SensorActive.setObjectName("actionF_t_SensorActive")
        self.actionNDIActive = QtWidgets.QAction(SmartDrill)
        self.actionNDIActive.setCheckable(True)
        self.actionNDIActive.setChecked(True)
        self.actionNDIActive.setObjectName("actionNDIActive")
        self.actionMicrophoneSettings = QtWidgets.QAction(SmartDrill)
        self.actionMicrophoneSettings.setObjectName("actionMicrophoneSettings")
        self.actionIMUSettings = QtWidgets.QAction(SmartDrill)
        self.actionIMUSettings.setObjectName("actionIMUSettings")
        self.actionCurrentSettings = QtWidgets.QAction(SmartDrill)
        self.actionCurrentSettings.setObjectName("actionCurrentSettings")
        self.actionF_t_SensorSettings = QtWidgets.QAction(SmartDrill)
        self.actionF_t_SensorSettings.setObjectName("actionF_t_SensorSettings")
        self.actionNDISettings = QtWidgets.QAction(SmartDrill)
        self.actionNDISettings.setObjectName("actionNDISettings")
        self.actionEnable = QtWidgets.QAction(SmartDrill)
        self.actionEnable.setCheckable(True)
        self.actionEnable.setObjectName("actionEnable")
        self.actionCreate = QtWidgets.QAction(SmartDrill)
        self.actionCreate.setObjectName("actionCreate")
        self.menuFile.addAction(self.actionCreate)
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(SmartDrill)
        QtCore.QMetaObject.connectSlotsByName(SmartDrill)

    def retranslateUi(self, SmartDrill):
        _translate = QtCore.QCoreApplication.translate
        SmartDrill.setWindowTitle(_translate("SmartDrill", "MainWindow"))
        self.pushButtonRecord.setText(_translate("SmartDrill", "Record"))
        self.showFrequency.setText(_translate("SmartDrill", "Frequency Settings:"))
        self.pushButtonStartInitialize.setText(_translate("SmartDrill", "Initialize"))
        self.pushButtonTest.setText(_translate("SmartDrill", "Test Sensors"))
        self.timer.setText(_translate("SmartDrill", "00:00"))
        self.menuFile.setTitle(_translate("SmartDrill", "File"))
        self.actionSave.setText(_translate("SmartDrill", "Save"))
        self.actionLoad.setText(_translate("SmartDrill", "Load"))
        self.actionMicrophoneActive.setText(_translate("SmartDrill", "Active"))
        self.actionIMUActive.setText(_translate("SmartDrill", "Active"))
        self.actionCurrentActive.setText(_translate("SmartDrill", "Active"))
        self.actionF_t_SensorActive.setText(_translate("SmartDrill", "Active"))
        self.actionNDIActive.setText(_translate("SmartDrill", "Active"))
        self.actionMicrophoneSettings.setText(_translate("SmartDrill", "Settings"))
        self.actionIMUSettings.setText(_translate("SmartDrill", "Settings"))
        self.actionCurrentSettings.setText(_translate("SmartDrill", "Settings"))
        self.actionF_t_SensorSettings.setText(_translate("SmartDrill", "Settings"))
        self.actionNDISettings.setText(_translate("SmartDrill", "Settings"))
        self.actionEnable.setText(_translate("SmartDrill", "Enable"))
        self.actionCreate.setText(_translate("SmartDrill", "Create"))


