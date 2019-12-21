import numpy as np
import cv2 as cv


def nothing(x):
    pass


# cap = cv.VideoCapture(0)

cv.namedWindow('Tracking')
cv.createTrackbar('LH', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LS', 'Tracking', 0, 255, nothing)
cv.createTrackbar('LV', 'Tracking', 0, 255, nothing)
cv.createTrackbar('UH', 'Tracking', 255, 255, nothing)
cv.createTrackbar('US', 'Tracking', 255, 255, nothing)
cv.createTrackbar('UV', 'Tracking', 255, 255, nothing)

while True:

    frame = cv.imread('/home/erick/Downloads/brincando-com-git-master/TestandoOpenCV/2_processed_img.png')

    # _, frame = cap.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

    l_h = cv.getTrackbarPos('LH', 'Tracking')
    l_s = cv.getTrackbarPos('LS', 'Tracking')
    l_v = cv.getTrackbarPos('LV', 'Tracking')

    u_h = cv.getTrackbarPos('UH', 'Tracking')
    u_s = cv.getTrackbarPos('US', 'Tracking')
    u_v = cv.getTrackbarPos('UV', 'Tracking')

    l_b = np.array([l_h, l_s, l_v])
    u_b = np.array([u_h, u_s, u_v])

    mask = cv.inRange(hsv, l_b, u_b)

    res = cv.bitwise_and(frame, frame, mask=mask)

    cv.imshow('frame', frame)
    cv.imshow('mask', mask)
    cv.imshow('res', res)

    k = cv.waitKey(1) & 0xFF
    if k == 27:
        cv.imwrite('/home/erick/Downloads/brincando-com-git-master/TestandoOpenCV/mask.png', mask)
        break

# cap.release()
cv.destroyAllWindows()
