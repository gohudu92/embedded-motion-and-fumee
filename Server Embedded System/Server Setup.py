import os
from flask import *
from flask import Flask
from flask import render_template
import reco
from threading import *

done = 0
app = Flask(__name__)
print(" the done is " + str(done))



    


@app.route('/')
def HelloWorld():
    return 'Hello world'
def gen():
    return 0 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/video')
def video_feed(): 
       """Video streaming route. Put this in the src attribute of an img tag."""
       return "Hello World" 

@app.route('/Imageslog')
def imageslog():
    return render_template('ImagesLog.html')

@app.route('/Control')
def b():
    global done
    if(done==0):
        print(str(done)+ " is the value")
        reco.startThread(done)
        done = 1
        print("This was done")
    elif(done==1):
        print(str(done)+ " is the value")
        reco.killThread(done)
        done = 0
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    print("Squalala")
    app.run(debug=True, host='0.0.0.0')

    








