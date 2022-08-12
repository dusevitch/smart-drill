
import serial.tools.list_ports
import serial


# To view available ports run this in the command line:
# python -m serial.tools.list_ports

# Variable Initialization
arduino_error_flag = 0
baudrate = 115200

# Automatically Detect the Arduino Uno Port
ports = list(serial.tools.list_ports.comports())
for p in ports:
    if p[1].find('Arduino Uno')!=-1:
        print('Arduino Uno found on ' + p[0])
        com_port = p[0]
        arduino_error_flag = 1 # arduino Uno found, good to proceed

# Load the Arduino from the correct port, and handle errors
try:
    if arduino_error_flag:
        arduino_dev = serial.Serial(com_port, baudrate=115200)
except Exception as e:
    print(str(e))
    print("Arduino Uno unit could not be found. Please check the Port is correct")
    
    # print("Arduino Uno unit could not be found. Please check the Port is correct")
    
# if check_flags:
# while True:
#     print(arduino_dev.readline())


# # Function to check all selected sensors have been found and are ready for recording
# def check_flags():
#     if arduino_error_flag and 