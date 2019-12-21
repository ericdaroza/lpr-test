import cv2 as cv
import numpy as np
from math import ceil
from matplotlib import pyplot as plt


def plotting_images(images_vet, titles_vet):
    column = int(ceil((len(images_vet)**.5)))
    lines = int(round(len(images_vet)**.5))

    for i in range(len(images_vet)):
        plt.subplot(lines, column, i+1), plt.imshow(images_vet[i], 'gray')
        plt.title(titles_vet[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


img = cv.imread('gradient.png')

_, th1 = cv.threshold(img, 50, 255, cv.THRESH_BINARY)
_, th2 = cv.threshold(img, 200, 255, cv.THRESH_BINARY_INV)
_, th3 = cv.threshold(img, 127, 255, cv.THRESH_TRUNC)
_, th4 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO)
_, th5 = cv.threshold(img, 127, 255, cv.THRESH_TOZERO_INV)

images = [img, th1, th2, th3, th4, th5]
titles = ['Original Image', 'THRESH BINARY', 'THRESH BINARY INV', 'THRESH TRUNC', 'THRESH TO ZERO',
          'THRESH TO ZERO INV']

plotting_images(images, titles)
