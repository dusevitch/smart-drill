from symbol import while_stmt
import rospy
from geometry_msgs.msg._WrenchStamped import WrenchStamped
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

class FT(Sensor):
    def __init__(self,Hz,mainWindow,FTSetting):
        super().__init__(Hz,mainWindow,"FT")
        self.FTSetting = FTSetting
        #self.connectPub = rospy.Publisher('NDI/connect',Bool, queue_size=10)
        #self.trackPub = rospy.Publisher("NDI/track",Bool,queue_size=10)
        self.FT_data = WrenchStamped()
        self.axis = self.figure.add_subplot(111)

    def init(self):
        if not self.isInitialized:
            try:
                rospy.init_node('smart_drill_data_collection')
            except:
                raise
            # rospy.init_node('smart_drill_data_collection', anonymous=True)
            self.stream()
            self.isInitialized = True

    def _stream(self):
        self.tool_sub = rospy.Subscriber(self.FTSetting["Topic"], 
        WrenchStamped, self.tool_sub_callback)
        rospy.spin()

    def getFrame(self):
        intervavl = np.linspace(0, self.Hz, num=self.Hz, endpoint=False)
        self.axis.plot(intervavl, [i[1] for i in self.data[-self.Hz:]])
        self.axis.plot(intervavl, [i[2] for i in self.data[-self.Hz:]])
        self.axis.plot(intervavl, [i[3] for i in self.data[-self.Hz:]])
        self.axis.plot(intervavl, [i[4] for i in self.data[-self.Hz:]])
        self.axis.plot(intervavl, [i[5] for i in self.data[-self.Hz:]])
        self.axis.plot(intervavl, [i[6] for i in self.data[-self.Hz:]])
        
    def tool_sub_callback(self,data):
        if self.streaming:
            self.FT_data = data
            self.data.append([self.FT_data.header.stamp,
                    self.FT_data.wrench.force.x,
                    self.FT_data.wrench.force.y,
                    self.FT_data.wrench.force.z,
                    self.FT_data.wrench.torque.x,
                    self.FT_data.wrench.torque.y,
                    self.FT_data.wrench.torque.z])