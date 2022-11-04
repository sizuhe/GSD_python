import pyqtgraph as pg
import numpy as np

class Graph4(pg.PlotItem):
    def __init__(self):
        super().__init__()
        self.plotGraph = self.plot()
        self.dataGraph = np.linspace(0, 0, 15)

    def update(self, value):
        self.dataGraph[:-1] = self.dataGraph[1:]
        self.dataGraph[-1] = float(value)
        self.plotGraph.setData(self.dataGraph)
