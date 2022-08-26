from aws_studio import * 
from start_chrome import start
import random
from time import sleep
import subprocess
from xdotool_commands import * 
import subprocess
import os
from titles_db_dx import titles 
import argparse
from argparse import ArgumentError
from .datax import yt_engine
import requests 


platform_path = "/home/circleci/project/"
# Colab
# platform_path = "/content/"


_path = f"{platform_path}outputs/stack_res.mp4"
_time_30s = 100    # FOR 30 SLIDES
_time_50s = 165    # FOR 30 SLIDES
_time_70s = 233    # FOR 30 SLIDES
_time_10s = 32    # FOR 30 SLIDES
_time_ppt = _time_30s



def get_arg_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser()

    parser.add_argument(
        "-l",
        "--acc",
        dest="acc",
        type=str,
        required=True,
    )
    parser.add_argument(
        "-z",
        "--slot",
        dest="slot",
        type=str,
        required=True,
    ) 
    
    parser.add_argument(
        "-y",
        "--target_url",
        dest="target_url",
        type=str,
        required=True,
    ) 

    parser.add_argument(
        "-a",
        "--type_content",
        dest="type_content",
        type=str,
        required=True,
    ) 
    parser.add_argument(
        "-m",
        "--key",
        dest="key",
        type=str,
        required=True,
    )
    return parser

def setup_chrome_acc(_acc, _lor):
    # _lor = os.environ["target_url"]
    _target = f"{_lor}{_acc}.zip" 

    subprocess.run(f"sudo wget --directory-prefix={platform_path} {_target}", shell=True)
    sleep(2)
    subprocess.run(f"unzip -q {platform_path}chrome_data_{_acc}.zip -d {platform_path}", shell=True)
    sleep(2)

    # initial start
    start()
    sleep(10)
    subprocess.run(f"sudo killall chrome", shell=True)
    sleep(3)

    subprocess.run("sudo rm -r /root/.config/google-chrome/Default", shell=True)
    sleep(3)
    subprocess.run(f"sudo mv {platform_path}root/.config/google-chrome/Default /root/.config/google-chrome/", shell=True)
    sleep(3)


heads = {
    "accept": "application/json",
    "accept-language": "en-US,en;q=0.9",
    "sec-ch-ua": "\"Chromium\";v=\"104\", \" Not A;Brand\";v=\"99\", \"Google Chrome\";v=\"104\"",
    "sec-ch-ua-mobile": "?0",
    "sec-ch-ua-platform": "\"Windows\"",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site"
  }

# "https://api.ranker.com/lists/1036420/items?limit=30"



def get_fact_num():
  _url_info = "https://api.countapi.xyz/info/qoute_db/num"
  _url_hit = "https://api.countapi.xyz/hit/qoute_db/num"

  heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

  r = requests.get(_url_info,headers=heads)
  r_raw = r.json()
  return r_raw['value']

def update_fact_num():
  _url_info = "https://api.countapi.xyz/info/qoute_db/num"
  _url_hit = "https://api.countapi.xyz/hit/qoute_db/num"

  heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
      'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
      'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
      'Accept-Encoding': 'none',
      'Accept-Language': 'en-US,en;q=0.8',
      'Connection': 'keep-alive'}

  r = requests.get(_url_hit,headers=heads)
  r_raw = r.json()
  return r_raw['value']


def upload():
    parser = get_arg_parser()
    args = parser.parse_args()

    _acc = args.acc
    _slot = args.slot
    _type_content = args.type_content
    _lor = args.target_url

    # setting up chrome data folder
    setup_chrome_acc(_acc, _lor)
    # subprocess.run("sudo rm /root/*.mp4", shell=True)
    if _slot == "day":
        ss = ["01:00", "03:00", "06:00", "09:00", "07:00", "08:00"]
        # ss = ["05:00", "07:00"]
        # ss = ["05:00"]
    else: 
        ss = ["13:00", "15:00", "18:00", "21:00", "19:00", "20:00"]

    __id = titles[int(get_fact_num()) -4][1]
    _url = f"https://api.ranker.com/lists/{__id}/items?limit=30" 
    r = requests.get(_url, headers=heads)
    res = r.json()
    # LISTS TO STORE DATA

    # RANKER: SEARCH listID
    _names = []
    _urls = []
    for i in range(len(res['listItems'])):
        _name = res["listItems"][i]["name"]
        _img = res["listItems"][i]["image"]["url"]
        _names.append(_name)
        _urls.append(_img)

    # Generate content 
    for i in ss:
        yt_engine(_names, _urls, _time_ppt, _path)
        sleep(5)

    # Starting chrome...
    start()

    sleep(5)
    # scrot_()
    close_all_popups()
    make_chrome_default()
    # scrot_()
    
    for i in ss:
        print(f"Uploading {ss.index(i) + 1} of shorts...")
        
        tss = titles[int(get_fact_num()) -4][0]
        _title = tss + " #datamatic #trending"

        _time = i
        _date = None
        _item = ss.index(i)

        studio_main(_title, _time, _date, _item)
        sleep(10)
     
def main():
    # subprocess.run("sudo su -", shell=True)
    # Uploading short
    upload()

    # Updating the slot
    print("Process completed.")
    # update_fact_num()


if __name__ == "__main__":
    main()