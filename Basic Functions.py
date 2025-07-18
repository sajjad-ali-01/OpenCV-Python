import cv2 as cv

img = cv.imread('photos/my pic.PNG')
cv.imshow('My pic',img)

#converting to the gray scale
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
cv.imshow('Gray image',gray)

#blur

blur = cv.GaussianBlur(img,(7,7),cv.BORDER_DEFAULT)
cv.imshow('blur',blur)

#Edge Cascade
canny = cv.Canny(img,125,175)
cv.imshow('Cascade',canny)

#delating
delating = cv.dilate(canny,(7,7),iterations=3)
cv.imshow('Dilating',delating) 

#eroding
eroding = cv.erode(delating,(3,3),iterations=1)
cv.imshow('eroding',eroding)

# Resize
resized = cv.resize(img, (500,500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Cropping
cropped = img[50:200, 200:400]
cv.imshow('Cropped', cropped)
cv.waitKey(0)