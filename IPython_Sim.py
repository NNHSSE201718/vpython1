from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig, graph_3D_curve
from synth_func import synth
import math
import time
import numpy as np
import pyaudio

##def playSound(stream):
##    global all_graphs,soundPlayer
##    framerate = 44100
##    total_time = 1
##    time1 = np.arange(0,total_time,total_time/framerate)
##    #time1 = np.linspace(0,total_time,framerate*5)
##    data = 0
##    divisor = 0
##    for i in range(len(all_graphs)):
##        divisor+= abs(all_graphs[i][1])
##    if divisor <1:
##        divisor=1
##    for i in range(len(all_graphs)):
##        data+= float(all_graphs[i][1])/divisor*np.sin(2*np.pi*440*all_graphs[i][2]*time1)
##    #soundPlayer = display(Audio(data,rate=framerate, autoplay=True))
##    data  = (32768*data).astype(np.int16)
##    stream.write(data.tobytes())
    

#set amplitude of the graph that is being changed
#updates the text displays, graph arrays, and displays for graphs
def setAmplitude(s):
    global all_graphs,allBars,allTexts,gd,gd2
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


#create the composite graph.
def createGraph():
    global curve1,gd,visCurve
    curve1.visible = False
    curve1.delete()
    gd.delete()
    gd = graph(width=600, height=300,
          title='<b>Composite</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5, align = "left")
    curve1 = graph_sumtrig(curve1,all_graphs,color.blue,gd)

#creates the individual graphs
def secondGraph():
    global gd2,all_graphs
    gd2.delete()
    gd2 = graph(width=600, height=300,
          title='<b>Individual</b>',
          xtitle='<i>x</i>', ytitle='<i>y</sup>',
          foreground=color.black, background=color.white,
          xmin=0, xmax=2*math.pi, ymin=-5, ymax=5, align = "right")
    color_list = [color.red,  color.green, color.orange, color.cyan, color.black, color.magenta]
    for i in range(len(all_graphs)):
        graph_simpletrig(all_graphs[i][0],all_graphs[i][1],all_graphs[i][2],all_graphs[i][3],color_list[i%len(color_list)], gd2)

#resets all graphs, arrays, slidebars, and functions
def reset():
    global allBars, allTexts, gd, gd2, all_graphs
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

def presetWave(m):
    global allBars, allTexts, gd, gd2, all_graphs
    if m.selected == "Select Below":
        reset()
    elif m.selected == "sine":
        for i in range(len(all_graphs)):
            if i == 0:
                allBars[i].value = 1
                allTexts[i].text = 1
                all_graphs[i][1] = 1
            else:
                allBars[i].value = 0
                allTexts[i].text = 0
                all_graphs[i][1] = 0
    elif m.selected == "triangle":
        for i in range(len(all_graphs)):
            n=i+1
            if n%2==0:
                num = 0
            else:
                if (n+1)%4 == 0:
                    num = 1
                else:
                    num = -1
            all_graphs[i][1] = float(num)/((i+1)*(i+1))
            allTexts[i].text =  float(num)/((i+1)*(i+1))
            allBars[i].value =  float(num)/((i+1)*(i+1))
    elif m.selected == "square":
        for i in range(len(all_graphs)):
            if i%2 == 0:
                all_graphs[i][1]= float(1)/(i+1)
                allTexts[i].text =  float(1)/(i+1)
                allBars[i].value =  float(1)/(i+1)
            else:
                all_graphs[i][1] = 0
                allTexts[i].text = 0
                allBars[i].value = 0
    elif m.selected == "sawtooth":
        for i in range(len(all_graphs)):
            if i%2==0:
                num = 1
            else:
                num = -1
            all_graphs[i][1] = float(num)/(i+1)
            allTexts[i].text =  float(num)/(i+1)
            allBars[i].value =  float(num)/(i+1)
    gd.visible= False
    gd2.visible = False
    gd.delete()
    gd2.delete()
    time.sleep(.01)
    createGraph()
    secondGraph()
    displayFunctions()


#Displays the wave composite function
def displayFunctions():
    global t,all_graphs
    setText = ''
    for i in range(len(all_graphs)):
        if all_graphs[i][1]==0:
            continue
        setText+=str(round(all_graphs[i][1],3))
        if all_graphs[i][0]:
            setText+="cos("
        else:
            setText+="sin("
        setText+=str(round(all_graphs[i][2],3))+str(chr(952))+") + "
    t.text = "\t" + setText


#Initialize all variables and format
scene.append_to_caption('<h1 align="center">Fourier Transform</h1>')
scene.align = 'right'
scene.userzoom = False
scene.userspin = False
scene.userpan  = False
amt_of_bars = 6
all_graphs = []
allBars = []
allTexts = []

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

visCurve = curve()
reset_button = button(bind=reset, text='Reset')
scene.append_to_caption('\n\n')
df = wtext(text = "Display Function:")
t = wtext(text = ' ', align = 'center' )
scene.append_to_caption('\n\n')

#Audio Stream
##P = pyaudio.PyAudio()
##stream = P.open(rate=44100, format=pyaudio.paInt16, channels=1, output=True)


#Create all the lists which contain the graphs
for i in range(amt_of_bars):
    all_graphs.append([0,0,(i+1),0])

#Creates the dropdown
presets = menu(choices=["Select Below","sine","triangle", "square","sawtooth"], bind = presetWave)

#Creates all the sliders
for i in range(amt_of_bars):
    scene.append_to_caption('\n\n')
    wtext(text = ("\t\tHarmonic "+str(i+1)+": "))
    allTexts.append(wtext(text=str("0")))
    allBars.append(slider(min=-1, max=1, value=0,length = 100, bind=setAmplitude,left=20,right=20))


scene.append_to_caption('\n\n\n\n')

#creates initial graphs
createGraph()
secondGraph()

#loop that updates the sound as well as moving curve
offset = 0
while True:
    offset+=.5
    # playSound(stream)
    
    synth(all_graphs, 1)
    graph_3D_curve(all_graphs, visCurve, offset)
    time.sleep(.001)
