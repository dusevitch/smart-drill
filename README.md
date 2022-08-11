# Smart Drill GUI 

This code builds a Python GUI for controlling sensors linked for a smart drilling platform for medical tasks. The immediate application is spinal drilling and tissue detection for laminectomy tasks but has various other drilling applications in the orthopedic, ENT, and neurosurgery space.


## Installation
Installation of this program depends on the hardware and the software components listed below:


### **<u>Hardware</u>**


**SENSORS**
The following sensors can be configured:
1. **IMU**: Data extracted from a BNO055, Adafruit IMU (100 HZ) running 
2. **Current Sensor**: 
3. **High Frequency Microphone**: 
4. **Force/Torque Sensor**: 

**OTHER HARDWARE**
1. **Arduino Uno**: Single Unit with usb cord
2. **Power Supply**: Some power supply to run the 
3. **Preamp for Microphone**: This work uses an AudioBox Usb preamp, but most preamps with associated Drivers installed should work as long as Reaper can detect them. 
2. **Drill Attachment**: See CAD file attached
3. **Retroreflective Spheres (NDI)**: These can be purchased here
4. **NDI Polaris Stereocamera System**: System for Tracking the Spheres and Calibration
    - NDI Architect 6D necessary for generating custom .ROM files


### **<u>Software Dependencies</u>**
1. **Python 3.10**: I like to set 
    - PyQt5: For the Gui
2. **Reaper**: v.
3. **Arduino**:
4. **CISST NDI**: 
5. **Slicer 3D**: Slicer is used to gather CT data of pieces and and also for registration during testing
    - Registration Package


## Using the Platform

### **<u>GUI Use</u>**
The GUI is written with PyQt5 and can operate any of the sensors. For full functionality, the GUI must be run in ReaScript so as to be able to control the recording of the microphone in time with the other platforms.

### **<u>To Run</u>**
1. Turn on Ardino unit with IMU/Current sensor
2. Attach F/T Sensor (if using)
3. Turn on Polaris, ensure correct .ROM for tool is loaded (you might have to generate new .ROM file for each drill bit using NDI Architect) 
3. Open Reaper, run ReaScript "record_widget.py"


### **<u>TODO (Future)</u>**
1. Remove Reaper Reliance
2. ROS 2 Package integration