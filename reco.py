import cv2
import time
cascPath = 'xml/upper.xml'
bodyCascade = cv2.CascadeClassifier(cascPath)
video_capture = cv2.VideoCapture(0)
#fourcc = cv2.VideoWriter_fourcc(*'XVID')
i=0
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read() 
    if ret == True:
        sframe=cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        gray = cv2.cvtColor(sframe, cv2.COLOR_BGR2GRAY)
        bodies = bodyCascade.detectMultiScale(gray,1.2,2)
        for (x, y, w, h) in bodies:
            x*=4
            y*=4
            h*=4
            w*=4
            cv2.rectangle(frame,(x,y),(x+w,y+h),(102, 102, 0), 2)
            crop_body = cv2.flip(frame,1)
            if(len(bodies)>0):
                """
                out = cv2.VideoWriter(time.strftime("%c")+'.avi', fourcc, 20.0, (640,480))
                while(i<100):
                    out.write(frame)
                    i=i+1
                    print("writing...")
                out.release()
                """
                cv2.imwrite('/home/pi/Documents/personne/'+time.strftime("%c")+'.jpg',crop_body)   
        cv2.imshow('Video', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
                break   
# When everything is done, release the capture
video_capture.release()
cv2.destroyAllWindows()