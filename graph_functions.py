from vpython import *
import math

# want to graph sine or cosine?
# @param co, 1 is cosine, 0 is sine
# @param a amplitude
# @param p period is 2pi/p
# @param b 2 pi/(phase shift)
# @param Gcolor the color of the graph
# will graph a*sin(p*(x + b))    (or cos)
def graph_simpletrig (co, a, p, b, Gcolor):
    f1 = gcurve(color=Gcolor)
    if co:
        for x in arange(0, 2*2*math.pi/p, 0.01):
            f1.plot(pos=(x, a*cos(p*(x+b))))
    else:
        for x in arange(0, 2*2*math.pi/p, 0.01):
            f1.plot(pos=(x, a*sin(p*(x+b))))


#test
graph_simpletrig(False, 1,1,0,color.blue)

