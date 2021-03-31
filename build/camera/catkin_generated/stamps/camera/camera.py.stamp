import cv2
import time
#import rospy
import numpy as np
import matplotlib.image as mat
print("TEST1")
dispW=int(1280*0.4)
dispH=int(960*0.4)
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=1848, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
print("TEST2")
cam=cv2.VideoCapture(camSet)
print("TEST3")
while True:
	
    t1 = time.time()
    print("TEST4")
    ret,frame=cam.read()
    print("TEST5")
    #cv2.imshow('piCam' ,frame)
    print("TEST5")
    t2 = time.time()
    print(' fps : ',round(1/(t2-t1)))
    if cv2.waitKey(100) & 0xFF==ord('q'):
        break
mat.imshow(frame)
mat.show()
cam.release()
cv2.destroyAllWindows()
