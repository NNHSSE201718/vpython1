import sys
import time
import numpy as np
from IPython.display import (
    Audio, display, clear_output)
import IPython
from ipywidgets import widgets
from functools import partial

rate = 16000.
duration = 2
t = np.linspace(
    0., duration, int(rate * duration))

# play the composite sound with a frequency list that corresponds with the amplitude list
def synth(freqList, ampList):
    if(len(freqList) != len(ampList)):
        print("Frequency list does not match amplitude list length. Bye bye.")
        sys.exit(0)

    x = 0
    for i in range(len(freqList)):
        x += ampList[i]*(np.sin(freqList[i] * 2. * np.pi * t)) 
        
    thing = Audio(x, rate=rate, autoplay=True)
    display(thing)
    
    clear_output(wait=True)
    time.sleep(2)
    #    display(Audio(x, rate=rate, autoplay=True))
    #a = IPython.display.DisplayObject(thing)
    #print(a)
    #display(a)
    #thing = Audio(x  + (np.sin(550 * 2. * np.pi * t)), rate=rate, autoplay=True)
    #a.reload()

synth([440,880],[1,100])
time.sleep(4)
synth([440],[1])
