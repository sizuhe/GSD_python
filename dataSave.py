import pandas as pd
import time
import os



class dataSave:
    def __init__(self):
        self.signalData = False
        self.time = 0
        self.dataList = []
        self.timeList = []

        # Creating folder 'saves'
        filePath = str(os.path.abspath(__file__))
        filePath = filePath.replace('dataSave.py','saves')

        if not os.path.exists(filePath):
            os.makedirs(filePath)

    # LCD time updater
    def LCD(self, lcdWidget):
        if self.signalData == True:
            self.time += 1
            lcdWidget.setProperty("value", self.time)
        else:
            pass

    # Saving data to lists
    def Save(self, timePacket, dataPacket):
        if self.signalData == True:
            self.dataList.append(float(dataPacket))
            self.timeList.append(float(timePacket))
            self.refTime = self.timeList[0]
            self.filename = "save" + time.strftime('_%H-%M-%S')
        else:
            self.dataList = []
            self.timeList = []

    def Stop(self, lcdWidget):
        self.signalData = False
        self.time = 0
        lcdWidget.setProperty("value", 0)

        # Time list starts at 0
        if len(self.timeList) > 0:
            self.refTime = self.timeList[0]
            for pos,value in enumerate(self.timeList):
                self.timeList[pos] = value - self.refTime
                # self.timeList[pos] = round(self.timeList[pos], 2)

            # Name differentiation
            dataDir = "saves/" + self.filename + ".csv"

            # Saving data to a CSV file
            dataDF = pd.DataFrame({"Time":self.timeList, "Data values":self.dataList})
            dataDF.to_csv(dataDir, header=False, index=False)

    def signalStart(self):
        self.signalData = True