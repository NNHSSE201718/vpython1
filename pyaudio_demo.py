import time
import numpy as np
from IPython.display import Audio, display
import random
import pyaudio

def playSound(stream):
    framerate = 44100
    total_time = 1
    time1 = np.arange(0,total_time,total_time/framerate)
    #time1 = np.linspace(0,total_time,framerate*5)
    data = 1*np.sin(2*np.pi*440*time1)
    #soundPlayer = display(Audio(data,rate=framerate, autoplay=True))
    data  = (32768*data).astype(np.int16)
    #*32768

    stream.write(data.tobytes())
    #time.sleep(total_time)

P = pyaudio.PyAudio()
stream = P.open(rate=44100, format=pyaudio.paInt16, channels=1, output=True)

offset = 0
while True:
    offset+=.5
    playSound(stream)
    time.sleep(.1)
