import cv2
import numpy as np

cap = cv2.VideoCapture(0)
# Setting ID 3 = width / 4 = height / 10 = Brightness
cap.set(3,600), cap.set(4,600), cap.set(10,100)

# PUMA Logo Image
pumaLogo = cv2.imread("Logos/puma_small.png", cv2.IMREAD_GRAYSCALE)

# Face detector
faceCascade= cv2.CascadeClassifier("Resources/haarcascade_frontalface_default.xml")

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # insert PUMA as Text
    # font = cv2.FONT_HERSHEY_SIMPLEX
    # cv2.putText(frame, 'PUMA', (10, 450), font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    # Transformations
    canny_noise = cv2.Canny(frame, 100, 100)
    canny_clean = cv2.Canny(frame, 150, 200)
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # ORB Detector
    orb = cv2.ORB_create()
    kp1, des1 = orb.detectAndCompute(pumaLogo, None)
    kp2, des2 = orb.detectAndCompute(frameGray, None)

    # Brute Force Matching (crossCheck True = only best match, False = more)
    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)
    matches = bf.match(des1, des2)
    matches = sorted(matches, key=lambda x: x.distance)

    matching_result = cv2.drawMatches(pumaLogo, kp1, frameGray, kp2, matches[:50], None, flags=2)

    # mark detected faces
    faces = faceCascade.detectMultiScale(frameGray, 1.1, 4)
    for (x, y, w, h) in faces:
        cv2.rectangle(canny_clean, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display Output
    cv2.imshow('Video Gray',frameGray)
    #cv2.imshow('Video Noise', canny_noise)
    #cv2.imshow('Video Clean', canny_clean)
    cv2.imshow("Matching result", matching_result)
    # cv2.imshow('Logo Output', pumaLogo)

    # exit loop = q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()