from visual import *
from visual.graph import *

# want to graph sine or cosine?
# @param co, 1 is cosine, 0 is sine
# @param a amplitude
# @param p period
# @param b 2 pi/(phase shift)
# @param color the color of the graph
# will graph a*sin(p*(x + b)) 
def graph_simpletrig (self, a, p, b, Gcolor):
    f1 = gcurve(color=Gcolor)
    for x in arange(0, 8.1, 0.01):
        f1.plot(pos=(x, a*sin(p*(x+b))))


#test
graph_simpletrig(1,1,0,color.blue)
