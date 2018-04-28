from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time
import numpy as np
from IPython.display import Audio, display
import random
import pyaudio


def playSound():
    global all_graphs
    global soundPlayer
    framerate = 44100
    total_time = 1
    time1 = np.arange(0,total_time,total_time/framerate)
    #time1 = np.linspace(0,5,framerate*5)
    data = 0
    for i in range(len(all_graphs)):
        data+= all_graphs[i][1]*np.sin(np.pi*440*all_graphs[i][2]*time1)
    #soundPlayer = display(Audio(data,rate=framerate, autoplay=True))
    data  = (32768*data).astype(np.int16)

    #*32768
    P = pyaudio.PyAudio()
    stream = P.open(rate=framerate, format=pyaudio.paInt16, channels=1, output=True)
    stream.write(data.tobytes())
    stream.close() # this blocks until sound finishes playing
    P.terminate()
    time.sleep(total_time)

#set amplitude of the graph that is being changed
def setAmplitude(s):
    global all_graphs
    global allBars
    global allTexts
    global gd
    global gd2
    allTexts[allBars.index(s)].text=s.value
    all_graphs[allBars.index(s)][1]=s.value
    gd.visible= False
    gd2.visible = False
    gd.delete()
    gd2.delete()
    createGraph()
    secondGraph()
    displayFunctions()
    playSound()


#create the graph by first deleting old code
def createGraph():
    #global all_graphs
    global curve1
    global gd
    global visCurve
    curve1.visible = False
    curve1.delete()
    gd = graph(width=600, height=300,
          title='<b>Composite</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5)
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd,visCurve)

def secondGraph():
    global gd2
    global all_graphs
    gd2 = graph(width=600, height=300,
          title='<b>Individual</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5)
    color_list = [color.red,  color.green, color.orange, color.cyan, color.black, color.magenta]
    for i in range(len(all_graphs)):
        graph_simpletrig(all_graphs[i][0],all_graphs[i][1],all_graphs[i][2],all_graphs[i][3],color_list[i%len(all_graphs)], gd2)




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
        setText+=str(round(all_graphs[i][2],3))+str(chr(952))+")+"+str(all_graphs[i][3])+" + "
    t.text = "\t" + setText


amt_of_bars = 5
all_graphs = []
gd = graph(width=600, height=300,
    title='<b>Composite</b>',
    xtitle='<i>x</i>', ytitle='<i>y</sup>',
    foreground=color.black, background=color.white,
    xmin=-4*math.pi, xmax=4*math.pi, ymin=-5, ymax=5)
gd2 = graph(width=600, height=300,
    title='<b>Individual</b>',
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
    all_graphs.append([0,0,(i+1),0]) #need to change amplitudes here??

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    allBars.append(slider(min=-1.2, max=1.2, value=0, length=100, bind=setAmplitude,vertical=False,left=20,right=20))
    wtext(text = ("Harmonic "+str(i+1)+":\t"))
    allTexts.append(wtext(text=str(allBars[i].value)))

#creates initial graph
createGraph()
secondGraph()
