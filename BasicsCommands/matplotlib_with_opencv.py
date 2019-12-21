import cv2 as cv
from matplotlib import pyplot as plt

img = cv.imread('lena.jpg', 0)
cv.imshow('Lena', img)
img_convert = cv.cvtColor(img, cv.COLOR_BGR2RGB)

plt.imshow(img_convert)
plt.xticks([]), plt.yticks([])  # Remove XY coordinates from the plot
plt.show()

cv.waitKey(27)
cv.destroyAllWindows()
