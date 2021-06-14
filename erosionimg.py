import cv2
import numpy as np

img = cv2.imread('brain.jpg',1)
kernel = np.ones((5,5),np.uint8)
erosion = cv2.erode(img,kernel,iterations = 1)
opening = cv2.morphologyEx(erosion, cv2.MORPH_OPEN, kernel)

cv2.imshow('erosion',erosion)
cv2.imshow('opening',opening)
cv2.imwrite('brain_erode_opening.jpg',opening)
#cv2.imwrite('brain_erode.jpg',erosion)