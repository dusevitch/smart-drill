
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QCheckBox, QGridLayout, QGroupBox, QHBoxLayout, QDialog
app = QApplication([])
app.setStyle('Fusion')

class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        self.originalPalette = QApplication.palette()
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        
        self.setWindowTitle("Smart Drill Recording GUI")
        self.setLayout(mainLayout)
    
    def topGroupBox(self):
        self.topGroupBox = QGroupBox("File")
            
    
    def createTopLeftGroupBox(self):
        self.topLeftGroupBox = QGroupBox("Settings")

        radioButtonMicrophone = QCheckBox("Microphone")
        radioButtonIMUSensor = QCheckBox("IMU")
        radioButtonCurrentSensor = QCheckBox("Current Sensor")
        radioButtonFTSensor = QCheckBox("F/T Sensor")
        radioButtonMicrophone.setChecked(True)
        radioButtonIMUSensor.setChecked(True)
        radioButtonCurrentSensor.setChecked(True)

        # fileLabel = QLabel("FileName")
        # filePath = QLineEdit()

        layout = QVBoxLayout()
        layout.addWidget(radioButtonMicrophone)
        layout.addWidget(radioButtonIMUSensor)
        layout.addWidget(radioButtonCurrentSensor)
        layout.addWidget(radioButtonFTSensor)
        
        # layout.addWidget(fileLabel)
        # layout.addWidget(filePath)
        
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    


    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Controls")

        recordPushButton = QPushButton("Record")
        recordPushButton.setCheckable(True)
        stopPushButton = QPushButton("Stop")
        
        pausePushButton = QPushButton("Pause")
        pausePushButton.setCheckable(True)
        
        layout = QVBoxLayout()
        layout.addWidget(recordPushButton)
        layout.addWidget(stopPushButton)
        layout.addWidget(pausePushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    # SIGNALS AND SLOT DEFINITIONS
    def on_record_button_clicked():
        return 1
    
    def on_stop_button_clicked():
        return 1
    
    def on_pause_button_clicked():
        return 1
    
    def browseFiles(self):
        fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:\User\dusev\Downloads\python_drill')
        self.filename.setText(fname[0])
        
if __name__ == '__main__':
    gallery = WidgetGallery()
    gallery.show()
    app.exec()