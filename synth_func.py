import sys

import numpy as np
##import matplotlib.pyplot as plt
from IPython.display import (
    Audio, display, clear_output)
from ipywidgets import widgets
from functools import partial

# play the composite sound with a frequency list that corresponds with the amplitude list
# graphList[0] defines the first function, etc.
def synth(graphList, duration):
    rate = 10000
    
    t = np.linspace(
        0., duration, int(rate * duration))
    
    x = 0
    for i in range(len(graphList)):
        x += graphList[i][1]*(np.sin(graphList[i][2] * 2. * np.pi * 440 * t))
    # wave = np.sin(2*np.pi*440*np.arange(10000*2)/10000)
    Audio(x, rate=rate, autoplay=True)

synth([[0,1,1,0]],5)
