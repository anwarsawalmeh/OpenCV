import numpy as np
import cv2

img = cv2.imread('assets/where.png',0)
template = cv2.imread('assets/wally.jpg.png',0)

"""
This gives me (height [number of rows], width [number of columns]). If we loaded it in as color the shape would return three elements which includes the BGR
"""
h , w = template.shape 

"""
Template matching methods
There are 6 main methods that do template matching. Advised to try out all the methods and see what gives you the best result
"""
methods  = [cv2.TM_CCOEFF, cv2.TM_CCOEFF_NORMED, cv2.TM_CCORR, cv2.TM_CCORR_NORMED, cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]
for method in methods:
    # Drawing the rectangle on the image copy rather on the same image for each method
    img2 = img.copy()
    # Takes our template image and slides it across the image to check if there is any match. Convolution. 
    # (W-w + 1, H-h + 1)
    result = cv2.matchTemplate(img2, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
    # Prints all the locations from the different methods where there may be a possible match
    # print(min_loc, max_loc)

    # These need the minimum values
    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        location = min_loc
    else:
        location = max_loc
    bottom_right = (location[0] + w, location[1] + h)
    cv2.rectangle(img2, location, bottom_right, 255, 5)

    cv2.imshow("Matching", img2)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
