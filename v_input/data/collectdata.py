
import os
import cv2
cap=cv2.VideoCapture(0)
directory='img/'
while True:
    _,frame=cap.read()
    count = {
             'a': len(os.listdir(directory+"/punch")),
             'b': len(os.listdir(directory+"/kick")),
             'c': len(os.listdir(directory+"/crouch"))
             }
    row = frame.shape[1]
    col = frame.shape[0]
    cv2.rectangle(frame,(0,40),(300,400),(255,255,255),2)
    cv2.imshow("data",frame)
    cv2.imshow("ROI",frame[40:400,0:300])
    frame=frame[40:400,0:300]
    interrupt = cv2.waitKey(10)
    # here ord[a] a keyinput for capturing img
    # count['a'] a -  dummy var for keep tracking a no of imgs
    if interrupt & 0xFF == ord('a'):
        cv2.imwrite(directory+'punch/'+str(count['a'])+'.png',frame)
    if interrupt & 0xFF == ord('b'):
        cv2.imwrite(directory+'kick/'+str(count['b'])+'.png',frame)
    if interrupt & 0xFF == ord('c'):
        cv2.imwrite(directory+'crouch/'+str(count['c'])+'.png',frame)

cap.release()
cv2.destroyAllWindows()