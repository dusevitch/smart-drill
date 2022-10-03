# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/jerry/Desktop/smart-drill/GUI/NDI_setting.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import json
from configparser import ConfigParser

class Ui_settingNDI(object):
    def setupUi(self, settingNDI):
        settingNDI.setObjectName("settingNDI")
        settingNDI.resize(393, 143)
        self.JSON = QtWidgets.QLabel(settingNDI)
        self.JSON.setGeometry(QtCore.QRect(20, 20, 71, 17))
        self.JSON.setObjectName("JSON")
        self.lineEditJSON = QtWidgets.QLineEdit(settingNDI)
        self.lineEditJSON.setGeometry(QtCore.QRect(100, 20, 241, 25))
        self.lineEditJSON.setObjectName("lineEditJSON")
        self.Portal = QtWidgets.QLabel(settingNDI)
        self.Portal.setGeometry(QtCore.QRect(20, 60, 81, 17))
        self.Portal.setObjectName("Portal")
        self.lineEditPORTAL = QtWidgets.QLineEdit(settingNDI)
        self.lineEditPORTAL.setGeometry(QtCore.QRect(100, 60, 241, 25))
        self.lineEditPORTAL.setObjectName("lineEditPORTAL")
        self.buttonBox = QtWidgets.QDialogButtonBox(settingNDI)
        self.buttonBox.setGeometry(QtCore.QRect(120, 100, 166, 25))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.pushButton = QtWidgets.QPushButton(settingNDI)
        self.pushButton.setGeometry(QtCore.QRect(350, 20, 31, 25))
        self.pushButton.setObjectName("pushButton")
        self.retranslateUi(settingNDI)
        QtCore.QMetaObject.connectSlotsByName(settingNDI)

    def retranslateUi(self, settingNDI):
        _translate = QtCore.QCoreApplication.translate
        settingNDI.setWindowTitle(_translate("settingNDI", "NDI Setting"))
        self.JSON.setText(_translate("settingNDI", "JSON File:"))
        self.Portal.setText(_translate("settingNDI", "I/O Portal:"))
        self.pushButton.setText(_translate("settingNDI", "..."))
    
    def initialize(self,NDISetting):
        self.jsonFile = NDISetting["JSON"]
        self.portal = NDISetting["PORTAL"]
        self.lineEditJSON.text = self.jsonFile
        self.lineEditPORTAL = self.portal
        self.buttonBox.accepted.connect(self.save)
        print("here")
        self.buttonBox.rejected.connect(lambda:self.close())
        self.pushButton.clicked.connect(self.loadFile)
        print("here")
        
    def loadFile(self):
        self.jsonFile, _ = QtWidgets.QFileDialog.getOpenFileName(None, "Load data",
                                                   "", "JSON Files (*.json)")
        if file:
            try:
                with open(self.jsonFile,"rb") as f:
                    jsonObject = json.load(f)
                self.portal = jsonObject["serial-port"]
                self.lineEditPORTAL = self.portal
            except:
                QMessageBox.about(self, "Error", "Not a valid NDI6D json file.")
    
    def save(self):
        conf = ConfigParser()
        conf["NDI"] = {"JSON":self.jsonFile,"PORTAL":self.portal}
        with open("/tmp/SmartDrillDataCollectorNDICache.ini","w+") as f:
            conf.write(f)

