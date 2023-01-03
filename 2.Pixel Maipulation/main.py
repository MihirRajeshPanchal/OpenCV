import cv2
import random

img = cv2.imread("C:\\Users\\Mihir\\OneDrive\\Pictures\\Screenshots\\Screenshot_20221230_164913.png", -1)

# Change first 100 rows to random pixels
for i in range(10):
	for j in range(img.shape[1]):
		img[i][j] = [random.randint(0, 255), random.randint(0, 255), random.randint(0, 255),random.randint(0, 255)]

# Copy part of image
tag = img[20:70, 40:90]
img[90:140, 85:135] = tag

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()