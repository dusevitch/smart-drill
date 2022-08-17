# Smart Drill GUI 

This code builds a Python GUI for controlling sensors linked for a smart drilling platform for medical tasks. The immediate application is spinal drilling and tissue detection for laminectomy tasks but has various other drilling applications in the orthopedic, ENT, and neurosurgery space.


## Installation
Installation of this program depends on the hardware and the software components listed below:


### **<u>Hardware</u>**


**SENSORS**
The following sensors can be configured:
1. **IMU**: Data extracted from a BNO055, Adafruit IMU (100 HZ). Theres a setup page [here](https://learn.adafruit.com/adafruit-bno055-absolute-orientation-sensor) 
2. **Current Sensor**: 32.5mm diameter, Measuring Range AC/DC 0-100amps, Output Signal 0-5V, [Hall Effect Current Sensor](https://www.ato.com/hall-effect-current-sensor-20a-to-2000a?affiliate=shopping&gclid=CjwKCAjw0dKXBhBPEiwA2bmObQ5OSWntZQFYQCi-ZZZS-ALRPwt0HOrH3kyMgdXkIS0IxyknPLNv9xoCYfcQAvD_BwE)
3. **High Frequency Microphone**: Earthworks 50k Omni Measurement Microphone from [Sweetwater](https://www.sweetwater.com/store/detail/M50--earthworks-m50-50khz-omnidirectional-measurement-microphone?main_web_category_rollup=2/23/105&mrkgadid=&mrkgcl=28&mrkgen=gpla&mrkgbflag=1&mrkgcat=drums&percussion&acctid=21700000001645388&dskeywordid=92700072478779155&lid=92700072478779155&ds_s_kwgid=58700007963105270&ds_s_inventory_feed_id=97700000007215323&dsproductgroupid=1720832031358&product_id=M50&prodctry=US&prodlang=en&channel=online&storeid=&device=c&network=u&matchtype=&adpos=largenumber&locationid=9007915&creative=615094225367&targetid=pla-1720832031358&campaignid=17962511191&awsearchcpc=&gclid=Cj0KCQjwgO2XBhCaARIsANrW2X1BCU2Z38AGIWfbqYU1OGVqii0Jh_oywba0EATVshacKn6OnbCR5OcaApjvEALw_wcB&gclsrc=aw.ds)
4. **Force/Torque Sensor**: Currently using an older model, Weiss 

**OTHER HARDWARE**
1. **Stryker Orthopedic Core Saber Drill Unit**:  Core Console w/ Power Cord, Bidirections Footswitch, Core Saber Drill, Elite 12 cm Drill Attachment, 4mm Precision Round 2-flute bur
1. **Arduino Uno**: Single Unit with usb cord
2. **Power Supply**: ? May not be necessary
3. **Microphone Audio Interface**: We're using a Focusrite Scarlett Solo 3rd Gen USB Audio Interface
2. **3D Printed Drill Attachment**: See CAD file attached, Use
3. **Retroreflective Spheres (NDI)**: These attach to the M3 Screws. They can be purchased at the [NDI Website here](https://www.ndigital.com/optical-measurement-technology/passive-marker-spheres/disposable-reflective-marker-sphere/)
4. **NDI Polaris Stereocamera System**: System for Tracking the Spheres and Calibration
    - NDI Architect 6D necessary for generating custom .ROM files


### **<u>Software Dependencies</u>**
1. **Python 3.10**:
    - PyQt5: For the Gui
2. **Reaper**: [Reaper DAW] (https://www.reaper.fm/)
3. **Arduino IDE**: [Arduino IDE](https://www.arduino.cc/en/software-)
4. **CISST sawNDITracker**: [https://github.com/jhu-saw/sawNDITracker](https://github.com/jhu-saw/sawNDITracker)
5. **Slicer 3D**: [3D Slicer](https://www.slicer.org/) is used to gather CT data of pieces and and also for registration during testing
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
1. Update CAD to attach to same drill position
2. Remove Reaper Reliance
2. ROS 2 Package integration