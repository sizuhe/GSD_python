import pandas as pd



class dataSave:
    def __init__(self):
        self.signal = False
        self.time = 0
        self.filename = ""
    
    def signalStart(self):
        self.signal = True

    # LCD time updater
    def LCD(self, lcdWidget):
        if self.signal == True:
            self.time += 1
            lcdWidget.setProperty("value", self.time)

    # Saving data to lists
    def Save(self, timePacket, dataPacket, nameFile):
        if self.signal == True:
            self.dataList.append(float(dataPacket))
            self.timeList.append(float(timePacket))
            self.refTime = self.timeList[0]
            self.filename = nameFile
        else:
            self.dataList = []
            self.timeList = []

    def Stop(self, lcdWidget):
        self.signal = False
        self.time = 0
        lcdWidget.setProperty("value", 0)

        # Time list starts at 0
        if len(self.timeList) > 0:
            self.refTime = self.timeList[0]
            for pos,value in enumerate(self.timeList):
                self.timeList[pos] = value - self.refTime

            # Name diferentiation
            dataDir = "saves/" + self.filename + ".csv"

            # Saving data to a CSV file
            dataDF = pd.DataFrame({"Time":self.timeList, "Data values":self.dataList})
            dataDF.to_csv(dataDir, header=False, index=False)