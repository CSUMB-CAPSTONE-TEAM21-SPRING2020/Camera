# Camera

Setting up the RaspberryPi

1. Installing Raspbian Operating System
    - Download the OS Image
       - https://www.raspberrypi.org/downloads/raspbian/
    - Download the Image burner
       - https://www.balena.io/etcher/
    - Unzip the image file and burn to SD card using Balena Etcher
  
2. RaspberryPi Configurations
    - Initial setup will require a mouse & keyboard
    - Finish setup wizard including updates
    - Start Menu -> Preferences -> RaspberryPi Configuration -> Interfaces
        - Enable Camera 
        - Enable SSH 
        - Enable VNC 
    - Launch & Set up account with VNC Viewer
        - Allows you to control the Device without a screen later if needed


3. Install dependencies
    - Main dependencies
        - sudo apt-get update && sudo apt-get upgrade
        - python3 -m pip install --user --upgrade pip
    - Create a Virtual Environment
        - python3 -m venv env
    - Activate Virtual Environment
        - source env/bin/activate
    - Dependencies for inside Virtual Environment
        - sudo apt-get update && sudo apt-get upgrade
        - sudo apt-get install build-essential cmake pkg-config
        - sudo apt-get install libjpeg-dev libtiff5-dev libjasper-dev libpng-dev
        - sudo apt-get install libavcodec-dev libavformat-dev libswscale-dev libv4l-dev
        - sudo apt-get install libxvidcore-dev libx264-dev
        - sudo apt-get install libfontconfig1-dev libcairo2-dev
        - sudo apt-get install libgdk-pixbuf2.0-dev libpango1.0-dev
        - sudo apt-get install libgtk2.0-dev libgtk-3-dev
        - sudo apt-get install libatlas-base-dev gfortran
        - sudo apt-get install libhdf5-dev libhdf5-serial-dev libhdf5-103
        - sudo apt-get install libqtgui4 libqtwebkit4 libqt4-test python3-pyqt5
        - sudo apt-get install python3-dev
        - pip install opencv-contrib-python==4.1.0.25



4. Running Program
    - cd PATHTOFILE
    - python3 camera.py

