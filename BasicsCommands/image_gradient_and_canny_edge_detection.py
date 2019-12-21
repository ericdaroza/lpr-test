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
                cv.imread('sudoku.png', cv.IMREAD_GRAYSCALE), cv.imread('gradient.png', cv.IMREAD_GRAYSCALE),
                cv.imread('messi5.jpg', cv.IMREAD_GRAYSCALE)
                ]

# 0 -> water
# 1 -> lena
# 2 -> carro2
# 3 -> opencv-logo
# 4 -> smarties
# 5 -> Halftone_Gaussian_Blur
# 6 -> carro1
# 7 -> carro3
# 8 -> carro4
# 9 -> smarties
# 10 -> sudoku
# 11 -> gradient
# 12 -> messi5

kernal = np.ones((2, 2), np.uint8)

img = img_database[12]
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

lap = cv.Laplacian(img, cv.CV_64F, ksize=3)
lap = np.uint8(np.absolute(lap))
sobelX = cv.Sobel(img, cv.CV_64F, 1, 0)
sobelY = cv.Sobel(img, cv.CV_64F, 0, 1)
edges = cv.Canny(img, 100, 200)

sobelX = np.uint8(np.absolute(sobelX))
sobelY = np.uint8(np.absolute(sobelY))

sobelCombined = cv.bitwise_or(sobelX, sobelY)


titles = ['Original Image', 'Laplacian Gradient', 'Sobel X', 'Sobel Y', 'Sobel Combined', 'Canny']
images = [img, lap, sobelX, sobelY, sobelCombined, edges]

plotting_images(images, titles)
