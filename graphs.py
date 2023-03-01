import pyqtgraph as pg
import numpy as np



class GraphPlot(pg.PlotItem):
    def __init__(self):
        super().__init__()
        # Zero values to replace with real data
        self.hideAxis("bottom")
        self.setLabel("left"," ")
        self.setMenuEnabled(False)
        self.getViewBox().setLimits(xMin=0, xMax=14)
        self.plotGraph = self.plot()
        self.plotGraph.setPen(255, 72, 0)
        self.dataGraph = np.linspace(0, 0, 15)

    def update(self, data):
        self.dataGraph[:-1] = self.dataGraph[1:]
        self.dataGraph[-1] = float(data)
        self.plotGraph.setData(self.dataGraph)
        
    def title(self, title):
        self.setTitle(title)