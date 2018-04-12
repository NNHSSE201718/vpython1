from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
print(vpython.__version__)

amt_of_bars = 5
all_graphs = []
for i in range(amt_of_bars):
    all_graphs.append([0,0,1,0])

def setAmplitude(s):
    global all_graphs
    global allBars
    all_graphs[allBars.index(s)][1]=s.value
    print(all_graphs)
    createGraph()
def createGraph():
    global all_graphs
    graph_sumtrig(all_graphs,color.blue)

allBars = []
for i in range(amt_of_bars):
    allBars.append(slider(min=0, max=5, value=3, length=100, bind=setAmplitude, right=90))
