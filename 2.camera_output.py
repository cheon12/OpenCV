import cv2

capture = cv2.VideoCapture(0)
capture.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
capture.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
capture.set(cv2.CAP_PROP_FPS,0.1)

while cv2.waitKey(33) !=ord('q') :
    ret, frame = capture.read()
    cv2.imshow("VideoFrame", frame)
capture.release()
cv2.destroyAllWindows()