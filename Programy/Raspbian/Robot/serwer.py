from flask import Flask, render_template #web server
from robot import Robot
app = Flask(__name__)

r = Robot()

@app.route('/')
def Index():    
    return render_template('index.html')


@app.route('/F')
def Forward():
    r.goForward()
    return render_template('index.html')

@app.route('/B')
def Back():
    r.goBack()
    return render_template('index.html')

@app.route('/L')
def Left():
    r.turnLeft()
    return render_template('index.html')

@app.route('/R')
def Right():
    r.turnRight()
    return render_template('index.html')
    
@app.route('/S')
def Stop():
    r.stop()
    return render_template('index.html')
    
    
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port = 3000)
 
    

