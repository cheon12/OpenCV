import cv2
src=cv2.imread('/home/cjy/Pictures/OpenCV/cat.png',cv2.IMREAD_COLOR)
hsv=cv2.cvtColor(src,cv2.COLOR_BGR2HSV)
h, s, v = cv2.split(hsv)

h = cv2.inRange(h, 0, 40)
orange = cv2.bitwise_and(hsv, hsv, mask = h)
orange = cv2.cvtColor(orange, cv2.COLOR_HSV2BGR)
cv2.imshow("cat",hsv)
cv2.imshow("orange", orange)
cv2.waitKey()
cv2.destroyAllWindows()