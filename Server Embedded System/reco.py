from threading import *
import time
from time import sleep
done = 0

def dodo():
    global done
    while done!=1:
        time.sleep(1)
        print("bonobo")
        
def startThread(val):
    global done
    thread = Thread(target = dodo)
    thread.start()
    done = val

def killThread(val):
    global done
    done = val
    

"""
import cv2
import time
import os
import email
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def logBook(stamp):
    log = open("logBook.txt", "a")
    log.write("[ALERTE] Un intru a été détecté le : "+stamp+" \n")
    log.close()

def sendMail(stamp):
    fromadr = "jeremy.martin12@hotmail.fr"
    toadr = "jeremy.martin@devinci.fr"
    msg = MIMEMultipart()
    msg['From'] = fromadr
    msg['To'] = toadr
    msg['Subject'] = "ALERTE !"
    body = "Intru detecte"
    msg.attach(MIMEText(body, 'plain'))
    filename = stamp+".jpg"
    attachment = open("/home/pi/Documents/"+stamp+".jpg", "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromadr, "Vahiteo2005")
    text = msg.as_string()
    server.sendmail(fromadr, toadr, text)
    os.remove('/home/pi/Documents/'+stamp+'.jpg')
    server.quit()

cascPath = 'xml/upper.xml'
bodyCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
i=0
count = 0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read() 
    if ret == True:
        stamp = time.strftime("%c")
        thread = threading.Thread(target=sendMail,args=(stamp,))
        sframe=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        gray = cv2.cvtColor(sframe, cv2.COLOR_BGR2GRAY)
        bodies = bodyCascade.detectMultiScale(gray,1.2,2)
        
        for (x, y, w, h) in bodies:
            x*=4
            y*=4
            h*=4
            w*=4
            #cv2.rectangle(frame,(x,y),(x+w,y+h),(102, 102, 0), 2)
            crop_body = cv2.flip(frame,1)
            print(count)
            if(len(bodies)>0):
                if(count > 30):
                    cv2.imwrite('/home/pi/Documents/'+stamp+'.jpg',crop_body)
                    logBook(stamp)
                    if(thread.is_alive() == False):
                        thread.start()
                        print("Envoyé")
                    count = 0
                count=count+1
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break   
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()
"""