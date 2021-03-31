import cv2
import time

dispW=int(1280*0.4)
dispH=int(960*0.4)
flip=2

camSet='nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3280, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'

cam=cv2.VideoCapture(camSet)

while True:
	
    t1 = time.time()
    ret,frame=cam.read()
    cv2.imshow('piCam' ,frame)
    t2 = time.time()
    print(' fps : ',round(1/(t2-t1)))
    if cv2.waitKey(1)==ord('q'):
        break

cam.release()
cv2.destroyAllWindows()
