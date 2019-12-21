import cv2 as cv
import numpy as np
from BasicsCommands import plotting_utilities as pu

kernal = np.ones((3, 3), np.uint8)

img = pu.img_database(7, 3)


bilateralFilter1 = cv.bilateralFilter(img, 9, 80, 150)
img_blurred = cv.GaussianBlur(bilateralFilter1, (5, 5), 0)
_, th1 = cv.threshold(img, 127, 255, cv.THRESH_BINARY_INV)
th2 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_MEAN_C, cv.THRESH_BINARY_INV, 11, 2)
th3 = cv.adaptiveThreshold(img, 255, cv.ADAPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY_INV, 11, 2)
bilateralFilter2 = cv.bilateralFilter(th2, 9, 75, 75)
median = cv.medianBlur(bilateralFilter2, 5)

"""
bilateralFilter2 = cv.bilateralFilter(th1, 9, 75, 75)
median = cv.medianBlur(th1, 5)
median_close = cv.morphologyEx(median, cv.MORPH_CLOSE, kernal)
opening = cv.morphologyEx(bilateralFilter2, cv.MORPH_OPEN, kernal)
"""
titles = ['Original Image', '1 - Bilateral Filter', '2 - Gaussian Blur', '3 - Threshold',
          '4 - th2', '5 - th3', '6 - Bilateral Filter 2', '7 - Median']
images = [img, bilateralFilter1, img_blurred, th1, th2, th3, bilateralFilter2, median]

pu.plotting_images(images, titles)
