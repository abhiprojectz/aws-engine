#!/bin/bash 

# sudo apt install scrot xvfb xorg xserver-xorg scrot imagemagick x11-utils xdotool
sudo chown -R _apt:root /var/lib/apt/lists
sudo wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# sudo apt install ./google-chrome-stable_current_amd64.deb 
sudo dpkg -i ./google-chrome-stable_current_amd64.deb 
