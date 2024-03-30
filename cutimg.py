import cv2
import numpy as np
import math as m
from matplotlib import pyplot as plt
import random as r

# 3x4 shape[0] = 3, shape[1] = 4
array = [[1, 2, 3, 4],
         [5, 6, 7, 8],
         [9, 0, 1, 2]]

array = np.array(array)
print(array.shape)


def cutImage(image, value):
    len = image.shape[0]
    wid = image.shape[1]
    wid = wid - value
    output = np.zeros((len, wid))

    for i in range(1, len(output)-1):
        for j in range(1, len(output[i])-1):
            (x, y, z) = image[i][j]

            output[i][j] = image[i][j]

    return output


img = cv2.imread("CIS_465\html\images\GerhartWorkPhoto.png", 1)
resize = cv2.resize(img, [550, 800], interpolation=cv2.INTER_AREA)

newimg = resize[0:620, 0:500]
cv2.imwrite("CIS_465\html\images\myPortrait.png", newimg)
cv2.imshow('Transformed', newimg)
cv2.imshow('Original', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
