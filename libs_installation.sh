#!/bin/bash 

sudo apt-get install scrot
sudo apt-get install xvfb xorg xserver-xorg scrot imagemagick x11-utils
sudo apt install xdotool

wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
sudo apt install ./google-chrome-stable_current_amd64.deb 

wget https://github.com/abhiprojectz/ytdeb/releases/download/v1/chrome_data.zip 