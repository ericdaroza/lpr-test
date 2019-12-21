from BasicsCommands.shape_detection import geometric_finder as g_f
import cv2

img = cv2.imread('/home/erick/Downloads/brincando-com-git-master/TestandoOpenCV/BasicsCommands/Shapes.png')

cv2.imshow('Shapes', g_f(img))
cv2.waitKey(0)
cv2.destroyAllWindows()
