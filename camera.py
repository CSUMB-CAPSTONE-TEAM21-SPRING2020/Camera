import cv2
import numpy as np
import sys
import time


cap = cv2.VideoCapture(0) # video camera

lower_green = np.array([40, 40, 40])
upper_green = np.array([80, 255, 200])

low_blue = np.array([94, 30, 2])
high_blue = np.array([150, 255, 200])



def calculate(green_mask, blue_mask): # print to console how many green/blue pixels there are
    green_count = cv2.countNonZero(green_mask)
    blue_count = cv2.countNonZero(blue_mask)
    green_percentage = round((green_count/green_mask.size) * 100, 2)
    blue_percentage = round((blue_count/blue_mask.size) * 100, 2)
    print(f"Greens: {green_percentage}% Blues: {blue_percentage}%")



def screenshot(): # use this if need to store the images, one original, one with greens only, and ones with blues only
    currentDir = sys.path[0]
    cv2.imwrite(f'{currentDir}/screenshot.png',cap.read()[1]) #saves it
    image = cv2.imread(f'{currentDir}/screenshot.png')
    
    hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    green = cv2.bitwise_and(image, image, mask=green_mask)
    cv2.imwrite(f'{currentDir}/maskgreen.png',green) #saves color mask

    blue_mask = cv2.inRange(hsv, low_blue, high_blue)
    blue = cv2.bitwise_and(image, image, mask=blue_mask)
    cv2.imwrite(f'{currentDir}/maskblue.png',blue) #saves color mask
    print("Screenshot Taken")
    calculate()



def video():
    t1 = time.time() #small delay before first finding blue and green
    period1 = 5 # do calculate every _ second
    sleep_seconds = 0.01

    while True:
        _, frame = cap.read()
        _, frame2 = cap.read()
        hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
        hsv2 = cv2.cvtColor(frame2, cv2.COLOR_BGR2HSV)
        
        #color masks to filter out colors not within range and show to screen
        green_mask = cv2.inRange(hsv, lower_green, upper_green)
        green = cv2.bitwise_and(frame, frame, mask=green_mask)

        #color masks to filter out colors not within range and show to screen
        blue_mask = cv2.inRange(hsv2, low_blue, high_blue)
        blue = cv2.bitwise_and(frame2, frame2, mask=blue_mask)


        #try and catch to handle different OS. They require different number of parameters or else it'll crash
        try:
            #contours to create rectangles around the colors
            (contours_green,_) = cv2.findContours(green_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            (contours_blue,_) = cv2.findContours(blue_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        except:
            (_,contours_green,_) = cv2.findContours(green_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            (_,contours_blue,_) = cv2.findContours(blue_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


        #draw rectangles around where green is spotted
        for contour in contours_green:
            area = cv2.contourArea(contour)
            if(area > 500):
                x,y,w,h = cv2.boundingRect(contour)
                frame = cv2.rectangle(frame, (x,y),(x+w,y+h),(0,255,0),10)
                
        #draw rectangles around where blue is spotted
        for contour in contours_blue:
            area = cv2.contourArea(contour)
            if(area > 500):
                x,y,w,h = cv2.boundingRect(contour)
                frame2 = cv2.rectangle(frame2, (x,y),(x+w,y+h),(255,0,0),10)
                
        #Stacking video frames into one gui
        numpy_horizontal1 = np.hstack((frame, frame2))
        numpy_horizontal2 = np.hstack((green, blue))
        numpy_vertical = np.vstack((numpy_horizontal1, numpy_horizontal2))
        cv2.imshow("Berry Harvest Optimizer", numpy_vertical)
        
        #cv2.imshow("camera", frame)
        #cv2.imshow("green", green)
        #cv2.imshow("blue", blue)

        k = cv2.waitKey(1)
        if k == 27: #escape key to exit
            break
        if k == ord('z'): #z key to exit
            break
        if k == ord('s'):
            screenshot()
        if k == ord('c'):
            calculate(green_mask, blue_mask)


    


        t = time.time()
        if t - t1 >= period1: #calls every period1 seconds
            #screenshot()
            calculate(green_mask, blue_mask)
            t1 = time.time()

        time.sleep( sleep_seconds )






    # Find OpenCV version
        (major_ver, minor_ver, subminor_ver) = (cv2.__version__).split('.')
        
       # With webcam get(CV_CAP_PROP_FPS) does not work.
       # Let's see for ourselves.
        
        if int(major_ver)  < 3 :
            fps = cap.get(cv2.cv.CV_CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.cv.CV_CAP_PROP_FPS): {0}".format(fps))
        else :
            fps = cap.get(cv2.CAP_PROP_FPS)
            print("Frames per second using video.get(cv2.CAP_PROP_FPS) : {0}".format(fps))


        # Number of frames to capture
        num_frames = 120;


        print("Capturing {0} frames".format(num_frames))

        # Start time
        start = time.time()

        # Grab a few frames
        for i in xrange(0, num_frames) :
            ret, frame = video.read()


        # End time
        end = time.time()

        # Time elapsed
        seconds = end - start
        print("Time taken : {0} seconds".format(seconds))

        # Calculate frames per second
        fps  = num_frames / seconds;
        print("Estimated frames per second : {0}".format(fps))
    
    

video() #initiate video when program starts
    
cv2.destroyAllWindows()
cap.release()



    


