import cv2
import numpy as np

"""
img1 = cv2.imread("C:/Users/apc/Downloads/kot.jpg")
img2 = cv2.imread("C:/Users/apc/Downloads/kotblur.jpg")
diff = cv2.absdiff(img1, img2)
mask = cv2.cvtColor(diff, cv2.COLOR_BGR2GRAY)

th = 1
imask =  mask > th

canvas = np.zeros_like(img2, np.uint8)
canvas[imask] = img2[imask]

cv2.imwrite("result.png", canvas)
"""

# load images
image1 = cv2.imread("D:/Projects/Input/kot.jpg")
image2 = cv2.imread("D:/Projects/Input/kotblur.jpg")

# compute difference
difference = cv2.subtract(image1, image2)

# color the mask red
Conv_hsv_Gray = cv2.cvtColor(difference, cv2.COLOR_BGR2GRAY)
_, mask = cv2.threshold(Conv_hsv_Gray, 0, 255, cv2.THRESH_BINARY_INV)
difference[mask != 255] = [0, 0, 255]

# add the red mask to the images to make the differences obvious
image1[mask != 255] = [0, 0, 255]
image2[mask != 255] = [0, 0, 255]

# store images
cv2.imwrite('D:/Projects/Output/diffOverImage1.png', image1)
cv2.imwrite('D:/Projects/Output/diffOverImage2.png', image1)
cv2.imwrite('D:/Projects/Output/diff.png', difference)
