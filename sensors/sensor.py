import numpy as np
import time
import threading
import ctypes
import inspect
from abc import ABC, abstractmethod
import matplotlib as plt
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar)
from multiprocessing import Process

class Sensor(ABC):
    def __init__(self,Hz,mainWindow,sensorType):
        self.Hz = int(Hz)
        self.mainWindow = mainWindow
        self.data = []
        self.backgroundProcessStream = None
        self.backgroundProcessVisualization = None
        self.sensorType = sensorType
        self.figure = plt.figure.Figure()
        self.axis = self.figure.add_subplot(111)
        self.axis.set_aspect(1)
        self.axis.set_title(self.sensorType)
        self.canvas = FigureCanvas(self.figure)
        self.canvas.draw()
        self.isInitialized = False
        self.streaming = False  

    def init(self):
        # Function that configs sensor. Remember to set self.isInitialized = True as the last line. 
        self.stream()


    @abstractmethod
    def _stream(self):
        # The virtual function to steaming data into self.data. This function must be overloaded.
        # We recommend to write in a while loop:
        while True:
            if self.streaming:
                self.data.append([]) # read your sensor output and append it into self.data

    @abstractmethod
    def getFrame(self,time):
        # Update the self.axis to a frame of the latest one second
        pass

    def _endStream(self):
        # You may want to overload this function if you are using ros.
        pass


    def stream(self):
        self.backgroundProcessStream = threading.Thread(target = self._stream)
        self.backgroundProcessVisualization = threading.Thread(target = self.visualization)
        self.backgroundProcessStream.start()
        time.sleep(0.01)
        self.backgroundProcessVisualization.start()
        time.sleep(0.01)

    def __len__(self):
        return len(self.data)

    def update(self):
        # The build-in function do the sensor data collection under thread, in background.
        #elf.visualizing = True
        self.streaming = True
        
    def stop(self):
        # This function will stop appending data into self.data, but will not stop streaming
        self.streaming = False
        # self.visualizing = False

    def kill(self):
        # Build-in function to stop data collection by kill the thread.
        self.streaming = False
        self.visualizing = False
        self._endStream()

        self.backgroundProcessStream.join()
        self.backgroundProcessVisualization.join()
        self.backgroundProcessStream = None
        self.backgroundProcessVisualization= None

    def clear(self):
        # Built-in function to clean the data collected.
        self.data = []
        self.axis.clear()

    # def getData(self,time):
    #     # Return data within certain tim stamp. Only integer are allowed.
    #     assert (len(time) == 1) or (len(time) == 2),"time argument should be in size 1 or 2"
    #     if len(time) == 1:True
    #     assert start_index <= (len(self.data) - 1),"Try to get data beyond valid time stamp."
    #     if end_index > (len(self.data) - 1):
    #         end_index = len(self.data) - 1  
    #     return self.data[start_index,end_index]

    def visualization(self):
        while True:
            if self.streaming:
                try:
                    self.axis.clear()
                    self.getFrame()
                    self.figure.tight_layout()
                    self.canvas.draw()
                except:
                    pass
                    #print("Missing plot for sensor {}".format(self.sensorType))
            else:
                try:
                    self.axis.clear()
                except:
                    pass
            