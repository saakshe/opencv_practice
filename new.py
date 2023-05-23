import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)  
  
while(True):  
    ret, frame = cap.read()  

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    cv2.imshow('frame', hsv_img)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    # Threshold the HSV image to get only blue colors
    mask = cv2.inRange(hsv_img, lower_blue, upper_blue)
    res = cv2.bitwise_and(frame,frame, mask= mask)
    cv2.imshow('frame',frame)
    cv2.imshow('mask',mask)
    cv2.imshow('res',res)
  
# When everything done, release the capture  
cap.release()  
cv2.destroyAllWindows()  