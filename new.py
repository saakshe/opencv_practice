import cv2 
import numpy as np 

cap = cv2.VideoCapture(0)  
  
while(True):  
    ret, frame = cap.read()  

    # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  
    hsv_img = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    # define range of blue color in HSV
    lower_blue = np.array([110,50,50])
    upper_blue = np.array([130,255,255])
    mask_blue = cv2.inRange(hsv_img, lower_blue, upper_blue)
    #here we are comparing the two images via a bitwise and to see if the pixel needs to be dicarded or it needs to be retained 
    # a dialation transformation is performed 
    kernel = np.ones((5,5),np.uint8)
    dilation_blue = cv2.dilate(res_blue,kernel)
    res_blue = cv2.bitwise_and(frame, frame, 
                              mask = mask_blue)
    contours, hierarchy = cv2.findContours(mask_blue,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 300):
            x, y, w, h = cv2.boundingRect(contour)
            frame = cv2.rectangle(frame, (x, y),
                                       (x + w, y + h),
                                       (255, 0, 0), 2)
              
            cv2.putText(frame, "Blue Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 0, 0))

# When everything done, release the capture  
    cv2.imshow('frame', frame)  
    if cv2.waitKey(1) & 0xFF == ord('q'):  
        break  

cap.release()  
cv2.destroyAllWindows()  