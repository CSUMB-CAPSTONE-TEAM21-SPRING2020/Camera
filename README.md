# Camera

Setting up the RaspberryPi

Installing Raspbian Operating System
•    Download the OS Image
    o    https://www.raspberrypi.org/downloads/raspbian/
•    Download the Image burner
    o    https://www.balena.io/etcher/
•    Unzip the image file and burn to SD card using Balena Etcher


RaspberryPi Configurations
•    Initial setup will require a mouse & keyboard
•    Finish setup wizard including updates
•    Start Menu -> Preferences -> RaspberryPi Configuration -> Interfaces
    o    Enable Camera 
    o    Enable SSH 
    o    Enable VNC 
•    Launch & Set up account with VNC Viewer
    o    Allows you to control the Device without a screen later if needed


Install dependencies
•    Main dependencies
    o    sudo apt-get update && sudo apt-get upgrade
    o    python3 -m pip install --user --upgrade pip
    
•    Create a Virtual Environment
    o    python3 -m venv env

•    Activate Virtual Environment
    o    source env/bin/activate

•    Dependencies for inside Virtual Environment
    o    sudo apt-get update && sudo apt-get upgrade
    o    sudo apt-get install build-essential cmake pkg-config
    o    sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
    o    sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
    o    sudo apt-get install libxvidcore-dev libx264-dev
    o    sudo apt-get install libfontconfig1-dev libcairo2-dev
    o    sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
    o    sudo apt-get install libgtk2.0-dev libgtk-3-dev
    o    sudo apt-get install libatlas-base-dev gfortran
    o    sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
    o    sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
    o    sudo apt-get install python3-dev
    o    pip install opencv-contrib-python==4.1.0.25



Running Program
•    cd PATHTOFILE
•    python3 camera.py

