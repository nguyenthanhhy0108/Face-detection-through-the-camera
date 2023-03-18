import cv2
#cam default
cam = cv2.VideoCapture(0)
#gan file cascade san
face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_alt.xml")
#doc cam
while True:
    ret, frame = cam.read()
    if ret == True:
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        face = face_cascade.detectMultiScale(gray, 1.4, 4)
        for (x, y, w, h) in face:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)
        cv2.imshow("faces", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break
cam.release()
cv2.destroyAllWindows()