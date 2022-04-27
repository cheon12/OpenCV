import cv2

src = cv2.imread("/home/cjy/Pictures/OpenCV/cat.png", cv2.IMREAD_COLOR)
dst = cv2.flip(src, -2)

cv2.imshow("src", src)
cv2.imshow("dst", dst)
cv2.waitKey()
cv2.destroyAllWindows()