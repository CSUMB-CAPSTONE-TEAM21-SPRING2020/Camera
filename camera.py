import sys

# import some PyQt5 modules
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtGui import QImage
from PyQt5.QtGui import QPixmap
from PyQt5.QtCore import QTimer
from PyQt5.QtCore import pyqtSlot
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (QWidget, QLabel, QLineEdit, QTextEdit, QGridLayout, QApplication, QVBoxLayout, QSlider)
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
import time
import math
import cv2
#from ui_main_window import *
import numpy as np
import threading
from threading import Timer
import pathlib


class MainWindow(QWidget):
    # class constructor
    def __init__(self):
        # call QWidget constructor
        super().__init__()
        
        #total measurements made before sending data
        self.current_averages_list = []
        
        self.text_messages_list = []
        
        # color values
        self.lower_green = np.array([40, 40, 40])
        self.upper_green = np.array([80, 255, 200])
        self.lower_blue = np.array([94, 30, 2])
        self.upper_blue = np.array([150, 255, 200])
                
        #get screen resolution for scaling
        self.windowObject = QtWidgets.QDesktopWidget().screenGeometry(-1)
        self.screen_height = self.windowObject.height()
        self.screen_width = self.windowObject.width()

        #GUI layouts
        self.videos_grid = QHBoxLayout() #bottom part, under sliders
        self.green_videos_grid = QVBoxLayout()
        self.blue_videos_grid = QVBoxLayout()
        self.sliders_grid = QGridLayout()
        self.buttons_grid = QGridLayout()
        self.main_grid = QVBoxLayout()
        
        
        
        #Defualt button to reset settings
        self.default_button = QPushButton('Default')
        self.default_button.clicked.connect(self.restore_default_settings)
        self.buttons_grid.addWidget(self.default_button,0,0)
        
        # button to save settings
        self.save_button = QPushButton('Save')
        self.save_button.clicked.connect(self.save_settings)
        self.buttons_grid.addWidget(self.save_button,0,1)
        
        # button to exit
        self.exit_button = QPushButton('Exit')
        self.exit_button.clicked.connect(self.controlTimer)
        self.buttons_grid.addWidget(self.exit_button,0,3)
        
        self.exit_button = QPushButton('Exit')

        self.text_panel = QPlainTextEdit(self)
        self.text_panel.setReadOnly(True)
        
        
        
        
        self.lower_green_label = QLabel("Lower Green Values ")
        self.lower_green_h_slider_label = QLabel("Lower Green H Value")
        self.lower_green_s_slider_label = QLabel("Lower Green S Value")
        self.lower_green_v_slider_label = QLabel("Lower Green V Value")

        self.upper_green_label = QLabel("Upper Green Values ")
        self.upper_green_h_slider_label = QLabel("Upper Green H Value")
        self.upper_green_s_slider_label = QLabel("Upper Green S Value")
        self.upper_green_v_slider_label = QLabel("Upper Green V Value")
        
        #slider1 lower green h
        self.slider1 = QSlider(Qt.Horizontal)
        self.slider1.valueChanged[int].connect(self.changeValueLowerGreenHSlider)
        self.slider1.setTickInterval(1)
        self.slider1.setMinimum(0)
        self.slider1.setMaximum(255)
        self.slider1.setValue(self.lower_green[0])
        
        #slider1 lower green s
        self.slider2 = QSlider(Qt.Horizontal)
        self.slider2.valueChanged[int].connect(self.changeValueLowerGreenSSlider)
        self.slider2.setTickInterval(1)
        self.slider2.setMinimum(0)
        self.slider2.setMaximum(255)
        self.slider2.setValue(self.lower_green[1])
        
        #slider1 lower green v
        self.slider3 = QSlider(Qt.Horizontal)
        self.slider3.valueChanged[int].connect(self.changeValueLowerGreenVSlider)
        self.slider3.setTickInterval(1)
        self.slider3.setMinimum(0)
        self.slider3.setMaximum(255)
        self.slider3.setValue(self.lower_green[2])
          
        #slider1 upper green h
        self.slider4 = QSlider(Qt.Horizontal)
        self.slider4.valueChanged[int].connect(self.changeValueUpperGreenHSlider)
        self.slider4.setTickInterval(1)
        self.slider4.setMinimum(0)
        self.slider4.setMaximum(255)
        self.slider4.setValue(self.upper_green[0])
        
        #slider1 upper green s
        self.slider5 = QSlider(Qt.Horizontal)
        self.slider5.valueChanged[int].connect(self.changeValueUpperGreenSSlider)
        self.slider5.setTickInterval(1)
        self.slider5.setMinimum(0)
        self.slider5.setMaximum(255)
        self.slider5.setValue(self.upper_green[1])
        
        #slider1 upper green v
        self.slider6 = QSlider(Qt.Horizontal)
        self.slider6.valueChanged[int].connect(self.changeValueUpperGreenVSlider)
        self.slider6.setTickInterval(1)
        self.slider6.setMinimum(0)
        self.slider6.setMaximum(255)
        self.slider6.setValue(self.upper_green[2])
        
        
        self.lower_blue_label = QLabel("Lower Blue Values ")
        self.lower_blue_h_slider_label = QLabel("Lower Blue H Value")
        self.lower_blue_s_slider_label = QLabel("Lower Blue S Value")
        self.lower_blue_v_slider_label = QLabel("Lower Blue V Value")

        self.upper_blue_label = QLabel("Upper Blue Values ")
        self.upper_blue_h_slider_label = QLabel("Upper Blue H Value")
        self.upper_blue_s_slider_label = QLabel("Upper Blue S Value")
        self.upper_blue_v_slider_label = QLabel("Upper Blue V Value")
        
        
        #slider1 lower blue h
        self.slider7 = QSlider(Qt.Horizontal)
        self.slider7.valueChanged[int].connect(self.changeValueLowerBlueHSlider)
        self.slider7.setTickInterval(1)
        self.slider7.setMinimum(0)
        self.slider7.setMaximum(255)
        self.slider7.setValue(self.lower_blue[0])
        
        #slider1 lower blue s
        self.slider8 = QSlider(Qt.Horizontal)
        self.slider8.valueChanged[int].connect(self.changeValueLowerBlueSSlider)
        self.slider8.setTickInterval(1)
        self.slider8.setMinimum(0)
        self.slider8.setMaximum(255)
        self.slider8.setValue(self.lower_blue[1])
        
        #slider1 lower blue v
        self.slider9 = QSlider(Qt.Horizontal)
        self.slider9.valueChanged[int].connect(self.changeValueLowerBlueVSlider)
        self.slider9.setTickInterval(1)
        self.slider9.setMinimum(0)
        self.slider9.setMaximum(255)
        self.slider9.setValue(self.lower_blue[2])
          
        #slider1 upper blue h
        self.slider10 = QSlider(Qt.Horizontal)
        self.slider10.valueChanged[int].connect(self.changeValueUpperBlueHSlider)
        self.slider10.setTickInterval(1)
        self.slider10.setMinimum(0)
        self.slider10.setMaximum(255)
        self.slider10.setValue(self.upper_blue[0])
        
        #slider1 upper blue s
        self.slider11 = QSlider(Qt.Horizontal)
        self.slider11.valueChanged[int].connect(self.changeValueUpperBlueSSlider)
        self.slider11.setTickInterval(1)
        self.slider11.setMinimum(0)
        self.slider11.setMaximum(255)
        self.slider11.setValue(self.upper_blue[1])
        
        #slider1 upper blue v
        self.slider12 = QSlider(Qt.Horizontal)
        self.slider12.valueChanged[int].connect(self.changeValueUpperBlueVSlider)
        self.slider12.setTickInterval(1)
        self.slider12.setMinimum(0)
        self.slider12.setMaximum(255)
        self.slider12.setValue(self.upper_blue[2])
        
        
        #Label are for video frame
        self.image_frame1 = QLabel()
        self.image_frame1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_frame1.setAlignment(Qt.AlignCenter)
        
        #Label are for video frame
        self.image_frame2 = QLabel()
        self.image_frame2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_frame2.setAlignment(Qt.AlignCenter)
        
        #Label are for video frame
        self.image_frame3 = QLabel()
        self.image_frame3.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_frame3.setAlignment(Qt.AlignCenter)
        
        #Label are for video frame
        self.image_frame4 = QLabel()
        self.image_frame4.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.image_frame4.setAlignment(Qt.AlignCenter)

        #green sliders
        self.sliders_grid.addWidget(self.lower_green_label, 0, 0)
        self.sliders_grid.addWidget(self.lower_green_h_slider_label, 1, 0)
        self.sliders_grid.addWidget(self.slider1, 1, 1)
        self.sliders_grid.addWidget(self.lower_green_s_slider_label, 2, 0)
        self.sliders_grid.addWidget(self.slider2, 2, 1)
        self.sliders_grid.addWidget(self.lower_green_v_slider_label, 3, 0)
        self.sliders_grid.addWidget(self.slider3, 3, 1)

        self.sliders_grid.addWidget(self.upper_green_label, 4, 0)
        self.sliders_grid.addWidget(self.upper_green_h_slider_label, 5, 0)
        self.sliders_grid.addWidget(self.slider4, 5, 1)
        self.sliders_grid.addWidget(self.upper_green_s_slider_label, 6, 0)
        self.sliders_grid.addWidget(self.slider5, 6, 1)
        self.sliders_grid.addWidget(self.upper_green_v_slider_label, 7, 0)
        self.sliders_grid.addWidget(self.slider6, 7, 1)

        #blue sliders
        self.sliders_grid.addWidget(self.lower_blue_label, 0, 3)
        self.sliders_grid.addWidget(self.lower_blue_h_slider_label, 1, 3)
        self.sliders_grid.addWidget(self.slider7, 1, 4)
        self.sliders_grid.addWidget(self.lower_blue_s_slider_label, 2, 3)
        self.sliders_grid.addWidget(self.slider8, 2, 4)
        self.sliders_grid.addWidget(self.lower_blue_v_slider_label, 3, 3)
        self.sliders_grid.addWidget(self.slider9, 3, 4)

        self.sliders_grid.addWidget(self.upper_blue_label, 4, 3)
        self.sliders_grid.addWidget(self.upper_blue_h_slider_label, 5, 3)
        self.sliders_grid.addWidget(self.slider10, 5, 4)
        self.sliders_grid.addWidget(self.upper_blue_s_slider_label, 6, 3)
        self.sliders_grid.addWidget(self.slider11, 6, 4)
        self.sliders_grid.addWidget(self.upper_blue_v_slider_label, 7, 3)
        self.sliders_grid.addWidget(self.slider12, 7, 4)

          

        #add video frames to layout
        self.green_videos_grid.addWidget(self.image_frame1)
        self.blue_videos_grid.addWidget(self.image_frame2)
        self.green_videos_grid.addWidget(self.image_frame3)
        self.blue_videos_grid.addWidget(self.image_frame4)

        self.videos_grid.addLayout(self.green_videos_grid)
        self.videos_grid.addWidget(self.text_panel)
        self.videos_grid.addLayout(self.blue_videos_grid)

        #main grid adding subgrids
        self.main_grid.addLayout(self.buttons_grid)
        self.main_grid.addLayout(self.sliders_grid)
        self.main_grid.addLayout(self.videos_grid)
        self.setLayout(self.main_grid)
        self.setGeometry(0, 0, self.screen_width, self.screen_height)
        self.setWindowTitle('Blueberry Harvest Optimizer')
               
               
        
        # create a timer
        self.timer = QTimer()
        # set timer timeout callback function
        self.timer.timeout.connect(self.viewCam)
        
        self.cap = cv2.VideoCapture(0)


        # read image in BGR format
        _, self.frame1 = self.cap.read()
        _, self.frame2 = self.cap.read()

        # convert image to RGB format
        self.frame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB)
        self.frame2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2RGB)
        self.hsv = cv2.cvtColor(self.frame1, cv2.COLOR_RGB2HSV)
        self.hsv2 = cv2.cvtColor(self.frame2, cv2.COLOR_RGB2HSV)
        
        #color masks to filter out colors not within range and show to screen
        self.green_mask = cv2.inRange(self.hsv, self.lower_green, self.upper_green)
        self.green = cv2.bitwise_and(self.frame1, self.frame1, mask=self.green_mask)

        #color masks to filter out colors not within range and show to screen
        self.blue_mask = cv2.inRange(self.hsv2, self.lower_blue, self.upper_blue)
        self.blue = cv2.bitwise_and(self.frame2, self.frame2, mask=self.blue_mask)
        

    #functions to change values according to sliders
    def changeValueLowerGreenHSlider(self, value):
        self.lower_green_h_slider_label.setText("H: " + str(value))
        self.lower_green[0] = value
        
    def changeValueLowerGreenSSlider(self, value):
        self.lower_green_s_slider_label.setText("S: " + str(value))
        self.lower_green[1] = value
        
    def changeValueLowerGreenVSlider(self, value):
        self.lower_green_v_slider_label.setText("V: " + str(value))
        self.lower_green[2] = value

    def changeValueUpperGreenHSlider(self, value):
        self.upper_green_h_slider_label.setText("H: " + str(value))
        self.upper_green[0] = value
        
    def changeValueUpperGreenSSlider(self, value):
        self.upper_green_s_slider_label.setText("S: " + str(value))
        self.upper_green[1] = value
        
    def changeValueUpperGreenVSlider(self, value):
        self.upper_green_v_slider_label.setText("V: " + str(value))
        self.upper_green[2] = value
    
    def changeValueLowerBlueHSlider(self, value):
        self.lower_blue_h_slider_label.setText("H: " + str(value))
        self.lower_blue[0] = value
        
    def changeValueLowerBlueSSlider(self, value):
        self.lower_blue_s_slider_label.setText("S: " + str(value))
        self.lower_blue[1] = value
        
    def changeValueLowerBlueVSlider(self, value):
        self.lower_blue_v_slider_label.setText("V: " + str(value))
        self.lower_blue[2] = value

    def changeValueUpperBlueHSlider(self, value):
        self.upper_blue_h_slider_label.setText("H: " + str(value))
        self.upper_blue[0] = value
        
    def changeValueUpperBlueSSlider(self, value):
        self.upper_blue_s_slider_label.setText("S: " + str(value))
        self.upper_blue[1] = value

    def changeValueUpperBlueVSlider(self, value):
        self.upper_blue_v_slider_label.setText("V: " + str(value))
        self.upper_blue[2] = value

    
    
    
    def calculate(self, green_mask, blue_mask): # print to console how many green/blue pixels there are
        green_count = cv2.countNonZero(green_mask)
        blue_count = cv2.countNonZero(blue_mask)
        green_percentage = round((green_count/green_mask.size) * 100, 2)
        blue_percentage = round((blue_count/blue_mask.size) * 100, 2)
        mainWindow.update_messages(f"Greens: {green_percentage}% Blues: {blue_percentage}% \n")
        #mainWindow.text_panel.append(f"Greens: {green_percentage}% Blues: {blue_percentage}% \n")
        
        tempAverages = [green_percentage, blue_percentage]
        self.current_averages_list.append(tempAverages)

        #When reached limit, calculate total average and send data
        if len(self.current_averages_list) == 5:
            tempSumGreen = 0
            tempSumBlue = 0
            tempTotalGreenAverages = 0
            tempTotalBlueAverages = 0
            for x in range(0, len(self.current_averages_list)):
                tempSumGreen = tempSumGreen + self.current_averages_list[x][0]
                tempSumBlue = tempSumBlue + self.current_averages_list[x][1]
                tempTotalGreenAverages = tempSumGreen/len(self.current_averages_list)
                tempTotalBlueAverages = tempSumBlue/len(self.current_averages_list)
            mainWindow.update_messages(f"Average Greens: {tempTotalGreenAverages}% Average Blues: {tempTotalBlueAverages}% \n")
            mainWindow.update_messages(f"Data sent to Server \n")

            self.current_averages_list.clear()
            





    # view camera
    def viewCam(self):

        # read image in BGR format
        _, self.frame1 = self.cap.read()
        _, self.frame2 = self.cap.read()

        # convert image to RGB format
        self.frame1 = cv2.cvtColor(self.frame1, cv2.COLOR_BGR2RGB)
        self.frame2 = cv2.cvtColor(self.frame2, cv2.COLOR_BGR2RGB)
        self.hsv = cv2.cvtColor(self.frame1, cv2.COLOR_RGB2HSV)
        self.hsv2 = cv2.cvtColor(self.frame2, cv2.COLOR_RGB2HSV)
        
        #color masks to filter out colors not within range and show to screen
        self.green_mask = cv2.inRange(self.hsv, self.lower_green, self.upper_green)
        self.green = cv2.bitwise_and(self.frame1, self.frame1, mask=self.green_mask)

        #color masks to filter out colors not within range and show to screen
        self.blue_mask = cv2.inRange(self.hsv2, self.lower_blue, self.upper_blue)
        self.blue = cv2.bitwise_and(self.frame2, self.frame2, mask=self.blue_mask)
        
        #try and catch to handle different OS. They require different number of parameters or else it'll crash
        try:
            #contours to create rectangles around the colors
            (contours_green,_) = cv2.findContours(self.green_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            (contours_blue,_) = cv2.findContours(self.blue_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        except:
            (_,contours_green,_) = cv2.findContours(self.green_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
            (_,contours_blue,_) = cv2.findContours(self.blue_mask, cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)


        #draw rectangles around where green is spotted
        for contour in contours_green:
            area = cv2.contourArea(contour)
            if(area > 500):
                x,y,w,h = cv2.boundingRect(contour)
                self.frame1 = cv2.rectangle(self.frame1, (x,y),(x+w,y+h),(0,255,0),10)
                
        #draw rectangles around where blue is spotted
        for contour in contours_blue:
            area = cv2.contourArea(contour)
            if(area > 500):
                x,y,w,h = cv2.boundingRect(contour)
                self.frame2 = cv2.rectangle(self.frame2, (x,y),(x+w,y+h),(0,0,255),10)
                

                    
                    
                    
        # get image infos
        height1, width1, channel1 = self.frame1.shape
        height2, width2, channel2 = self.frame2.shape

        step1 = channel1 * width1
        step2 = channel2 * width2
        # create QImage from image
        qImg1 = QImage(self.frame1.data, width1, height1, step1, QImage.Format_RGB888)
        qImg2 = QImage(self.frame2.data, width2, height2, step2, QImage.Format_RGB888)
        qImg3 = QImage(self.green.data, width1, height1, step1, QImage.Format_RGB888)
        qImg4 = QImage(self.blue.data, width2, height2, step2, QImage.Format_RGB888)
        #resize frames
        qImg1 = qImg1.scaled(math.floor(self.screen_width/3), math.floor(self.screen_height/3), QtCore.Qt.KeepAspectRatio)
        qImg2 = qImg2.scaled(math.floor(self.screen_width/3), math.floor(self.screen_height/3), QtCore.Qt.KeepAspectRatio)
        qImg3 = qImg3.scaled(math.floor(self.screen_width/3), math.floor(self.screen_height/3), QtCore.Qt.KeepAspectRatio)
        qImg4 = qImg4.scaled(math.floor(self.screen_width/3), math.floor(self.screen_height/3), QtCore.Qt.KeepAspectRatio)
        
        # show image in img_label
        self.image_frame1.setPixmap(QPixmap.fromImage(qImg1))
        self.image_frame2.setPixmap(QPixmap.fromImage(qImg2))
        self.image_frame3.setPixmap(QPixmap.fromImage(qImg3))
        self.image_frame4.setPixmap(QPixmap.fromImage(qImg4))

        
        
    # start/stop timer, if timer stopped program closes
    def controlTimer(self):
        if not self.timer.isActive():
            # start timer
            self.timer.start(20)
        else:
            # stop timer, close program
            self.timer.stop()
            self.cap.release()
            mainWindow.close()


    #Check if user closed app, stop other threads
    def check_exit_status(self):
        if(mainWindow.isVisible() and self.timer.isActive()):
            Timer(1, mainWindow.check_exit_status).start()
        else:
            sys.exit()

    #Timer for when to capture data
    def capture_data_timer(self):
        if(mainWindow.isVisible() and self.timer.isActive()):
            Timer(5, mainWindow.capture_data_timer).start()
            mainWindow.calculate(self.green_mask, self.blue_mask)
        else:
            sys.exit()

    
    def update_messages(self,MYSTRING):
        #mainWindow.text_panel.append(MYSTRING) #append string
        #mainWindow.text_panel.setText("TEST")
        mainWindow.text_panel.insertPlainText(MYSTRING)

        mainWindow.text_messages_list.append(MYSTRING)
        
        QApplication.processEvents() #update gui for pyqt
        
    


    def save_settings(self):
        file = open("settings.txt", "w")
        file.write(f'{self.lower_green[0]}\n')
        file.write(f'{self.lower_green[1]}\n')
        file.write(f'{self.lower_green[2]}\n')
        file.write(f'{self.upper_green[0]}\n')
        file.write(f'{self.upper_green[1]}\n')
        file.write(f'{self.upper_green[2]}\n')
        file.write(f'{self.lower_blue[0]}\n')
        file.write(f'{self.lower_blue[1]}\n')
        file.write(f'{self.lower_blue[2]}\n')
        file.write(f'{self.upper_blue[0]}\n')
        file.write(f'{self.upper_blue[1]}\n')
        file.write(f'{self.upper_blue[2]}\n')
        file.close()
        self.hide()
        self.show()
        mainWindow.update_messages("Color Settings Saved. \n")




    #save a file containing the default settings
    def save_settings_default(self):
        self.file = open("settingsdefault.txt", "w")
        self.file.write(f'{self.lower_green[0]}\n')
        self.file.write(f'{self.lower_green[1]}\n')
        self.file.write(f'{self.lower_green[2]}\n')
        self.file.write(f'{self.upper_green[0]}\n')
        self.file.write(f'{self.upper_green[1]}\n')
        self.file.write(f'{self.upper_green[2]}\n')
        self.file.write(f'{self.lower_blue[0]}\n')
        self.file.write(f'{self.lower_blue[1]}\n')
        self.file.write(f'{self.lower_blue[2]}\n')
        self.file.write(f'{self.upper_blue[0]}\n')
        self.file.write(f'{self.upper_blue[1]}\n')
        self.file.write(f'{self.upper_blue[2]}\n')
        self.file.close()
        self.hide()
        self.show()
        
  
        
    #Load  default settings
    def restore_default_settings(self):
        file = open("settingsdefault.txt", "r")
        lines = file.readlines()
        self.lower_green[0] = int(lines[0])
        self.lower_green[1] = int(lines[1])
        self.lower_green[2] = int(lines[2])
        self.upper_green[0] = int(lines[3])
        self.upper_green[1] = int(lines[4])
        self.upper_green[2] = int(lines[5])
        self.lower_blue[0] = int(lines[6])
        self.lower_blue[1] = int(lines[7])
        self.lower_blue[2] = int(lines[8])
        self.upper_blue[0] = int(lines[9])
        self.upper_blue[1] = int(lines[10])
        self.upper_blue[2] = int(lines[11])
        
        self.slider1.setValue(self.lower_green[0])
        self.slider2.setValue(self.lower_green[1])
        self.slider3.setValue(self.lower_green[2])
        self.slider4.setValue(self.upper_green[0])
        self.slider5.setValue(self.upper_green[1])
        self.slider6.setValue(self.upper_green[2])
        self.slider7.setValue(self.lower_blue[0])
        self.slider8.setValue(self.lower_blue[1])
        self.slider9.setValue(self.lower_blue[2])
        self.slider10.setValue(self.upper_blue[0])
        self.slider11.setValue(self.upper_blue[1])
        self.slider12.setValue(self.upper_blue[2])
        self.hide()
        self.show()
        
        
        
    #Load user saved settings
    def restore_settings(self):
        file = open("settings.txt", "r")
        lines = file.readlines()
        self.lower_green[0] = int(lines[0])
        self.lower_green[1] = int(lines[1])
        self.lower_green[2] = int(lines[2])
        self.upper_green[0] = int(lines[3])
        self.upper_green[1] = int(lines[4])
        self.upper_green[2] = int(lines[5])
        self.lower_blue[0] = int(lines[6])
        self.lower_blue[1] = int(lines[7])
        self.lower_blue[2] = int(lines[8])
        self.upper_blue[0] = int(lines[9])
        self.upper_blue[1] = int(lines[10])
        self.upper_blue[2] = int(lines[11])
        
        self.slider1.setValue(self.lower_green[0])
        self.slider2.setValue(self.lower_green[1])
        self.slider3.setValue(self.lower_green[2])
        self.slider4.setValue(self.upper_green[0])
        self.slider5.setValue(self.upper_green[1])
        self.slider6.setValue(self.upper_green[2])
        self.slider7.setValue(self.lower_blue[0])
        self.slider8.setValue(self.lower_blue[1])
        self.slider9.setValue(self.lower_blue[2])
        self.slider10.setValue(self.upper_blue[0])
        self.slider11.setValue(self.upper_blue[1])
        self.slider12.setValue(self.upper_blue[2])
        self.hide()
        self.show()
            
                
if __name__ == '__main__':
    app = QApplication(sys.argv)

    
        
    # create and show mainWindow
    mainWindow = MainWindow()
    mainWindow.show()
    

    #Handle restoring user settings
    settings_file = pathlib.Path("settings.txt")
    settings_default_file = pathlib.Path("settingsdefault.txt")
    mainWindow.save_settings_default()
        
        
    try:
        mainWindow.restore_settings()
        mainWindow.update_messages("Color Settings Restored. \n")
    except:
        mainWindow.update_messages("No Color Settings Found. Generating From Default Profile. \n")
        mainWindow.save_settings()

        
        
    mainWindow.controlTimer()
    mainWindow.check_exit_status()
    mainWindow.capture_data_timer()

    sys.exit(app.exec_())


