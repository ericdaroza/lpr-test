import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt
from math import ceil


def plotting_images(images_vet, titles_vet):
    column = int(ceil((len(images_vet)**.5)))
    lines = int(round(len(images_vet)**.5))

    for i in range(len(images_vet)):
        plt.subplot(lines, column, i+1), plt.imshow(images_vet[i], 'gray')
        plt.title(titles_vet[i])
        plt.xticks([]), plt.yticks([])

    plt.show()


img_database = [cv.imread('water.png', cv.IMREAD_GRAYSCALE), cv.imread('lena.jpg', cv.IMREAD_GRAYSCALE),
                cv.imread('carro2.jpg', cv.IMREAD_GRAYSCALE), cv.imread('opencv-logo.png', cv.IMREAD_GRAYSCALE),
                cv.imread('smarties.png', cv.IMREAD_GRAYSCALE), cv.imread('Halftone_Gaussian_Blur.jpg',
                                                                          cv.IMREAD_GRAYSCALE),
                cv.imread('carro1.jpg', cv.IMREAD_GRAYSCALE), cv.imread('carro3.jpeg', cv.IMREAD_GRAYSCALE),
                cv.imread('carro4.png', cv.IMREAD_GRAYSCALE), cv.imread('smarties.png', cv.IMREAD_GRAYSCALE),
                cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE), cv.imread('gradient.png', cv.IMREAD_GRAYSCALE)]

img = img_database[0]
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

kernel = np.ones((5, 5), np.float32)/25
dst = cv.filter2D(img, -1, kernel)
blur = cv.blur(img, (5, 5))
gblur = cv.GaussianBlur(img, (5, 5), 0)
median = cv.medianBlur(img, 5)
bilateralFilter = cv.bilateralFilter(img, 9, 75, 75)

titles = ['Original Image', '2D Convolution', 'Blur', 'Gaussian Blur', 'Median Filter', 'Bilateral Filter']
images = [img, dst, blur, gblur, median, bilateralFilter]

plotting_images(images, titles)
