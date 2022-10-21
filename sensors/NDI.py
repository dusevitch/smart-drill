from symbol import while_stmt
import rospy
from geometry_msgs.msg import PoseStamped
import numpy as np
import matplotlib.pyplot as plt
import tf.transformations as tr
from pathlib import Path
from .sensor import Sensor
import time
import subprocess
import os
from mpl_toolkits.mplot3d import Axes3D
from scipy.spatial.transform import Rotation
import signal

class NDI(Sensor):
    def __init__(self,Hz,mainWindow,sawSetting,NDISetting):
        super().__init__(Hz,mainWindow,"NDI")
        self.sawSetting = sawSetting
        self.NDISetting = NDISetting
        #self.connectPub = rospy.Publisher('NDI/connect',Bool, queue_size=10)
        #self.trackPub = rospy.Publisher("NDI/track",Bool,queue_size=10)
        self.tool_sub = None
        self.tool_transform = PoseStamped()
        self.axis = self.figure.add_subplot(111,projection ='3d')

    def init(self):
        if not self.isInitialized:
            try:
                rospy.init_node('smart_drill_data_collection')
            except:
                    pass
            self.stream()
            self.isInitialized = True
        # if not self.isInitialized:
        #     try:
        #         self.setupSaw(Path(self.sawSetting["SAW"]),Path(self.NDISetting["JSON"]).resolve(),Path(self.NDISetting["PORTAL"]),self.Hz)
        #         #self.mainWindow.pubNotice(self.ros.communicate()[0])
        #         #self.connect = subprocess.Popen("rostopic pub /NDI/connect std_msgs/Bool true",stdout=subprocess.PIPE)
        #         #self.connectPub.publish(Bool(True))
        #         #self.mainWindow.pubNotice(self.connect.communicate()[0])
        #         #self.connect.terminate()
        #         #self.track = subprocess.Popen("rostopic pub /NDI/track std_msgs/Bool true",stdout=subprocess.PIPE)
        #         #os.system("gnome-terminal -e " + "'rostopic pub /NDI/track std_msgs/Bool true'")
        #         #self.trackPub.publish(Bool(True))
        #         #self.mainWindow.pubNotice(self.track.communicate()[0])
        #         #self.track.terminate()
        #         rospy.init_node('smart_drill_data_collection')
        #         self.stream()
        #         self.isInitialized = True
        #     except:
        #         raise
        #     # rospy.init_node('smart_drill_data_collection', anonymous=True)

    def _stream(self):
        self.tool_sub = rospy.Subscriber(self.sawSetting["rostopic"], 
        PoseStamped, self.tool_sub_callback)
        rospy.spin()

    def _endStream(self):
        rospy.signal_shutdown("Stop Data Collection")
        time.sleep(0.1)

    def getFrame(self):
        initial = np.array([[1,0,0],[0,1,0],[0,0,1]])
        rotation = Rotation.from_quat(self.data[-1][-4:]).as_matrix()
        initial = rotation @ initial
        
        self.axis.plot([0,initial[0,0]],[0,initial[1,0]],zs = [0,initial[2,0]],color = "r")
        self.axis.plot([0,initial[0,1]],[0,initial[1,1]],zs = [0,initial[2,1]],color = "g")
        self.axis.plot([0,initial[0,2]],[0,initial[1,2]],zs = [0,initial[2,2]],color = "b")

    def tool_sub_callback(self,transform):
        if self.streaming:
            self.tool_transform = transform
            self.data.append([self.tool_transform.header.stamp.secs,
                    self.tool_transform.pose.position.x,
                    self.tool_transform.pose.position.y,
                    self.tool_transform.pose.position.z,
                    self.tool_transform.pose.orientation.x,
                    self.tool_transform.pose.orientation.y,
                    self.tool_transform.pose.orientation.z,
                    self.tool_transform.pose.orientation.w])

    def setupSaw(self,path_to_nditracking,json,port,Hz):
        pass
    #     process1 = ["killall","-9","roscore"]
    #     subprocess.Popen(process1)
    #     process2 =  ["killall","-9","rosmaster"]
    #     subprocess.Popen(process2)
    #     time.sleep(1)
    #     subprocess.Popen("roscore")
    #     time.sleep(1)
    #     os.chdir(str(path_to_nditracking))
    #     #json = "/home/jerry/ros_catkin_ws/src/cisst-saw/sawNDITracker/share/SmartDrill.json"
    #     #port = "/dev/ttyUSB0"
    #     command = ["./ndi_tracker","-j",str(json),"-s",str(port),"-p",str(1 / Hz)]
    #     print(os.getcwd())
    #     self.saw = subprocess.Popen(command)
    #     time.sleep(0.1)
    #     #saw = subprocess.Popen(command,shell = True,stdout=subprocess.PIPE)