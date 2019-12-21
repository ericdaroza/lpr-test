import cv2 as cv
from matplotlib import pyplot as plt
from math import ceil


class plotting_utilities:

    color_def = [0, 1, -1, cv.IMREAD_GRAYSCALE, cv.IMREAD_COLOR]


    def plotting_images(images_vet, titles_vet):
        column = int(ceil((len(images_vet)**.5)))
        lines = int(round(len(images_vet)**.5))

        for i in range(len(images_vet)):
            plt.subplot(lines, column, i+1), plt.imshow(images_vet[i], 'gray')
            plt.title(titles_vet[i])
            plt.xticks([]), plt.yticks([])

        plt.show()


    def img_database(image, color_definition):

        images_array = [cv.imread('water.png', color_def[color_definition]),
                        cv.imread('lena.jpg', color_def[color_definition]),
                        cv.imread('carro2.jpg', color_def[color_definition]),
                        cv.imread('opencv-logo.png', color_def[color_definition]),
                        cv.imread('smarties.png', color_def[color_definition]),
                        cv.imread('Halftone_Gaussian_Blur.jpg', color_def[color_definition]),
                        cv.imread('carro1.jpg', color_def[color_definition]),
                        cv.imread('carro3.jpeg', color_def[color_definition]),
                        cv.imread('carro4.png', color_def[color_definition]),
                        cv.imread('smarties.png', color_def[color_definition]),
                        cv.imread('sudoku.png', color_def[color_definition]),
                        cv.imread('gradient.png', color_def[color_definition]),
                        cv.imread('messi5.jpg', color_def[color_definition]),
                        cv.imread('apple.jpg', color_def[color_definition]),
                        cv.imread('orange.jpg', color_def[color_definition])
                        ]

        return images_array[image]

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
