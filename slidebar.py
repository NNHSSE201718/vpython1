from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
print(vpython.__version__)

global all_graphs = [[0,0,1,0],[0,0,1,0],[0,0,1,0]]
print(all_graphs)
def setAmplitude(s):
    


def createGraph(graph_list):
    graph_sumtrig(graph_list,color.blue)


bar1 = slider(min=0, max=5, value=3, length=100, bind=createGraph(all_graphs), right=90)
