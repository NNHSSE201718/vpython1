from vpython import *
import math

sphere()

f1 = gcurve(color=color.blue, graph=gd)
f1.plot(pos=(x,cos(x)))
