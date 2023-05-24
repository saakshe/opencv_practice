#face detection using haar classifiers in opencv

import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)  
  
while(True):  
    ret, frame = cap.read()  

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    haar_cascade = cv2.CascadeClassifier('haar.xml')
    faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors =5)
    for(x,y,w,h) in faces_rect:
        cv2.rectangle(frame, (x,y),(x+w, y+h), (255,0,0), thickness = 2)

    cv2.imshow('detected face', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break 
