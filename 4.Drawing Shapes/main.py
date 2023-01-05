import numpy as np
import cv2

cap = cv2.VideoCapture(0)

while True:
    ret , frame = cap.read()
    width=int(cap.get(3))
    height=int(cap.get(4))
    
    # Lines
    # img = cv2.line(frame,(0,0),(width,height), (0,0,255),1)
    # img = cv2.line(img,(0,height),(width,0), (0,0,255),1)
    
    # rectangle
    # img=cv2.rectangle(frame, (0,0),(width,height),(128,128,128),5)
    
    # Circle
    # img=cv2.circle(frame,(width//2,height//2),50,(128,128,128),5)
    
    # Text
    # font=cv2.FONT_HERSHEY_PLAIN
    # img=cv2.putText(frame,"My Name is Mihir", (10,height-10),font, 3, (128,128,128), 5, cv2.LINE_AA)
    
    cv2.imshow('frame',frame)
    
    if cv2.waitKey(1)==ord('q'):
        break
    
cap.release()
cv2.destroyAllWindows()