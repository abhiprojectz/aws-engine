import subprocess
import re
from time import sleep

def new_tab():
  subprocess.run("xdotool key ctrl+t", shell=True)


def open_dev_tools():
  subprocess.run("xdotool key ctrl+shift i", shell=True)


def click_one(x,y):
  x__ = x 
  y__ = y 
  window = subprocess.check_output("xdotool getmouselocation", shell=True)
  wind__ = int(re.search(r'\d+', str(window).split(" ")[-1].strip()).group())
  subprocess.run(f"xdotool mousemove --window {wind__} {x__} {y__} click 1", shell=True)
  # subprocess.run("scrot", shell=True)


def click_two(x,y):
  x__ = x
  y__ = y
  window = subprocess.check_output("xdotool getmouselocation", shell=True)
  wind__ = int(re.search(r'\d+', str(window).split(" ")[-1].strip()).group())
  subprocess.run(f"xdotool mousemove --window {wind__} {x__} {y__} click 2", shell=True)


def scrot_():
  subprocess.run("scrot", cwd="/home/circleci/project/ss/", shell=True)


def close_dev_tool():
  click_one(1518, 84)


def search(xx):
  click_one(600 ,55)
  subprocess.run(f"xdotool type {xx}", shell=True)
  subprocess.run("xdotool key KP_Enter", shell=True)


def text_type(x):
  subprocess.run(f'xdotool type "{x}"', shell=True)

def get_cookies():
  # search("https://raw.githubusercontent.com/abhiprojectz/ytdeb/master/lorem.json")
  search("https://raw.githubusercontent.com/abhiprojectz/ytdeb/master/yp.json")
  sleep(5)
  subprocess.run("xdotool key ctrl+a", shell=True)
  subprocess.run("xdotool key ctrl+c", shell=True)
  sleep(2)
  search("https://youtube.com")