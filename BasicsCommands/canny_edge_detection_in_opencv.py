import cv2 as cv
from BasicsCommands.plotting_utilities import plotting_images, img_database

img = img_database(1, 0)
# img = cv.cvtColor(img, cv.COLOR_BGR2RGB)

canny = cv.Canny(img, 100, 200,)

titles = ['Original Image', 'Canny']
images = [img, canny]

plotting_images(images, titles)
