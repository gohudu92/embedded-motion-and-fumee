import pip
import os
import subprocess as sub
import picamera 
import cv2
import socket 
import io 


sub.call(["sudo", "apt-get", "install", "python3-flask"])

from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
  def HelloWorld():
      return 'Hello world'
def gen(camera):
    while True: 
       rval, frame = vc.read() 
       cv2.imwrite('pic.jpg', frame) 
       yield (b'--frame\r\n' 
              b'Content-Type: image/jpeg\r\n\r\n' + open('pic.jpg', 'rb').read() + b'\r\n') 

@app.route('/index')
  def index():
      return render_template('index.html')

@app.route('/video')
  def video_feed(): 
   """Video streaming route. Put this in the src attribute of an img tag.""" 
   return Response(gen(), 
                   mimetype='multipart/x-mixed-replace; boundary=frame') 

@app.route('/Imageslog')
  def imageslog():
      return render_template('ImagesLog.html')

@app.route('/Control')
  def control():
        return render_template('sender.php')


  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')







