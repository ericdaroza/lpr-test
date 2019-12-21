# DetectChars.py
import os

import cv2
import numpy as np


# module level variables ##########################################################################

kNearest = cv2.ml.KNearest_create()

# constants for checkIfPossibleChar, this checks one possible char only (does not compare to another char)
MIN_PIXEL_WIDTH = 2
MIN_PIXEL_HEIGHT = 8

MIN_ASPECT_RATIO = 0.25
MAX_ASPECT_RATIO = 1.0

MIN_PIXEL_AREA = 80

# constants for comparing two chars
MIN_DIAG_SIZE_MULTIPLE_AWAY = 0.3
MAX_DIAG_SIZE_MULTIPLE_AWAY = 5.0

MAX_CHANGE_IN_AREA = 0.5

MAX_CHANGE_IN_WIDTH = 0.8
MAX_CHANGE_IN_HEIGHT = 0.2

MAX_ANGLE_BETWEEN_CHARS = 12.0

# other constants
MIN_NUMBER_OF_MATCHING_CHARS = 3

RESIZED_CHAR_IMAGE_WIDTH = 20
RESIZED_CHAR_IMAGE_HEIGHT = 30

MIN_CONTOUR_AREA = 100


###################################################################################################


def stload_knn_data_data_and_train_knn():
    # all_contours_with_data = []  # declare empty lists,
    # valid_contours_with_data = []  # we will fill these shortly

    try:
        npa_classifications = np.loadtxt("classifications.txt", np.float32)  # read in training  # classifications

    except:  # if file could not be opened
        print("error, unable to open classifications.txt, exiting program\n")  # show error message
        os.system("pause")
        return False  # and return False
    # end try

    try:
        npa_flattened_images = np.loadtxt("flattened_images.txt", np.float32)  # read in training images

    except:  # if file could not be opened
        print("error, unable to open flattened_images.txt, exiting program\n")  # show error message
        os.system("pause")
        return False  # and return False
    # end try

    npa_classifications = npa_classifications.reshape(
        (npa_classifications.size, 1))  # reshape numpy array to 1d, necessary to pass to call to train

    kNearest.setDefaultK(1)  # set default K to 1

    kNearest.train(npa_flattened_images, cv2.ml.ROW_SAMPLE, npa_classifications)  # train KNN object

    return True  # if we got here training was successful so return true


# end function

###################################################################################################
