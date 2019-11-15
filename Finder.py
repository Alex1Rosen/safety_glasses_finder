import numpy as np
import cv2

# multiple cascades: https://github.com/Itseez/opencv/tree/master/data/haarcascades

#https://github.com/Itseez/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
#https://github.com/sightmachine/SimpleCV/blob/master/SimpleCV/Features/HaarCascades/glasses.xml
glasses_cascade = cv2.CascadeClassifier('glasses.xml')

cap = cv2.VideoCapture(0)

while 1:
    ret, img = cap.read()
    # gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(img, 1.3, 5)
    # glasses = glasses_cascade.detectMultiSCALE(img, 1.3, 5)
   
    for (x,y,w,h) in faces:
        face_cut = img[y:y+h, x:x+w]
        glasses_in_cut = glasses_cascade.detectMultiSCALE(face_cut, 1.3, 5)
        counter =0
       for (ex,ey,ew,eh) in glasses_in_cut: 
            counter = counter + 1
            cx=x+ew/2
            cy=y+eh/2
            if cx not in range(x,x+w) || cy not in range(y,y+h):
                cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
                
        if counter = 0:
           cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0),2) 
        
    
    cv2.imshow('img',img)
    k = cv2.waitKey(30) & 0xff
    if k == 27:
        break

cap.release()
cv2.destroyAllWindows()
