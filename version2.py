import cv2
import numpy as np

kernel = np.ones((5,5),np.uint8)

cap = cv2.VideoCapture(0)
# Setting ID 3 = width / 4 = height
cap.set(3,600)
cap.set(4,600)
# ID 10 = Brightness
cap.set(10,100)


while(True):
    # Capture frame-by-frame
    ret, canny = cap.read()
    ret, dilate = cap.read()

    # Switch from BGR to GRAY and insert PUMA as Text
    canny_noise = cv2.Canny(canny,100,100)
    canny_clean = cv2.Canny(dilate,150,200)
    canny_dilate = cv2.dilate(canny_clean,kernel,iterations=1)
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(canny_noise, 'PUMA', (10, 450), font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('canny',canny_noise)
    cv2.imshow('dilate',canny_dilate)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()