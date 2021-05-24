import serial
import os
import time



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
        datano = 0
        while os.path.exists(self.joinpath(f"Flight_3571_C-{datano}.csv")):
            datano += 1
        self.PATH.append(self.joinpath(f"Flight_3571_C-{datano}.csv"))
        datano = 0
        while os.path.exists(self.joinpath(f"Flight_3571_SP1-{datano}.csv")):
            datano += 1
        self.PATH.append(self.joinpath(f"Flight_3571_SP1-{datano}.csv"))
        datano = 0
        while os.path.exists(self.joinpath(f"Flight_3571_SP2-{datano}.csv")):
            datano += 1
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
                        print("inc")
                        # Data[2] = self.isInt(Data[2])  # packetcount
                        # Data[4] = self.isChar(Data[4])  # flightmode
                        # Data[5] = self.isChar(Data[5])  # sp1r
                        # Data[6] = self.isChar(Data[6])  # sp2r
                        # Data[7] = self.isFloat(Data[7])  # altitude
                        # Data[8] = self.isFloat(Data[8])  # temp
                        # Data[9] = self.isFloat(Data[9])  # voltage
                        # Data[11] = self.isFloat(Data[11])  # lat
                        # Data[12] = self.isFloat(Data[12])  # long
                        # Data[13] = self.isFloat(Data[13])  # Galt
                        # Data[14] = self.isInt(Data[14])  # Gsat
                        # Data[15] = self.isChar(Data[15])  # state
                        # Data[16] = self.isInt(Data[16])  # sp1count
                        # Data[17] = self.isInt(Data[17])  # sp2count
                        # Data[18] = self.isChar(Data[18])  # echo
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
    A.connect_port(9600)
    print(A.reading())
