from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time
import numpy as np
from IPython.display import Audio, display
import random

def playSound():
    global all_graphs
    global soundPlayer
    framerate = 44100
    time1 = np.linspace(0,5,framerate*5)
    print(time1)
    data = 0
    for i in range(len(all_graphs)):
        data+= all_graphs[i][1]*np.sin(440*all_graphs[i][2]*time1)
#        if all_graphs[i][1]==0:
 #           continue
  #      if all_graphs[i][0] == 1:
   #         data += all_graphs[i][1]*np.cos(all_graphs[i][2]*time)
    #    else:
     #       data += all_graphs[i][1]*np.sin(float(880)/3*all_graphs[i][2]*time)
      #      print(float(880)*all_graphs[i][2])
    soundPlayer = display(Audio(data,rate=framerate, autoplay=True))
    time.sleep(5)

#set amplitude of the graph that is being changed
def setAmplitude(s):
    global all_graphs
    global allBars
    global allTexts
    allTexts[allBars.index(s)].text=s.value
    all_graphs[allBars.index(s)][1]=s.value
    createGraph()

#create the graph by first deleting old code
def createGraph():
    #global all_graphs
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
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5)
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd,visCurve)
    displayFunctions()
    print(random.randint(0,100))
    playSound()


def displayFunctions():
    global t
    global all_graphs
    setText = ''
    for i in range(len(all_graphs)):
        if all_graphs[i][1]==0:
            continue
        setText+=str(all_graphs[i][1])
        if all_graphs[i][0]:
            setText+="cos("
        else:
            setText+="sin("
        setText+=str(round(all_graphs[i][2],3))+"θ)+"+str(all_graphs[i][3])+" + "
    t.text = "\t" + setText


soundPlayer = Audio(np.sin(0*np.linspace(0,5,44100*5)) ,rate=44100, autoplay=True)
print(soundPlayer)
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
df = wtext(text = "Display Function:")
t = wtext(text = 'Function: ', align = 'center' )

#Create all the lists which contain the graphs
for i in range(amt_of_bars):
    all_graphs.append([0,1,2*math.pi*(i+1),0]) #need to change amplitudes here??

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    allBars.append(slider(min=-1.2, max=1.2, value=0, length=100, bind=setAmplitude,vertical=False,left=20,right=20))
    wtext(text = ("Graph "+str(i+1)+":\t"))
    allTexts.append(wtext(text=str(allBars[i].value)))

#creates initial graph
createGraph()
