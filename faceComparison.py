import numpy as np
import cv2
import os

cap = cv2.VideoCapture(0)

face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
image_counter = 0
while True:
    ret, frame = cap.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    face = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in face:
       frame = cv2.rectangle(frame, (x,y), (x+w,y+h), (255), 5)
       face_image = frame[y:y+h, x:x+w]
       cv2.imshow("Face", face_image)
       
       image_counter += 1
       image_filename = f"face_images/face_{image_counter}.png"
       cv2.imwrite(image_filename, face_image)
       print(f"Saved: {image_filename}")
    
    cv2.imshow("Testing", frame)
    if cv2.waitKey(1) == ord('q'):
        break
cap.release()
cv2.destroyAllWindows()