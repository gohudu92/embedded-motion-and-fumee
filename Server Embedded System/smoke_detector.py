import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def sendMail(stamp):
    global message
    fromadr = "penelopesecur@outlook.com"
    toadr = "hugo.pierre@devinci.fr"
    msg = MIMEMultipart()
    msg['From'] = fromadr
    msg['To'] = toadr
    msg['Subject'] = "ALERTE !"
    body = "Intru detecte"
    server = smtplib.SMTP('smtp.live.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(fromadr, "Penelope")
    text = msg.as_string()
    server.sendmail(fromadr, toadr, text)
    server.quit()

while True:
    input_state = GPIO.input(18)
    if input_state == False:
        print('Smoke detector alert')
        sendMail(time.strtime("%c")
        time.sleep(0.2)

