import os
import smoke_detector as sd
import sys
from flask import *
from flask import Flask
from flask import render_template
import reco
import cv2
from threading import *
import time


done = 0
app = Flask(__name__)
print("Server started")
sd.startThread()


@app.route('/')
def HelloWorld():
    return render_template('index.html') 

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/Control')
def function():
    global done
    if(done==0):
        reco.startThread(done)
        done = 1
        return redirect(url_for('index'))
    elif(done==1):
        reco.killThread(done)
        done = 0
        return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')

    








