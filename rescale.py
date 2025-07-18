import cv2 as cv

# # # reading images
img = cv.imread('photos/my pic.PNG')

cv.imshow('Sajjad',img)

def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1]*scale)
    height = int(frame.shape[0]*scale)
    dimmentions = (width,height)
    return cv.resize(frame,dimmentions,interpolation=cv.INTER_AREA)


def changeReolution(width, height):
    capture.set(3,width)
    capture.set(4,height)
    

resize_img = rescaleFrame(img)
cv.imshow('Sajjad_resized',resize_img)





capture = cv.VideoCapture('videos/vid.mp4')  

while True:
    isTrue, frame = capture.read()
    
    frame_resized = rescaleFrame(frame,scale=.2)
    cv.imshow('Video',frame)
    cv.imshow('Resized Video',frame_resized)
    if(cv.waitKey(20)& 0xFF==ord('d')):
        break
capture.release()
cv.destroyAllWindows()




cv.waitKey(0)