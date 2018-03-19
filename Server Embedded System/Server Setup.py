import os
import sys
from flask import *
from flask import Flask
from flask import render_template
import reco
import cv2
from threading import *
from time import time

class Camera(object):
    def __init__(self):
        self.video = cv2.VideoCapture(0)
    
    def __del__(self):
        self.video.release()
    
    def get_frame(self):
        success, image = self.video.read()
        if not success:
            print ("Failing")
        image_bytes = image.tobytes()
        return image_bytes

done = 0
app = Flask(__name__)
print("Server started")

#----------------------------------------------------------------------------



#----------------------------------------------------------------------------




@app.route('/')
def HelloWorld():
    return render_template('index.html')

@app.route('/index')
def index():
    return render_template('index.html')

"""
def gen(camera):
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')

@app.route('/video')
def video_feed():
    return Response(gen(Camera()),mimetype='multipart/x-mixed-replace; boundary=frame')


@app.route('/video')
def video_feed(): 
       return "Hello World" 
"""
@app.route('/Imageslog')
def imageslog():
    return render_template('ImagesLog.html')


@app.route('/Control')
def function():
    global done
    if(done==0):
        print(str(done)+ " is the value")
        reco.startThread(0)
        done = 1
        print("This was done")
    elif(done==1):
        print(str(done)+ " is the value")
        reco.killThread(1)
        done = 0
    
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

    








