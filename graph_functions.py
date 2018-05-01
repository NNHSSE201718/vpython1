from vpython import *
#from vpython.graph import *
import math

# want to graph sine or cosine?
# @param co, 1 is cosine, 0 is sine
# @param a amplitude
# @param p period is 2pi/p
# @param b 2 pi/(phase shift)
# @param Gcolor the color of the graph
# will graph a*sin(p*(x + b))    (or cos)
def graph_simpletrig (co, a, p, b, Gcolor,gd):
    f1 = gcurve(color=Gcolor,graph=gd)
    if co==1:
        for x in arange(0, 2*2*math.pi, 0.01):
            f1.plot(pos=(x, a*cos(p*(x+b))))
    else:
        for x in arange(0, 2*2*math.pi, 0.01):
            f1.plot(pos=(x, a*sin(p*(x+b))))

# @param functions list of functions in terms of x
#       each function is a list, with paramaters for
#       graph_simpletrig above, without color
# @param Gcolor the color of the total graph
def graph_sumtrig (f2, functions, Gcolor, gd):
    #c.clear()
    f2 = gcurve(color=Gcolor,graph=gd)
    for i in range(len(functions)):
        if len(functions[i]) != 4:
            print("Function number" , (i+1) , "was inputted incorrectly")
            sys.exit()

    for x in arange(0, 6*math.pi, 0.01):
        total = 0
        for i in range(len(functions)):
            if functions[i][0]==1:
                total = total + functions[i][1]*cos(functions[i][2]*(x+functions[i][3]))
            else:
                total = total + functions[i][1]*sin(functions[i][2]*(x+functions[i][3]))

        f2.plot(pos=(x,total))
        #c.append(pos = vector(x-5,total,0))
    return(f2)
def graph_3D_curve(functions,c,offset):
    c.clear()
    for x in arange(0, 6*math.pi, 0.01):
        total = 0
        for i in range(len(functions)):
            if functions[i][0]==1:
                total = total + functions[i][1]*cos(functions[i][2]*(x+offset+functions[i][3]))
            else:
                total = total + functions[i][1]*sin(functions[i][2]*(x+offset+functions[i][3]))
        c.append(pos=vector(x-5,total,0))
