from platform import release
import serial
import serial.tools.list_ports
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QVBoxLayout, QCheckBox, QGridLayout, QGroupBox, QHBoxLayout, QDialog, QLabel

app = QApplication([])
app.setStyle('Fusion')



class WidgetGallery(QDialog):
    def __init__(self, parent=None):
        super(WidgetGallery, self).__init__(parent)

        
        # Arduino Variable Initialization
        self.arduino_error_flag = 0
        self.baudrate = 115200

        self.originalPalette = QApplication.palette()
        self.createTopLeftGroupBox()
        self.createTopRightGroupBox()
        self.createArduinoGroupBox()
        
        mainLayout = QGridLayout()
        mainLayout.addWidget(self.topLeftGroupBox, 1, 0)
        mainLayout.addWidget(self.topRightGroupBox, 1, 1)
        mainLayout.addWidget(self.arduinoGroupBox, 1, 2)
        
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
        sensorCheckLabel = QLabel("Check Sensor Boxes to include sensors in File Output")
        
        layout = QVBoxLayout()
        layout.addWidget(radioButtonMicrophone)
        layout.addWidget(radioButtonIMUSensor)
        layout.addWidget(radioButtonCurrentSensor)
        layout.addWidget(radioButtonFTSensor)
        
        # layout.addWidget(fileLabel)
        # layout.addWidget(filePath)
        
        layout.addStretch(1)
        self.topLeftGroupBox.setLayout(layout)    

    def createArduinoGroupBox(self):
        self.arduinoGroupBox = QGroupBox("Arduino Sensors")
        
        #items
        initializeArduino = QPushButton("Initialize Arduino")
        initializeArduino.clicked.connect(self.on_arduino_initialize_clicked)
        IMULiveStream = QPushButton("Stream IMU Data")
        IMULiveStream.setCheckable(True)
        currentSensorLiveStream = QPushButton("Stream Current Sensor")
        currentSensorLiveStream.setCheckable(True)
        # radioButtonIMUSensor = QCheckBox("IMU")
        # radioButtonCurrentSensor = QCheckBox("Current Sensor")
        # TODO include LED Lights to see activated sensors
        # IMULed = img
        # currentLed = 
        
        #items layout
        IMULayout = QHBoxLayout()
        # IMULayout.addWidget(radioButtonIMUSensor)
        IMULayout.addWidget(IMULiveStream)
        
        currentLayout = QHBoxLayout()
        # currentLayout.addWidget(radioButtonCurrentSensor)
        currentLayout.addWidget(currentSensorLiveStream)
        
        layout = QVBoxLayout()
        layout.addWidget(initializeArduino)
        layout.addLayout(IMULayout)
        layout.addLayout(currentLayout)
        
        layout.addStretch(1)
        self.arduinoGroupBox.setLayout(layout)

    def createTopRightGroupBox(self):
        self.topRightGroupBox = QGroupBox("Controls")

        self.recordPushButton = QPushButton("Record")
        self.recordPushButton.setCheckable(True)
        self.recordPushButton.clicked.connect(self.on_record_button_clicked)
        stopPushButton = QPushButton("Stop")
        
        # pausePushButton = QPushButton("Pause")
        # pausePushButton.setCheckable(True)
        
        layout = QVBoxLayout()
        layout.addWidget(self.recordPushButton)
        layout.addWidget(stopPushButton)
        # layout.addWidget(pausePushButton)
        layout.addStretch(1)
        self.topRightGroupBox.setLayout(layout)

    # SIGNALS AND SLOT DEFINITIONS
    def on_record_button_clicked(self):
        # TODO: Check which boxes are checked to know which flags to check before recording
        if self.arduino_error_flag:
            while self.recordPushButton.isChecked():
                self.stream_arduino_data()
        else: # TODO: add this output to the GUI error message box
            print("Error with recording. One of the sensors is not initialized (stil 0):\n")
            print('arduino_error_flag: ' + self.arduino_error_flag)
    
    def on_stop_button_clicked(self):
        return 1
    
    def on_arduino_initialize_clicked(self):
        # Automatically Detect the Arduino Uno Port
        ports = list(serial.tools.list_ports.comports())
        for p in ports:
            if p[1].find('Arduino Uno') != -1:
                print('Arduino Uno found on ' + p[0])
                com_port = p[0]
                self.arduino_error_flag = 1  # arduino Uno found, good to proceed

        # Load the Arduino from the correct port, and handle errors
        try:
            if self.arduino_error_flag:
                self.arduino_dev = serial.Serial(com_port, baudrate=self.baudrate)
        except Exception as e:
            print(str(e))
            print("Arduino Uno unit could not be found. Please check the Port is correct")
    
    # TODO make a streaming function to see live stream updating (check to make sure data is incoming)
    def on_arduino_stream_clicked(self):
        return 1
    
    # def on_pause_button_clicked():
    #     return 1
    
    def stream_arduino_data(self):
        print(self.arduino_dev.readline())
    
    # def browseFiles(self):
    #     fname = QFileDialog.getOpenFileName(self, 'Open File', 'C:\User\dusev\Downloads\python_drill')
    #     self.filename.setText(fname[0])
        
if __name__ == '__main__':
    gallery = WidgetGallery()
    gallery.show()
    app.exec()