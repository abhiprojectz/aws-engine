from aws_studio import * 
from start_chrome import start
import random
from time import sleep
from ytdeb.main import yt_engine
import subprocess
from xdotool_commands import * 
import subprocess
import os
import argparse
from argparse import ArgumentError

def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--acc",
        dest="acc",
        type=str,
        help="A json file that contains the cookies required to sign into YouTube in the target browser.",
        required=True,
    )
    parser.add_argument(
        "-z",
        "--slot",
        dest="slot",
        type=str,
        help="A json file that contains the cookies required to sign into YouTube in the target browser.",
        required=True,
    )
    return parser


def set_slot():
    with open("/home/circleci/project/res.txt", 'r') as f:
        text = f.read()


    _slot = text

    _valid_slots = ["day_A", "night_A", "day_B","night_B", "day_C", "night_C"]

    if _valid_slots.index(_slot) == len(_valid_slots) -1:
        _slot = "day_A"
    else:
        _slot = _valid_slots[_valid_slots.index(_slot) + 1]


    _format = f"{_slot}"
    with open("/home/circleci/project/res.txt", 'w') as f:
        f.write(_format)


def setup_chrome_acc(_acc):
    _target = f"https://github.com/abhiprojectz/ytdeb/releases/download/v1/chrome_data_{_acc}.zip" 

    subprocess.run(f"sudo wget --directory-prefix=/home/circleci/project/ {_target}", shell=True)
    sleep(2)
    subprocess.run(f"unzip -q /home/circleci/project/chrome_data_{_acc}.zip -d /home/circleci/project/", shell=True)
    sleep(2)

    # initial start
    start()
    sleep(10)
    subprocess.run("sudo killall chrome", shell=True)
    sleep(3)

    subprocess.run("sudo rm -r /root/.config/google-chrome/Default", shell=True)
    sleep(3)
    subprocess.run("sudo mv /home/circleci/project/root/.config/google-chrome/Default /root/.config/google-chrome/", shell=True)
    sleep(3)


def upload():
    ts = ["#shorts #motivation #fun #meme #jee #knowledge #upsc #satisfying #amazing",
    "#satisfying #amazing #ias #ips #pcs #jee #knowledge #upsc #neet",
    "Subscribe & like #ias #ips #motivation #shorts #jee #knowledge #upsc #satisfying #amazing",
    "#knowledge #motivation #shorts #ias #ips #pcs #jee #knowledge #upsc",
    "#motivational #satisfying #amazing #motivation #shorts #ias #ips #pcs #jee #knowledge #upsc",
    "#shorts #motivation #knowledge #ias #ips #pcs #knowledge #upsc #satisfying #amazing",
    "Most motivational #shorts ever #motivation #iit #jee #ias #ips #pcs #upsc #satisfying #amazing",
    "#motivational #memes #shorts #ias #ips #funny #jee #knowledge #upsc #satisfying #amazing",
    "#inspiring #motivation #shorts #ias #ips #pcs #jee #knowledge #upsc #satisfying #amazing",
    "Please subscribe the channel #motivation #shorts #ias #knowledge #upsc #satisfying #amazing",
    "Don't for get to subscribe #motivational #motivation #ias #ips #pcs #shorts",
    "Most inspirational shorts ever #shorts #motivation",
    "Help us reach 1000 subscribers #motivational #ias #ips #pcs #shorts"
    ]

    parser = get_arg_parser()
    args = parser.parse_args()

    _acc = args.acc
    _slot = args.slot

    # # Setup right slot 
    # with open("/home/circleci/project/res.txt", 'r') as f:
    #     _slot = f.read()
    # _slot_time = _slot.split("_")[0]
    # _acc = _slot.split("_")[1]


    # setting up chrome data folder
    setup_chrome_acc(_acc)

    # subprocess.run("sudo rm /root/*.mp4", shell=True)


    if _slot == "day":
        # ss = ["01:00", "03:00", "06:00", "09:00"]
        ss = ["05:00"]
    else: 
        ss = ["13:00", "15:00", "18:00", "21:00"]


    # Generate content 
    for i in ss:
        yt_engine()
        sleep(10)


    # Starting chrome...
    start()

    sleep(5)
    # scrot_()
    close_all_popups()
    make_chrome_default()
    # scrot_()
    
    for i in ss:
        tss = random.choice(ts) 
        _title = tss

        _time = i
        _date = None
        _item = ss.index(i)

        # Starting studio...
        print("Running studio script...")
        studio_main(_title, _time, _date, _item)
        sleep(10)

     
def main():
    # subprocess.run("sudo su -", shell=True)
    # Uploading short
    upload()


    # Updating the slot
    print("Process completed.")



if __name__ == "__main__":
    main()