import pyqtgraph as pg
import numpy as np



class graphName2(pg.PlotItem):
    def __init__(self):
        super().__init__()
        # Zero values to replace with real data
        self.plotGraph = self.plot()
        self.dataGraph = np.linspace(0, 0, 15)

    def update(self, data):
        self.dataGraph[:-1] = self.dataGraph[1:]
        self.dataGraph[-1] = float(data)
        self.plotGraph.setData(self.dataGraph)