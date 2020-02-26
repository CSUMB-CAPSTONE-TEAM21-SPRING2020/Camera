# Camera

Under Construction

Setting up the RaspberryPi
pip3 install opencv-python

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
    o    Allows you to control the Device without a screen later


python3 -m pip install --user --upgrade pip
python3 -m pip install --user virtualenv
python3 -m venv env
source env/bin/activate
pip install requests
