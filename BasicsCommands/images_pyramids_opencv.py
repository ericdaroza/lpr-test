import cv2 as cv
from BasicsCommands.plotting_utilities import plotting_images, img_database

img = img_database(1, 3)
img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

layer = img.copy()
gp = [layer]
titles = ['Original Image']
lp = [layer]*7

for i in range(6):
    layer = cv.pyrDown(layer)
    gp.append(layer)
    titles.append('pyrDown ' + str(i+1))

plotting_images(gp, titles)

for i in range(5, 0, -1):
    gaussian_extended = cv.pyrUp(gp[i])
    laplacian = cv.subtract(gp[i-1], gaussian_extended)
    titles[i] = 'pyrUP ' + str(6-i)
    lp[i] = laplacian

plotting_images(lp, titles)
"""
cv.imshow('Original Image', img)
cv.waitKey(0)
cv.destroyAllWindows()
"""
