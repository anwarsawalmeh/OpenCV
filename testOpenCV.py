import cv2

"""
Image reading modes:
1) cv2.IMREAD_COLOR : Loads color image == -1
2) cv2.IMREAD_GRAYSCALE : Loads image in Gray Scale mode == 0
3) cv2.IMREAD_UNCHANGED : Loads image as sucg including alpha channel == 1
"""

img = cv2.imread('assets/KHJS3577.JPG', 1)
img = cv2.resize(img, (400,400))
cv2.imshow('Image Displaying',img)


""" Wait an infinite amount of time until we click any key on the keyboard. 5 Would mean 5 seconds and if not pressed in 5 seconds it's skipped"""
cv2.waitKey(0)
""" Once any key is clicked we destroy all windows """
cv2.destroyAllWindows()

