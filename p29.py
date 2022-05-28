import cv2

img=cv2.imread('../data/cat.png',cv2.IMREAD_GRAYSCALE)
print('original image shape: ',img.shape)
width,height=128,256
resized_img=cv2.resize(img,(width,height))
print('resizzed to 128x256 image shape: ',resized_img.shape)