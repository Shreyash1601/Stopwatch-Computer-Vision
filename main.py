import cv2
import cvzone
import time
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(1)
detector=HandDetector(detectionCon=0.8)

cap.set(3,1280)
cap.set(4,720)
clock=cv2.imread("clock.png",cv2.IMREAD_UNCHANGED)
clock=cv2.resize(clock,(500,500))
hand=cv2.imread("hand4.png",cv2.IMREAD_UNCHANGED)
hand=cv2.resize(hand,(200,200))
time1=None
history=None
start_time=time.time()
while True:
    succ,img=cap.read()
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType=False)
    if hands:
          lmList=hands[0]['lmList']
          cursor=lmList[8]
          length,info,img=detector.findDistance(lmList[8],lmList[12],img)
          if length<60:
            if(time1==None):
                time1=time.time()
                start_time=time.time()
            end_time=time.time()
            cvzone.putTextRect(img,f"Time:{round(end_time-time1,2)}",[10,100],scale=3,thickness=5,offset=10)    
            if(round(end_time-start_time)==1):
              start_time=end_time
              hand=cvzone.rotateImage(hand,-4.2,1)
          else:
              history=round(end_time-time1,2)
              start_time=end_time=time.time()
    else:
        time1=None
        hand=None
        history=None
        hand=cv2.imread("hand4.png",cv2.IMREAD_UNCHANGED)
        hand=cv2.resize(hand,(200,200))
        
    img=cvzone.overlayPNG(img,clock,[10,200])
    img=cvzone.overlayPNG(img,hand,[170,350])
    cv2.namedWindow("img",cv2.WND_PROP_FULLSCREEN)
    cv2.imshow("img",img)
    cv2.waitKey(1)