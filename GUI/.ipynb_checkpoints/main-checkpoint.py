# -*- coding: utf-8 -*-
from PyQt5 import QtCore, QtGui, QtWidgets
from csv import writer, reader
import numpy as np
from .NDISetting import Ui_settingNDI
from configparser import ConfigParser
import sys
class Ui_SmartDrill(object):
    def __init__(self):
        self.NDISettingui = Ui_settingNDI()
        
    def setupUi(self, SmartDrill):
        SmartDrill.setObjectName("SmartDrill")
        SmartDrill.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(SmartDrill)
        self.centralwidget.setObjectName("centralwidget")
        SmartDrill.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(SmartDrill)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 22))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuSensors = QtWidgets.QMenu(self.menubar)
        self.menuSensors.setObjectName("menuSensors")
        self.menuMicrophone = QtWidgets.QMenu(self.menuSensors)
        self.menuMicrophone.setObjectName("menuMicrophone")
        self.menuIMU = QtWidgets.QMenu(self.menuSensors)
        self.menuIMU.setObjectName("menuIMU")
        self.menuCurrent = QtWidgets.QMenu(self.menuSensors)
        self.menuCurrent.setObjectName("menuCurrent")
        self.menuF_T_Sensor = QtWidgets.QMenu(self.menuSensors)
        self.menuF_T_Sensor.setObjectName("menuF_T_Sensor")
        self.menuNDI = QtWidgets.QMenu(self.menuSensors)
        self.menuNDI.setObjectName("menuNDI")
        SmartDrill.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(SmartDrill)
        self.statusbar.setObjectName("statusbar")
        SmartDrill.setStatusBar(self.statusbar)
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
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionLoad)
        self.menuMicrophone.addAction(self.actionMicrophoneActive)
        self.menuMicrophone.addAction(self.actionMicrophoneSettings)
        self.menuIMU.addAction(self.actionIMUActive)
        self.menuIMU.addAction(self.actionIMUSettings)
        self.menuCurrent.addAction(self.actionCurrentActive)
        self.menuCurrent.addAction(self.actionCurrentSettings)
        self.menuF_T_Sensor.addAction(self.actionF_t_SensorActive)
        self.menuF_T_Sensor.addAction(self.actionF_t_SensorSettings)
        self.menuNDI.addAction(self.actionNDIActive)
        self.menuNDI.addAction(self.actionNDISettings)
        self.menuSensors.addAction(self.menuMicrophone.menuAction())
        self.menuSensors.addAction(self.menuIMU.menuAction())
        self.menuSensors.addAction(self.menuCurrent.menuAction())
        self.menuSensors.addAction(self.menuF_T_Sensor.menuAction())
        self.menuSensors.addAction(self.menuNDI.menuAction())
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuSensors.menuAction())

        self.retranslateUi(SmartDrill)
        QtCore.QMetaObject.connectSlotsByName(SmartDrill)

    def retranslateUi(self, SmartDrill):
        _translate = QtCore.QCoreApplication.translate
        SmartDrill.setWindowTitle(_translate("SmartDrill", "MainWindow"))
        self.menuFile.setTitle(_translate("SmartDrill", "File"))
        self.menuSensors.setTitle(_translate("SmartDrill", "Sensors"))
        self.menuMicrophone.setTitle(_translate("SmartDrill", "Microphone"))
        self.menuIMU.setTitle(_translate("SmartDrill", "IMU"))
        self.menuCurrent.setTitle(_translate("SmartDrill", "Current"))
        self.menuF_T_Sensor.setTitle(_translate("SmartDrill", "F/T Sensor"))
        self.menuNDI.setTitle(_translate("SmartDrill", "NDI"))
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
        
    def initialize(self,mainUI):
        self.NDIData = np.array([])
        self.NDISetting = {"JSON":"./NDI/SmartDrill.json","PORTAL":"/dev/ttyUSB0"}
        self.actionSave.triggered.connect(self.saveFile)
        self.actionNDISettings.triggered.connect(self.settingNDI)
        self.mainUI = mainUI
        
    def saveFile(self):
        file, _ = QtWidgets.QFileDialog.getSaveFileName(None, "Save data",
                                                   "", "CSV Files (*.csv)")
        if file:
            # Currently only NDI data is stored and recorded.
            with open(file,"w") as f:
                titleList=["Time","NDI_x","NDI_y","NDI_z","NDI_Rx","NDI_Ry","NDI_Rz","NDI_Rw"]
                writer_object = writer(f)
                writer_object.writerow(titleList)
                for i in self.NDIData:
                    writer.object.writerow(i.tolist())
                    
    def loadFile(self):
        file, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load data",
                                                   "", "CSV Files (*.csv)")
        if self.NDIData.size > 0:
            qm = QtGui.QMessageBox
            qm.question(self,'', "You have loaded/unsaved data in memory. Clear and load a new one?", qm.Yes | qm.No)

            if qm.Yes:
                if file:
                # Currently only NDI data is stored and recorded.
                    try:
                        with open(file,"r") as f:
                            read_object = reader(f)
                            for i,rows in enumerate(read_object):
                                if i == 0:
                                    continue
                                if i == 1:
                                    self.NDIData = np.asarray(rows)
                                    continue
                                self.NDIData.append(np.asarray([rows]))
                    except:
                        QMessageBox.about(self, "Error", "Fail to load file.")
                        self.NDIData = np.array([])
            else:
                return
            
    def settingNDI(self):
        self.NDISettingui.setupUi(self.mainUI)
        self.NDISettingui.initialize(self.NDISetting)
        self.NDISettingui.show()
        config = ConfigParser()
        config.read("/tmp/SmartDrillDataCollectorNDICache.ini")
        self.NDISetting["JSON"] = config["NDI"]["JSON"]
        self.NDISetting["PORTAL"] = config["NDI"]["PORTAL"]