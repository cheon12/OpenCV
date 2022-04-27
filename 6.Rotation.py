import cv2

#src = cv2.imread("/home/cjy/Pictures/OpenCV/cat.png", cv2.IMREAD_COLOR)

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)

while cv2.waitKey(33) !=ord('q') :


    ret, frame = capture.read()
    height, width, channel = frame.shape
    matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
    dst = cv2.warpAffine(frame, matrix, (width, height))
    cv2.imshow("freme", frame)
    cv2.imshow("VideoFrame", dst)
capture.release()
cv2.destroyAllWindows()


# height, width, channel = src.shape
# matrix = cv2.getRotationMatrix2D((width/2, height/2), 90, 1)
# dst = cv2.warpAffine(src, matrix, (width, height))

# cv2.imshow("src", src)
# cv2.imshow("dst", dst)
# cv2.waitKey()
# cv2.destroyAllWindows()
