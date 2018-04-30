from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time
import numpy as np
from IPython.display import Audio, display
import random
import pyaudio


def playSound(stream):
    global all_graphs
    global soundPlayer
    framerate = 44100
    total_time = 1
    time1 = np.arange(0,total_time,total_time/framerate)
    #time1 = np.linspace(0,total_time,framerate*5)
    data = 0
    for i in range(len(all_graphs)):
        data+= all_graphs[i][1]*np.sin(2*np.pi*440*all_graphs[i][2]*time1)
    #soundPlayer = display(Audio(data,rate=framerate, autoplay=True))
    data  = (32768*data).astype(np.int16)
    #*32768

    stream.write(data.tobytes())

    #time.sleep(total_time)

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
    time.sleep(.01)
    createGraph()
    secondGraph()
    displayFunctions()


#create the graph by first deleting old code
def createGraph():
    global curve1
    global gd
    global visCurve
    curve1.visible = False
    curve1.delete()
    gd.delete()
    gd = graph(width=600, height=300,
          title='<b>Composite</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5, align = "left")
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd,visCurve)

def secondGraph():
    global gd2
    global all_graphs
    gd2.delete()
    gd2 = graph(width=600, height=300,
          title='<b>Individual</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5, align = "right")
    color_list = [color.red,  color.green, color.orange, color.cyan, color.black, color.magenta]
    for i in range(len(all_graphs)):
        graph_simpletrig(all_graphs[i][0],all_graphs[i][1],all_graphs[i][2],all_graphs[i][3],color_list[i%len(all_graphs)], gd2)


def reset(c):
    global allBars
    global allTexts
    global gd
    global gd2
    for i in allBars:
        i.value = 0
    for i in allTexts:
        i.text = 0
    for i in all_graphs:
        i[1] = 0
    gd.visible= False
    gd2.visible = False
    gd.delete()
    gd2.delete()
    time.sleep(.01)
    createGraph()
    secondGraph()
    displayFunctions()

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
    xmin=-4*math.pi, xmax=4*math.pi, ymin=-5, ymax=5,align = "left")
gd2 = graph(width=600, height=300,
    title='<b>Individual</b>',
    xtitle='<i>x</i>', ytitle='<i>y</sup>',
    foreground=color.black, background=color.white,
    xmin=-4*math.pi, xmax=4*math.pi, ymin=-5, ymax=5,align = "right")
curve1 = gcurve(color =color.blue,graph=gd )
allBars = []
allTexts = []
visCurve = curve()
reset_button = button(bind=reset, text='Reset')
df = wtext(text = "Display Function:")
t = wtext(text = ' ', align = 'center' )
P = pyaudio.PyAudio()
stream = P.open(rate=44100, format=pyaudio.paInt16, channels=1, output=True)
#Create all the lists which contain the graphs
for i in range(amt_of_bars):
    all_graphs.append([0,0,(i+1),0]) #need to change amplitudes here??

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    allBars.append(slider(min=-1, max=1, value=0, length=100, bind=setAmplitude,vertical=False,left=20,right=20))
    wtext(text = ("Harmonic "+str(i+1)+":\t"))
    allTexts.append(wtext(text=str(allBars[i].value)))

#creates initial graph
createGraph()
secondGraph()
while True:
    playSound(stream)
    time.sleep(.05)
