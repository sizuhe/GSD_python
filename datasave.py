import pandas as pd
import time
import os



class DataSave:
    def __init__(self, graphcounter):
        self.graphcounter = graphcounter
        self.signalData = False
        self.time = 0
        self.timeList = []
        self.dataLists = [[] for _ in range(self.graphcounter)]

        # Creating folder 'saves'
        filePath = str(os.path.abspath(__file__))
        filePath = filePath.replace('datasave.py','saves')

        if not os.path.exists(filePath):
            os.makedirs(filePath)

    # LCD time updater
    def LCD(self, lcdWidget):
        if self.signalData == True:
            self.time += 1
            lcdWidget.setProperty("value", self.time)

    # Saving data to lists
    def Save(self, timePacket, *dataPackets):
        if self.signalData == True:
            self.timeList.append(float(timePacket))
            self.refTime = self.timeList[0]

            # Saving data on respective list
            for pos,packet in enumerate(dataPackets):
                self.dataLists[pos].append(float(packet))
        else:
            self.dataLists = [[] for _ in range(self.graphcounter)]
            self.timeList = []

    def Stop(self, lcdWidget):
        self.signalData = False
        self.time = 0
        lcdWidget.setProperty("value", 0)

        # Data processing for each packet
        if len(self.timeList) > 0:
            for pos0 in range(self.graphcounter):
                # Time data organization
                self.refTime = self.timeList[0]
                for pos1,value in enumerate(self.timeList):
                    self.timeList[pos1] = value - self.refTime

                # Name differentiation
                dataDir = "saves/" + time.strftime('%H-%M-%S_') + "Graph" + str(pos0+1) + ".csv"

                # Saving data to various CSV files
                actualList = self.dataLists[pos0]
                dataDF = pd.DataFrame({"Time":self.timeList, 
                                       "Data values":actualList})
                try:
                    dataDF.to_csv(dataDir, header=False, index=False)
                except Exception as error:
                    print("Error datasave - Save to csv")
                    print(error)

    def signalStart(self):
        self.signalData = True
