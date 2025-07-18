import cv2 as cv

# reading images
img = cv.imread('photos/my pic.PNG')

cv.imshow('Sajjad',img)
cv.waitKey(0)
#reading videos
capture = cv.VideoCapture('videos/vid.mp4')  #we can give the reference for 
                                #the camera connected to the system 0 for the webcam 

while True:
    isTrue, frame = capture.read()
    cv.imshow('Video',frame)

    if(cv.waitKey(20)& 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()
