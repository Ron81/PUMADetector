import cv2

cap = cv2.VideoCapture(0)
# Setting ID 3 = width / 4 = height / 10 = Brightness
cap.set(3,600), cap.set(4,600), cap.set(10,100)

# PUMA Logo Image
puma = cv2.imread("Logos/puma_black.png")
pumaGray = cv2.cvtColor(puma,cv2.COLOR_BGR2GRAY)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # insert PUMA as Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'PUMA', (10, 450), font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    # Display Output
    cv2.imshow('Video Output',frame)
    cv2.imshow('Logo Output', pumaGray)

    # Killswitch = q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()