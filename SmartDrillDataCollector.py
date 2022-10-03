# -*- coding: utf-8 -*-
from ast import main
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QFileDialog,QMessageBox, QGraphicsScene
from PyQt5 import QtGui
import PyQt5
from GUI import Ui_SmartDrill
import sys
from SmartDrillDataBase import SmartDrillDataBase
from pathlib import Path
from sensors import NDI
from createDialog import CreateDialog
import time
import threading
class mainWindow(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.main_ui = Ui_SmartDrill()
        self.main_ui.setupUi(self)
        self.reset()
        self.main_ui.actionSave.triggered.connect(self.save)

    def sensorInitialization(self):
        self.main_ui.pushButtonStartInitialize.setDisabled(True)
        self.main_ui.pushButtonStartInitialize.setText("Initializing...")
        for i in self.sensorList:
            try:
                self.sensorList[i].init()
            except:
                msgBox = QMessageBox()
                msgBox.setText("Fail to initialize sensor {}.".format(i))
                msgBox.setWindowTitle("Sensor Initializationi Error") 
                msgBox.exec_()
                self.main_ui.pushButtonStartInitialize.setDisabled(False)
                return
        self.areSensorInitialized = True
        self.main_ui.pushButtonTest.clicked.connect(self.startTesting)
        self.main_ui.pushButtonTest.setDisabled(False)
        self.main_ui.pushButtonStartInitialize.setText("Initialized")

    def createVis(self):
        for index,i in enumerate(self.sensorList):
            self.main_ui.graphicsLayout.addWidget(self.sensorList[i].canvas,int(index /self.numofGraphsperRow),
            index % self.numofGraphsperRow)

    def startTesting(self):
        self.main_ui.pushButtonTest.setDisabled(True)
        self.main_ui.pushButtonTest.setText("Testing...")
        for i in self.sensorList:
            self.timer[i] = float(time.time())
            try:
                self.sensorList[i].update()
            except:
                msgBox = QMessageBox()
                msgBox.setText("Cannot recieve update from sensor {}.".format(i))
                msgBox.setWindowTitle("Sensor Test Error") 
                msgBox.exec_()
                self.main_ui.pushButtonTest.setDisabled(False)
                self.main_ui.pushButtonTest.setText("Test")
                return False
        self.main_ui.pushButtonTest.setDisabled(False)
        self.main_ui.pushButtonTest.clicked.disconnect()
        self.main_ui.pushButtonTest.clicked.connect(self.stopTesting)
        self.main_ui.pushButtonTest.setText("Stop Test")
        return True

    def stopTesting(self):
        self.main_ui.pushButtonTest.setDisabled(True)
        for i in self.sensorList:
            try:
                endTime = time.time()
                self.pubNotice("Sensor {} collected {} data during testing, mean frequency is {}".format(i,len(self.sensorList[i]),
                len(self.sensorList[i]) / (endTime - self.timer[i])))
                self.sensorList[i].stop()
                self.sensorList[i].clear()
            except:
                msgBox = QMessageBox()
                msgBox.setText("Cannot safely stop the testing of sensor {}. Please abort the software and debug!".format(i))
                msgBox.setWindowTitle("Sensor Test Error") 
                msgBox.exec_()
                return
        self.main_ui.pushButtonTest.clicked.disconnect()
        self.main_ui.pushButtonTest.clicked.connect(self.startTesting)
        self.main_ui.pushButtonTest.setDisabled(False)
        self.main_ui.pushButtonTest.setText("Test")
        self.main_ui.pushButtonRecord.clicked.connect(self.startCollection)
        self.main_ui.pushButtonRecord.setDisabled(False)
        self.timer = {}

    def startCollection(self):
        self.main_ui.pushButtonTest.setDisabled(True)
        self.main_ui.pushButtonRecord.setDisabled(True)
        for i in self.sensorList:
            start = time.time()
            try:
                self.sensorList[i].update()
                self.timer[i] = start
            except:
                msgBox = QMessageBox()
                msgBox.setText("Cannot recieve update from sensor {}.".format(i))
                msgBox.setWindowTitle("Sensor Run Error") 
                msgBox.exec_()
                self.main_ui.pushButtonRecord.setDisabled(False)
                self.main_ui.pushButtonTest.setDisabled(False)
                return
        self.unsaved = True
        self.isCollection = True
        self.Timing()
        self.main_ui.pushButtonRecord.setText("Stop")
        self.main_ui.pushButtonRecord.setDisabled(False)
        self.main_ui.pushButtonRecord.clicked.disconnect()
        self.main_ui.pushButtonRecord.clicked.connect(self.stopCollection)
        self.main_ui.pushButtonRecord.setStyleSheet("background-color : red")

    def stopCollection(self):
        self.main_ui.pushButtonRecord.setDisabled(True)
        self.isCollection = False
        self.timingThread.join()
        for i in self.sensorList:
            try:
                endTime = time.time()
                self.sensorList[i].stop()
                self.pubNotice("Sensor {} collected {} data during testing, mean frequency is {}".format(i,len(self.sensorList[i]),
                len(self.sensorList[i]) / (endTime - self.timer[i])))
                self.timer[i] = endTime - self.timer[i]
            except:
                msgBox = QMessageBox()
                msgBox.setText("Cannot safely stop the testing of sensor {}. Please abort the software and debug!".format(i))
                msgBox.setWindowTitle("Sensor Test Error") 
                msgBox.exec_()
                return
        for i in self.sensorList:
            try:
                endTime = time.time()
                self.sensorList[i].kill()
            except:
                msgBox = QMessageBox()
                msgBox.setText("Fail to kill sensor {}".format(i))
                msgBox.setWindowTitle("Sensor Kill Error") 
                msgBox.exec_()

        self.main_ui.pushButtonRecord.clicked.disconnect()
        self.main_ui.pushButtonRecord.setText("Finished")
        self.main_ui.pushButtonRecord.setStyleSheet("background-color : green")

    def save(self):
        self.path= QFileDialog.getSaveFileName(None, "Select Directory", "./")    
        self.fileInUse = self.path[0] + ".json"
        if self.Database:
            for i in self.sensorList:
                self.Database.update(i,self.sensorList[i].data,self.timer[i])
            self.Database.save(self.fileInUse)
            self.unsaved = False
        else:
            msgBox = QMessageBox()
            msgBox.setText("No Data Needs to Save.")
            msgBox.setWindowTitle("Save Error") 
            msgBox.exec_()

    def resetHz(self):
        for i in self.HzSetting:
            self.main_ui.textBrowserHzSetting.append(" {}: {}".format(i,str(self.HzSetting[i])))

    def pubNotice(self,Notice):
        self.main_ui.textBrowserInfo.append(str(Notice))

    def Timing(self):
        self.timingThread = threading.Thread(target = self._Timing)
        self.timingThread.start()

    def _Timing(self):
        startTime = time.time()
        while self.isCollection:
            sec = int(time.time() - startTime) % 60
            min = int((time.time() - startTime) // 60)
            self.main_ui.timer.setText(str(min).zfill(2) + ":" + str(sec).zfill(2))

    def reset(self):
        self.main_ui.pushButtonRecord.setDisabled(True)
        self.main_ui.pushButtonTest.setDisabled(True)
        self.main_ui.pushButtonRecord.setText("Record")
        self.main_ui.pushButtonStartInitialize.setText("Initialize")
        self.main_ui.pushButtonTest.setText("Test")

        try:
            self.main_ui.pushButtonRecord.clicked.disconnect()
        except TypeError:
            pass
            
        try:
            self.main_ui.pushButtonTest.clicked.disconnect()
        except TypeError:
            pass

        try:
            self.main_ui.pushButtonStartInitialize.clicked.disconnect()
        except TypeError:
            pass

        self.main_ui.pushButtonStartInitialize.clicked.connect(self.sensorInitialization)
        self.numofGraphsperRow = 3
        self.NDISetting = {"JSON":"./NDI/SmartDrill.json","PORTAL":"/dev/ttyUSB0"}
        self.HzSetting = {}
        self.fileInUse = None
        self.Database = None
        self.unsaved = False
        self.sensorList = {}
        self.graphics = {}
        self.timer = {}
        self.isCollection = False
        self.timingThread = None
        self.main_ui.pushButtonRecord.setStyleSheet("background-color : white")
        self.main_ui.pushButtonStartInitialize.setDisabled(False)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainWindow = mainWindow()
    # NDISettingDialog = NDISettingDialog(mainWindow)
    createDialog = CreateDialog(mainWindow)
    # Link main window actions to sub-windows
    # mainWindow.main_ui.actionNDISettings.triggered.connect(NDISettingDialog.show)
    mainWindow.main_ui.actionCreate.triggered.connect(createDialog.show)
    
    mainWindow.show()
    sys.exit(app.exec_())