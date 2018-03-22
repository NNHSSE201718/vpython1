from visual import *
from visual.graph import *
f1 = gcurve(color=color.blue)
for x in arange(0,8.05,0.01):
    f1.plot(pos=(x,sin(x)))
