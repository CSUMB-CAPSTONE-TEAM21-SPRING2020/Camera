import cv2
import numpy as np
import threading
import sys
import threading
import time


cam = cv2.VideoCapture(0) # image camera

def screenshot():
    global cam
   # cv2.imshow("screenshot", cam.read()[1]) # shows the screenshot directly
    currentDir = sys.path[0]
    frame = cv2.imread(f'{currentDir}/testImage2.jpg')
    
    lower_green = np.array([25, 20, 50])
    upper_green = np.array([80, 255, 255])
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)
    green_mask = cv2.inRange(hsv, lower_green, upper_green)
    cv2.imwrite(f'{currentDir}/mask.png',green_mask) #saves color mask to directory of script


screenshot()

cv2.destroyAllWindows()



    


