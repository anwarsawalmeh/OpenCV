import numpy as np
import cv2 

""" 
The number inside the method links to the camera or device we want to use. 
If we had multiple different numbers access the different ones. 

We can also display videos. Instead of a number we input the file name.
"""
cap = cv2.VideoCapture(0)

while True:
    """ Read returns a numpy array of the image itself. Numpy arrays represent our images. RET shows us if it worked or not. True or False """
    ret, frame = cap.read() 
    # getting the width and height of the capture. We convert into ints because they come as floating type.
    width = int(cap.get(3))
    height = int(cap.get(4))

    # Image is just a black image. 
    image = np.zeros(frame.shape, np.uint8)
    smaller_frame = cv2.resize(frame, (0,0), fx=0.5, fy=0.5)
    
    # Top left
    image[:height//2, :width//2] = smaller_frame
    # Bottom left
    image[height//2:, :width//2] = smaller_frame
    # Top right
    image[:height//2, width//2:] = smaller_frame
    # Bottom right
    image[height//2:, width//2:] = smaller_frame
    
    cv2.imshow('frame', image)

    """ Every milisecond it checks if we clicked on q. If we did then it will break the for loop and close the window. """
    if cv2.waitKey(1) == ord('q'):
        break
""" Releases the camera to be used by other programs.  """
cap.release()
cv2.destroyAllWindows()

 