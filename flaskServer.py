from flask import Flask

app = Flask(__name__)
app.secret_key = 'development key'
password = 'nnhs3061'
@app.route('/')
def runVpython():
    exec(open("Full_Simulation_Python.py").read(),globals())
    return
if __name__ == "__main__":
    app.run()
