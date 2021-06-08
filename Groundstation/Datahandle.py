import serial
import os
import time
from datetime import datetime,date



class Port:
    def __init__(self, device=None):
        self.PortName = []
        self.PortFullName = []
        self.PortList = self.list_ports()
        self.pkg = ''
        self.device = device
        self.endpoint = '$'
        self.path()

    @staticmethod
    def list_ports():
        comall = []
        for i in range(256):
            comtest = 'COM' + str(i)
            try:
                serial.Serial(comtest)
            except:
                pass
            else:
                comall.append(comtest)
        return comall

    def connect_port(self, baudrate):
        try:
            self.device = serial.Serial(self.device, baudrate=int(baudrate), timeout=60)
        except:
            print("[Cannot connect port]")

    def read(self):
        telemetry = self.device.read().decode('utf-8')
        alldata = ''
        while telemetry != "$":
            alldata += telemetry
            telemetry = self.device.read().decode('utf-8')
        alldata.replace('\r', '')
        alldata.replace('\n', '')
        return alldata

    def path(self):
        self.PATH = []
        stime = datetime.now().time()
        today = date.today()
        timestp = str('%02d' % stime.hour) + '_' + str('%02d' % stime.minute)
        datano = str(timestp) + '_' + str(today.strftime("%b-%d-%Y"))
        self.PATH.append(self.joinpath(f"Flight_3571_C-{datano}.csv"))
        self.PATH.append(self.joinpath(f"Flight_3571_SP1-{datano}.csv"))
        self.PATH.append(self.joinpath(f"Flight_3571_SP2-{datano}.csv"))

    @staticmethod
    def joinpath(name):  # join pathname
        path = 'FLIGHT/' + name
        return str(path)

    @staticmethod
    def isFloat(num):
        num = float(num)
        if isinstance(num, float):
            return str(num)
        else:
            return "N/A"

    @staticmethod
    def isChar(cha):
        if isinstance(cha, str):
            return cha
        else:
            return "N/A"

    @staticmethod
    def isInt(num):
        if isinstance(int(num), int):
            return num
        else:
            return "N/A"

    def reading(self):
        recieved = ''
        while True:
            try:
                recieved = self.read()
                # print(recieved)
                if recieved != "":
                    recieved = recieved.replace('\r', '')
                    recieved = recieved.replace('\n', '')
                    Data = recieved.split(',')

                    # checkdata
                    print(f"[READING] : {Data}")
                    if Data[3] == 'C':

                        with open(self.PATH[0], 'a') as file:
                            for i in range(len(Data)):
                                file.write(Data[i])
                                file.write(',')
                            file.write("\n")
                        return Data

                    elif Data[3] == 'S1':  # team,time,pkg,s1,alt,temp,rotation,latitude,longitude
                        self.isInt(Data[2])
                        self.isFloat(Data[4])
                        self.isFloat(Data[5])
                        self.isFloat(Data[6])
                        self.isFloat(Data[7])
                        self.isFloat(Data[8])
                        with open(self.PATH[1], 'a') as file:
                            for i in range(len(Data)):
                                file.write(Data[i])
                                file.write(',')
                            file.write("\n")
                        return Data

                    elif Data[3] == 'S2':
                        self.isInt(Data[2])
                        self.isFloat(Data[4])
                        self.isFloat(Data[5])
                        self.isFloat(Data[6])
                        self.isFloat(Data[7])
                        self.isFloat(Data[8])
                        with open(self.PATH[2], 'a') as file:
                            for i in range(len(Data)):
                                file.write(Data[i])
                                file.write(',')
                            file.write("\n")
                        return Data
                    else:
                        return Data
            except:
                pass

if __name__ == "__main__":
    A = Port('COM11')
    A.path()
    print(A.PATH)

