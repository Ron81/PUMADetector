import cv2
import numpy as np

#Video Capture Settings
cap = cv2.VideoCapture(0)
# Setting ID 3 = width / 4 = height
cap.set(3,600)
cap.set(4,600)
# ID 10 = Brightness
cap.set(10,100)

#Trackbar for Modifiying the video
def empty(a):
    pass

cv2.namedWindow("Trackbars")
cv2.resizeWindow("Trackbars",600,300)
cv2.createTrackbar("Hue Min","Trackbars",0,179,empty)

#Video Modification Part
while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    #insert PUMA as Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'PUMA', (10, 450), font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    #change from BGR to HSV
    imgHSV = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # Display the resulting frame
    cv2.imshow('Output Window',imgHSV)

    # Display the Trackbars
    h_min = cv2.getTrackbarPos("Hue Min", "Trackbars")


    # Ending the loop via q-Button
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()