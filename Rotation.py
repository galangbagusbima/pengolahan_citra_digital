import cv2

load = cv2.imread('galang.jpg', 1)
width, heighmyt = load.shape[1], load.shape[2]

rotate = cv2.getRotationMatrix2D((width/2, height/2), 180, 1)
img_rotate = cv2.warpAffine(load, rotate, (width, height))

cv2.imshow('Image Rotate', img_rotate)

cv2.waitkey(0)
cv2.destroyAllwindows()