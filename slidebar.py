from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time

#set amplitude of the graph that is being changed
def setFrequency(s):
    global all_graphs
    global allBars
    global curve1
    global allTexts
    allTexts[allBars.index(s)].text=s.value
    all_graphs[allBars.index(s)][2]=s.value
    createGraph()

#create the graph by first deleting old code
def createGraph():
    global all_graphs
    global curve1
    global gd
    global visCurve
    time.sleep(.01)
    curve1.delete()
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd,visCurve)

#sphere()
amt_of_bars = 5
all_graphs = []
gd = graph(width=600, height=300,
      title='<b>The Greatest Curve of All Time</b>',
      xtitle='<i>x</i>', ytitle='<i>y</sup>',
      foreground=color.black, background=color.white,
      xmin=-4*math.pi, xmax=4*math.pi, ymin=-5, ymax=5)
curve1 = gcurve(color =color.blue,graph=gd )
allBars = []
allTexts = []
visCurve = curve()
#Create all the lists which contain the graphs
for i in range(amt_of_bars):
    all_graphs.append([0,1,1,0])

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    allBars.append(slider(min=-1, max=1, value=0, length=100, bind=setFrequency,vertical=False,left=20,right=20))
    wtext(text = ("Graph "+str(i+1)+":\t"))
    allTexts.append(wtext(text=str(allBars[i].value)))

#creates initial graph
createGraph()
