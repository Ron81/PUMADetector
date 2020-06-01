import cv2

cap = cv2.VideoCapture(0)
# Setting ID 3 = width / 4 = height
cap.set(3,600)
cap.set(4,600)
# ID 10 = Brightness
cap.set(10,100)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()

    # insert PUMA as Text
    font = cv2.FONT_HERSHEY_SIMPLEX
    cv2.putText(frame, 'PUMA', (10, 450), font, 2, (255, 255, 255), 1, cv2.LINE_AA)

    # Display the resulting frame
    cv2.imshow('Video Output',frame)

    # Killswitch = q
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()