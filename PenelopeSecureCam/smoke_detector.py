import RPi.GPIO as GPIO
import time
import email
import smtplib
import threading
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def startThread():
    thread = threading.Thread(target=sd,args=())
    thread.start()
    print("smoke detector activated")

def sendMail(stamp):
    fromadr = "penelopesecur@outlook.com"
    toadr = "hugo.pierre@devinci.fr"
    msg = MIMEMultipart()
    msg['From'] = fromadr
    msg['To'] = toadr
    msg['Subject'] = "ALERTE FEU !"
    body = "Incendie détecté !!!!!!!!!!!!!!!!!!!!!!!!!!!"
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromadr, "Penelope")
    text = msg.as_string()
    server.sendmail(fromadr, toadr, text)
    server.quit()
    
def sd():
    while True:
        input_state = GPIO.input(18)
        if input_state == False:
            print('Smoke detector alert')
            sendMail(time.strftime("%c"))
            time.sleep(1)
