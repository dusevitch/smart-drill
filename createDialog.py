from ast import main
from PyQt5.QtWidgets import QApplication,QMainWindow,QDialog,QFileDialog,QMessageBox, QGraphicsScene
from PyQt5 import QtGui
import PyQt5
from GUI import Ui_SmartDrill, Ui_Create
import sys
from SmartDrillDataBase import SmartDrillDataBase
from pathlib import Path
import config
from sensors import NDI


class CreateDialog(QDialog):
    def __init__(self,mainWindow):
        QDialog.__init__(self)
        self.path = None
        self.filename = None
        self.createDialog=Ui_Create()
        self.createDialog.setupUi(self)
        self.createDialog.buttonBox.accepted.connect(self.create)
        self.createDialog.buttonBox.rejected.connect(lambda:self.close())
        self.createDialog.spinBoxNDI.setValue(int(config.Hz["NDI"]))
        self.createDialog.spinBoxCurrent.setValue(int(config.Hz["Current"]))
        self.createDialog.spinBoxMicrophone.setValue(int(config.Hz["Microphone"]))
        self.createDialog.spinBoxIMU.setValue(int(config.Hz["IMU"]))
        self.createDialog.spinBoxFT.setValue(int(config.Hz["FT"]))
        self.mainWindow = mainWindow 

    def create(self): 
        if self.mainWindow.Database and self.mainWindow.unsaved:
            qm = QMessageBox()
            ret = qm.question(self,'', "You have loaded/unsaved data in memory. Clear and create a new one?", qm.Yes | qm.No)
            if ret == qm.No:
                return

        self.mainWindow.reset()
        if self.createDialog.checkBoxNDI.isChecked():
            try:
                self.mainWindow.HzSetting["NDI"] = self.createDialog.spinBoxNDI.value()
                self.mainWindow.sensorList["NDI"] = NDI.NDI(self.mainWindow.HzSetting["NDI"],self.mainWindow,config.sawSetting,config.NDISetting)
            except:
                msgBox = QMessageBox()
                msgBox.setText("Fail to config NDI. Please check your configuration file.")
                msgBox.setWindowTitle("NDI Error") 
                msgBox.exec_()
                return
        if self.createDialog.checkBoxMicrophone.isChecked():
            #TODO
            self.mainWindow.sensorList["Microphone"] = None
            self.mainWindow.HzSetting["Microphone"] = self.createDialog.spinBoxMicrophone.value()
        if self.createDialog.checkBoxIMU.isChecked():
            #TODO
            self.mainWindow.sensorList["IMU"] = None
            self.mainWindow.HzSetting["IMU"] = self.createDialog.spinBoxIMU.value()
        if self.createDialog.checkBoxCurrent.isChecked():
            #TODO
            self.mainWindow.sensorList["Current"] = None
            self.mainWindow.HzSetting["Current"] = self.createDialog.spinBoxCurrent.value()
        if self.createDialog.checkBoxFT.isChecked():
            #TODO
            self.mainWindow.sensorList["FT"] = None
            self.mainWindow.HzSetting["FT"] = self.createDialog.spinBoxFT.value()
        if not self.mainWindow.sensorList:
            msgBox = QMessageBox()
            msgBox.setText("Please select at least one type of sensor.")
            msgBox.setWindowTitle("Sensor Type Error") 
            msgBox.exec_()
            return
        Database = SmartDrillDataBase.create(self.mainWindow.sensorList)
        for i in self.mainWindow.sensorList:
            Database.data[i].Hz = self.mainWindow.HzSetting[i]
        self.mainWindow.unsaved = True
        self.mainWindow.NDISetting = config.NDISetting
        self.mainWindow.resetHz()
        self.mainWindow.createVis()
        self.mainWindow.Database = Database
        self.close()