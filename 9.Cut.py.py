import cv2

src = cv2.imread("/home/cjy/Pictures/OpenCV/cat.png", cv2.IMREAD_COLOR)
height, width, channel = src.shape
print(height, width , channel)
dst = src.copy() 
roi = src[50:150, 200:300]
dst[0:100, 0:100] = roi

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()