import pip
import os
import subprocess as sub


sub.call(["sudo", "apt-get", "install", "python3-flask"])

from Flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
  def HelloWorld():
      return 'Hello world'

@app.route('/index')
  def index():
      return render_template('index.html')

@app.route('/video')
  def videoLive():
      return render_template('video.html')

@app.route('/Imageslog')
  def imageslog():
      return render_template('ImagesLog.html')

@app.route('/Control')
  def control():
        return render_template('control.php')


  if __name__ == '__main__':
      app.run(debug=True, host='0.0.0.0')







