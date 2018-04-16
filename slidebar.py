from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time

#set amplitude of the graph that is being changed
def setFrequency(s):
    global all_graphs
    global allBars
    global allTexts
    displayFunctions()
    allTexts[allBars.index(s)].text=s.value
    all_graphs[allBars.index(s)][2]=s.value
    createGraph()

#create the graph by first deleting old code
def createGraph():
    global all_graphs
    global curve1
    global gd
    global visCurve
    curve1.visible = False
    curve1.delete()
    gd.delete()
    gd = graph(width=600, height=300,
          title='<b>The Greatest Curve of All Time</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=-4*math.pi, xmax=4*math.pi, ymin=-5, ymax=5)
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd,visCurve)

def displayFunctions():
    global t
    global all_graphs
    setText = ''
    for i in range(len(all_graphs)):
        setText+=str(all_graphs[i][1])
        if all_graphs[i][0]:
            setText+="cos("
        else:
            setText+="sin("
        setText+=str(all_graphs[i][2])+"θ)+"+str(all_graphs[i][3])+"  "
    t.text = (setText )

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
t = wtext(text = '')

#Create all the lists which contain the graphs
for i in range(amt_of_bars):
    all_graphs.append([0,1,1,0])

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    allBars.append(slider(min=-1, max=1, value=0, length=100, bind=setFrequency,vertical=False,left=20,right=20))
    wtext(text = ("Graph "+str(i+1)+":\t"))
    allTexts.append(wtext(text=str(allBars[i].value)))

#show the function in the 3D view
displayFunctions()
#creates initial graph
createGraph()
