import cv2 as cv
import math
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('smarties.png', cv.IMREAD_GRAYSCALE)
_, mask = cv.threshold(img, 220, 255, cv.THRESH_BINARY_INV)

kernal = np.ones((5, 5), np.uint8)
dilation = cv.dilate(mask, kernal, iterations=2)
erosion = cv.erode(mask, kernal, iterations=1)
opening = cv.morphologyEx(mask, cv.MORPH_OPEN, kernal)
close = cv.morphologyEx(mask, cv.MORPH_CLOSE, kernal)
mg = cv.morphologyEx(mask, cv.MORPH_GRADIENT, kernal)
th = cv.morphologyEx(mask, cv.MORPH_TOPHAT, kernal)

titles = ['image', "MASK", 'Dilation', 'Erosion', 'Opening', 'Close', 'Gradient', 'Tophat']
images = [img, mask, dilation, erosion, opening, close, mg, th]

column = int(math.ceil((len(images)**.5)))
lines = int(round(len(images)**.5))

for i in range(len(images)):
    plt.subplot(lines, column, i+1), plt.imshow(images[i], 'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])

plt.show()
