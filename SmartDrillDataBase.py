import numpy as np
import json
import pandas as pd
from pathlib import Path
import config

def LoadDataPoint(info):
    csvData = pd.read_csv(info["data"], sep=',', header=0)
    data = csvData.values.tolist()
    Count = data.shape[0]
    Hz = info["Hz"]
    return mapSensorType(info)(data,Count,Hz)

def mapSensorType(DataPoint):
    sensorType = DataPoint["sensorType"]
    if sensorType == "NDI":
        return NDIDataPoint
    elif sensorType == "Microphone":
        return MicrophoneDataPoint
    elif sensorType == "IMU":
        return IMUDataPoint
    elif sensorType == "Current":
        return CurrentDataPoint
    elif sensorType == "FT":
        return FTDataPoint
    else:
        raise("Undefined Data type")  

def createDataPoint(sensorType):
    if sensorType == "NDI":
        return NDIDataPoint([],0,int(config.Hz["NDI"]))
    elif sensorType == "Microphone":
        return MicrophoneDataPoint([],0,int(config.Hz["Microphone"]))
    elif sensorType == "IMU":
        return IMUDataPoint([],0,int(config.Hz["IMU"]))
    elif sensorType == "Current":
        return CurrentDataPoint([],0,int(config.Hz["Current"]))
    elif sensorType == "FT":
        return FTDataPoint([],0,int(config.Hz["FT"]))
    else:
        raise("Undefined Data type") 

class DataPoint(object):
    def __init__(self,data,Count,Hz):
        self.interpret = ["Stamp","x","y","z","Rx","Ry","Rz","Rw"]
        self.data = data
        self.Hz = Hz
        self.Count = Count
        self.sensorType = "Default"
        
    def save(self,path):
        pdData = pd.DataFrame(self.data)
        with open(path,"w+") as f:
            pdData.to_csv(f, header=self.interpret)
            
class NDIDataPoint(DataPoint):
    def __init__(self,data,Count,Hz):
        super(NDIDataPoint,self).__init__(data,Count,Hz)
        self.interpret = ["Stamp","x","y","z","Rx","Ry","Rz","Rw"]
        self.sensorType = "NDI"
        
class MicrophoneDataPoint(DataPoint):
    def __init__(self,data,Count,Hz):
        super(MicrophoneDataPoint,self).__init__(data,Count,Hz)
        self.interpret = ["Stamp","x"]
        self.sensorType = "Microphone"
        
class IMUDataPoint(DataPoint):
    def __init__(self,data,Count,Hz):
        super(IMUDataPoint,self).__init__(data,Count,Hz)
        self.interpret = ["Stamp","x","y","z","w"]
        self.sensorType = "IMU"
        
class CurrentDataPoint(DataPoint):
    def __init__(self,data,Count,Hz):
        super(CurrentDataPoint,self).__init__(data,Count,Hz)
        self.interpret = ["Stamp","A"]
        self.sensorType = "Current"
        
class FTDataPoint(DataPoint):
    def __init__(self,data,Count,Hz):
        super(FTDataPoint,self).__init__(data,Count,Hz)
        self.interpret = ["Stamp","Fx","Fy","Fz","Tx","Ty","Tz"]   
        self.sensorType = "FT"
        
class SmartDrillDataBase(object):
    def __init__(self,info,data):
        self.info = info
        self.data = data
        self.iterator_count = 0

    @classmethod   
    def load_from(self,filePath):
        info = {}
        data = {}
        with open(filePath,"r") as f:
            info = json.load(f)
        for i in info:
            data[i]=LoadDataPoint(info[i]) 
        return self(info,data)
        
    def save(self,jsonPath):
        jsonPath = Path(jsonPath)
        filename = jsonPath.stem
        saveJson = {}
        for i in self.data:
            csvPath = jsonPath.parent / (filename + i + ".csv")
            self.data[i].save(str(csvPath))
            saveJson[i] = {"sensorType":i,"Hz":self.data[i].Hz,"data":filename + i + ".csv","duration":self.info[i]["duration"]}
        with open(jsonPath,"w+") as f:
            json.dump(saveJson, f)

    @classmethod
    def create(self,sensorList = ["NDI","Microphone","IMU","FT","Current"]):
        dataList = {}
        info = {}
        for i in sensorList:
            dataList[i] = createDataPoint(i)
            info[i] = {"sensorType":i,"data":[],"Hz":config.Hz[i],"Count":0,"duration":0}

        return self(info,dataList)
    
    def update(self,sensortype,data,duration):
        self.data[sensortype].data = data
        self.data[sensortype].Count = len(data)
        self.info[sensortype]["Count"] = len(data)
        self.info[sensortype]["duration"] = duration

    def __iter__(self):
        return self

    def __next__(self):
        self.iterator_count += 1
        if self.iterator_count >= len(self.data):
            raise StopIteration()
        return self.data[self.iterator_count]
