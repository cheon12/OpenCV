import cv2

capture = cv2.VideoCapture("/home/cjy/Pictures/OpenCV/1.mp4")

while cv2.waitKey(33) !=ord('q') :
    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.set(cv2.CAP_PROP_POS_FRAMES, 0)

    ret, frame = capture.read()
    dst = cv2.resize(frame, dsize=(640, 480), interpolation=cv2.INTER_AREA)
    cv2.imshow("VideoFrame", dst)

capture.release()
cv2.destroyAllWindows()