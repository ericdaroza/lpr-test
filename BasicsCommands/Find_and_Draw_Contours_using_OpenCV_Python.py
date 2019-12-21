import numpy as np
import cv2

img = cv2.imread('opencv-logo.png')
imgray = cv2.cvtColor(img, cv2.COLOR_BAYER_BG2GRAY)

cv2.imshow('Image', img)
cv2.imshow('Image GRAY', imgray)
cv2.waitKey()
cv2.destroyAllWindows()
