import cv2

img = cv2.imread('assets\Mihir.jpeg', 0)

# resize
img = cv2.resize(img,(400,400))
# img = cv2.resize(img, (0,0), fx=0.5, fy=0.5)

# rotate
# img=cv2.rotate(img, cv2.ROTATE_90_CLOCKWISE)

# write image
cv2.imwrite("new_img.jpeg",img)

cv2.imshow('MIHIR',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
