import numpy as np
import cv2

cap = cv2.VideoCapture(0)
"""
Face and eye classifier we are using is already a trained classifier. It knows what it's looking for.
"""
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye_default.xml')

while True:
    ret, frame = cap.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    """ Detect Multi scale will return the locations of all of the faces """
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    # Output of faces is a list of a rectangle position in the image
    # To draw the rectangle we get the coordinates from the "Faces" variable [[x,y,w,h]].
    # first two items is the position of the face and the next two are the size of the face. 
    
    for (x, y, w, h) in faces:
        # Draws a rectangle on the face. Coordingate of top left of the face is x,y. 
        # So we know the width of the rectangle would start at x and then go to x + w
        # And the height of the rectangle would start at y and then go to y + h
        frame = cv2.rectangle(frame, (x,y), (x + w,y+ h), (255), 5)
    
    # Displays the window
    cv2.imshow("Auto", frame)
    # Close the window when we click on q
    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()