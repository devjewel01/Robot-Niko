import sys
sys.path.append("/home/pi/Robot-Niko/src/movement")
from head import  servoMove
from time import sleep

import cv2

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
cap = cv2.VideoCapture(0)

while cap.isOpened():
    _, img = cap.read()

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    for (x, y , w ,h) in faces:
        cv2.rectangle(img, (x,y), (x+w, y+h), (0, 0 , 0), 3)
        print(x, y)
        servoMove(11, (int)(90+(-250+x)/12))
        sleep(0.1)        

    cv2.imshow('img', img)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
