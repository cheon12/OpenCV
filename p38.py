import cv2, random

image=cv2.imread('../data/cat.png')
w,h=image.shape[1], image.shape[0]

def rand_pt(mult=1.):
    return(random.randrange(int(w*mult)),random.randrange(int(h*mult)))

cv2.circle(image, rand_pt(),40,(255,0,0))
cv2.circle(image, rand_pt(),5,(255,0,0),cv2.FILLED)
cv2.circle(image, rand_pt(),40,(255,85,85),2)
cv2.circle(image, rand_pt(),40,(255,170,170),2,cv2.LINE_AA)

cv2.line(image,rand_pt(),rand_pt(),(0,255,0))
cv2.line(image,rand_pt(),rand_pt(),(85,255,85),3)
cv2.line(image,rand_pt(),rand_pt(),(170,255,170),3,cv2.LINE_AA)

cv2.putText(image,'OpenCV',rand_pt(),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,0),3)

while True:
    cv2.imshow('window',image)