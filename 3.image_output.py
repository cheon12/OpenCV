import cv2

image = cv2.imread("/home/cjy/Pictures/OpenCV/index.jpeg", cv2.IMREAD_GRAYSCALE)
cv2.imshow("Moon", image)
cv2.waitKey()
cv2.destroyAllWindows()