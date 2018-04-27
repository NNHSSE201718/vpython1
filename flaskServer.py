from flask import Flask
from vpython import *
from graph_functions import graph_simpletrig, graph_sumtrig
import math
import time
import numpy as np
from IPython.display import Audio, display
import random

app = Flask(__name__)
app.secret_key = 'development key'
password = 'nnhs3061'
@app.route('/')
def runVpython():
    exec(open("Full_Simulation_Python.py").read(),globals())
if __name__ == "__main__":
    app.run()
