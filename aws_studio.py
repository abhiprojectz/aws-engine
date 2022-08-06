# AWS STUDIO SCRIPT

from xdotool_commands import * 


def close_all_popups():
  ## Closing all popups
  print("Closing all popusps....")
  click_one(1511, 88) 
  sleep(2)
  click_one(1511, 133)
  sleep(2)
  click_one(1515, 130)
  sleep(2)
  click_one(1515, 83)
  sleep(3)


def make_chrome_default():
  ## Making it default 
  print("Making browser default")
  new_tab()
  sleep(2)
  search("chrome://settings/defaultBrowser")
  sleep(3)
  click_one(1000, 235)
  sleep(3)
  click_one(30, 10)
  sleep(3)


def set_up_youtube():
  ## add to chrome
  print("Adding extension to chrome...")
  click_one(1180, 236)
  sleep(3)

  ## add extension 
  click_one(896, 215)
  sleep(8)

  ## close x
  click_one(1412 , 78)
  sleep(3)

  ## open extension icon
  click_one(1416, 49)
  sleep(3)

  ## pin it
  click_one(1353, 195)
  sleep(3)
  print("Getting cookies...")

  get_cookies()
  sleep(5)

  ## open extension
  print("Opening extension...")
  click_one(1385, 52)
  sleep(3)

  ## click on import icon 
  print("Importing cookies...")
  click_one(1237, 340)
  sleep(3)

  ## paste json
  click_one(1111, 240)
  subprocess.run("xdotool key ctrl+v", shell=True)
  sleep(5)

  ## click ok
  click_one(1300, 517)
  sleep(2)
  ## reload
  print("Reloading the page...")
  subprocess.run("xdotool key ctrl+r", shell=True)
  sleep(5)
  print("Youtube setup!")
  scrot_()


def set_up_upload(_item):
  # # Click on upload icon
  # click_one(1417,164 )
  # sleep(4)

  # close popusps 1
  click_one(1320 , 102) 
  sleep(3)
  # scrot_()
  # close popusps 2
  click_one(1481, 91)
  sleep(3)
  # scrot_()
  #create 
  click_one(1402, 98) 
  sleep(3)
  # scrot_()
  #upload vedio
  click_one(1384, 136)
  sleep(4)
  # scrot_()

  # select files
  click_one(765, 575)
  sleep(4)

  ## open home
  click_one(20, 60)
  sleep(4)

  if _item == 0:
    click_one(233, 90) #1
  elif _item == 1:
    click_one(233, 115) #2
  elif _item == 2:
    click_one(233, 126) #3
  elif _item == 3:
    click_one(233, 153) #4

  sleep(4)


  ## open btn
  click_one(1100, 800)
  sleep(4)


def set_title(res):
  ## tile
  text_type(str(res))
  sleep(3)

  ## next 
  click_one(1200, 775)
  sleep(3)

  # next screen 2 
  click_one(1200, 775)
  sleep(3)

  # next screen 3
  click_one(1200, 775)
  sleep(3)

  # schedule btn
  click_one(366, 704)
  sleep(3)


def set_date(res):
  ## For date
  click_one(468, 532)
  sleep(3)
  subprocess.run("xdotool key ctrl+a", shell=True)
  subprocess.run("xdotool key BackSpace", shell=True)
  sleep(3)

  # Date format: 19 JUl 2022
  text_type(str(res))
  click_one(745, 535)


def set_time(res):
  # select time
  click_one(625, 535)
  subprocess.run("xdotool key ctrl+a", shell=True)
  subprocess.run("xdotool key BackSpace", shell=True)

  ## type time Format: "06:00"
  text_type(str(res))
  sleep(4)
  click_one(745, 535)
  sleep(5)


def schedule():
  # SCHEDULE FINAL
  click_one(1200, 775)

def open_studio():
    search("https://studio.youtube.com/")
    sleep(10)
    print("Studio startup...")


def studio_main(_title, _time, _date, _item):
  # Open studio
  open_studio()
  # scrot_()

  ## Time & date
  if not _title:
    _title = "Lorem ipsum..."

  if not _time: 
    _time = "06:00"
  
#   if not _date:
#     _date = "23 Jul 2022"

  set_up_upload(_item)
  # scrot_()
  print("Setting up title...")
  set_title(_title)
  # scrot_()

  # if _date:
  #   set_date(_date)

  print("Setting up time..")
  set_time(_time)

  print("Waiting for processing....")
  sleep(25)
  # scrot_()
  schedule()
  print("Short successfully uploaded.")
  sleep(30)
  # scrot_()
  



# studio_main()

