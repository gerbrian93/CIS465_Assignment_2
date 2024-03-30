import cv2
import numpy as np
import math as m
from matplotlib import pyplot as plt
import random as r


def changeImage(image):
    fill = 1
    bilist = []
    while fill < len(image)-1:
        bilist.append([])
        fill += 1
    for i in range(1, len(image)-1):
        for j in range(1, len(image[i])-1):
            x = image[i][j]
            g1 = image[i][j+1]
            g2 = image[i-1][j+1]
            g3 = image[i-1][j]
            g4 = image[i-1][j-1]
            g5 = image[i][j-1]
            g6 = image[i+1][j-1]
            g7 = image[i+1][j]
            g8 = image[i+1][j+1]

            bistr = ''
            for k in [g1, g2, g3, g4, g5, g6, g7, g8]:
                if int(k) - int(x) >= 0:
                    bistr += '1'
                else:
                    bistr += '0'
            bilist[i-1].append(int(bistr, 2))
    return np.array(bilist)

# greyscale transformation 1: binary image transformation


def T1(image):
    fill = 0
    bilist = []
    while fill < len(image):
        bilist.append([])
        fill += 1
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            x = image[i][j]

            if x < 70 and 170:
                x = 0
            elif x >= 70 and 170:
                x = 255 - x
            bilist[i].append(x)

    return np.array(bilist)

# greyscale transformation 2: Interval reservation transformation


def T2(image):
    fill = 0
    bilist = []
    while fill < len(image):
        bilist.append([])
        fill += 1
    t1 = 70
    t2 = 170
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            x = image[i][j]
            if x < t1:
                x = 0
            elif x >= t1 and x <= t2:
                x = x
            elif x > t2:
                x = 0
            bilist[i].append(x)

    return np.array(bilist)


# greyscale transformation 3: Log Base 10 Transformation
def T3(image):
    fill = 0
    bilist = []
    while fill < len(image):
        bilist.append([])
        fill += 1
    c = 255/m.log10(1+255)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            x = image[i][j]

            s = c*m.log10(1+x)
            bilist[i].append(s)

    return np.array(bilist)

# greyscale transformation 4: Gamma Correction Transformation


def T4(image):
    fill = 0
    bilist = []
    while fill < len(image):
        bilist.append([])
        fill += 1
    gamma = 1.8
    c = 255/m.pow(255, gamma)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            x = image[i][j]
            s = int(c*m.pow(x, gamma))
            bilist[i].append(s)
    return np.array(bilist)


def T5(image):  # colored input (r,g,b) for every pixel
    #r,c = image.shape
    #bilist = np.empty((r, c))
    fill = 0
    bilist = []
    while fill < len(image):
        bilist.append([])
        fill += 1
    gamma = 1.5
    c = 255/m.pow(255, gamma)
    for i in range(0, len(image)):
        for j in range(0, len(image[i])):
            (r, g, b) = image[i][j]
            x = (r/3)+(g/3)+(b/3)

            bilist[i].append(x)
    return np.array(bilist)


image = cv2.imread("CIS_465\html\images\jWebb.jpg", 2)
resize = cv2.resize(image, [800, 550], interpolation=cv2.INTER_AREA)

newimg = T1(resize)
newimg = newimg.astype(np.uint8)

cv2.imshow('Transformed', newimg)
cv2.imshow('Original', resize)
cv2.waitKey(0)
cv2.destroyAllWindows()
