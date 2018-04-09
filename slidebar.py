from visual import *
from visual.controls import *
#from vpython.controls import * doesn't work
print(visual.__version__)

def change(): # Called by controls when button clicked
    if b.text == 'Click me':
        b.text = 'Try again'
    else:
        b.text = 'Click me'
 
c = controls() # Create controls window
print(controls)
# Create a button in the controls window:
b = button( pos=(10,10), width=60, height=60, 
              text='Click me', action=lambda: change() )

c = controls(title='Controlling the Scene',x=0, y=400, width=300, height=300,
             range=50)
