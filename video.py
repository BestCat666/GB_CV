import cv2

face_cascades = cv2.CascadeClassifier(cv2.data.haarcascades + "haarcascade_frontalface_default.xml")

img = cv2.imread('family.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) #делаем из цветное картинки серую
faces = face_cascades.detectMultiScale(img_gray)
# print(faces) # в консоли координаты лица [[477 158 452 452]]

for (x, y, w, h) in faces:
  cv2.rectangle(img, (x,y), (x + w, y + h), (0, 0, 255), 1)

cv2.imshow('Result', img)
cv2.waitKey(0)



#cap = cv2.VideoCapture(0)   # чтобы работать с видео положить видео в папку ('название видео')

#while True:
 #   success, frame = cap.read()
 #   cv2.imshow('camera', frame)

  #  if cv2.waitKey(1) & 0xff == ord('q'): # чтобы выйти из бескоечного цикла
  #    break
