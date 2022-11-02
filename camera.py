import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_smile.xml")
cap = cv2.VideoCapture(0)   # чтобы работать с видео положить видео в папку ('название видео')

while True:
    success, frame = cap.read()
    cv2.imshow('camera', frame)
    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascades.detectMultiScale(img_gray)
    for (x, y, w, h) in faces:
       cv2.rectangle(frame, (x,y), (x + w, y + h), (0, 0, 255), 1)
    
    cv2.imshow('Result', frame)

    if cv2.waitKey(1) & 0xff == ord('q'): 
        break
