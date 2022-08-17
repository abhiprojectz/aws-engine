from googletrans import Translator
from gtts import gTTS
import random
import string
import requests
import shutil
import os, sys
from datetime import datetime
from PIL import Image
import time
from os.path import exists
from time import sleep
import subprocess 
from moviepy.editor import VideoFileClip, AudioFileClip
from moviepy.audio.fx.all import volumex
from moviepy.editor import *
import textwrap

from .content_db import items
from .mixkit_urls import vids

from .riddle_db import items_riddle
from .pexels_db import pexels_id

# ========= DEFAULTS =========
# __file__ = '/content/djhdd.py'
dir_path = os.path.dirname(os.path.realpath(__file__))
fps = 24
VIDS_NUM_DURATION = 15
VIDS_NUM_DURATION_SHORTS = 8

def id_generator(size=20, chars=string.ascii_uppercase + string.digits):
  return ''.join(random.choice(chars) for _ in range(size))

def translate_text(text):
    # Translator method for translation
    translator = Translator()

    from_lang = 'en'
    to_lang = 'hi'

    text_to_translate = translator.translate(text, src= from_lang, dest= to_lang)
    res = text_to_translate.text
    print(res)
    return res


def generate_speech(text_m):
    # text_m = '''अजय पहले भारतीय YouTuber थे जिन्होंने रोस्टिंग कंटेंट शुरू किया था। बाद में उन्होंने अपने चैनल का नाम बदलकर CarryMinati कर लिया।
    # उनके परिवार ने उनका समर्थन किया जब उन्होंने कहा कि वह अपनी पढ़ाई छोड़ना चाहते हैं और बाद में एक ओपन स्कूल के माध्यम से अपनी पढ़ाई पूरी की।'''

    language = "hi"
    _file = id_generator()

    gtts_object = gTTS(text = text_m, lang = language, slow = False)
    _out = os.path.join(dir_path, _file + ".wav") 
    gtts_object.save(_out)
    return _out

def deleteResized():
    dir = os.path.join(dir_path, "resized")
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

def deletedownloads():
    dir = os.path.join(dir_path, "downloaded")
    for files in os.listdir(dir):
        path = os.path.join(dir, files)
        try:
            shutil.rmtree(path)
        except OSError:
            os.remove(path)

def resizer_shorts(x):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    resized_dir = os.path.join(dir_path, "resized")
    filename = os.path.join(resized_dir, id_generator() + '.mp4') 
    subprocess.run(f'ffmpeg -i {x} -vf "scale=720:1280:force_original_aspect_ratio=decrease,pad=720:1280:-1:-1:color=black" {filename}', shell=True)


def resizer_vid(x):
    dir_path = os.path.dirname(os.path.realpath(__file__))
    resized_dir = os.path.join(dir_path, "resized")
    filename = os.path.join(resized_dir, id_generator() + '.mp4') 
    subprocess.run(f'ffmpeg -i {x} -vf "scale=1280:720:force_original_aspect_ratio=decrease,pad=1280:720:-1:-1:color=black" {filename}', shell=True)
    

# def get_vids_and_resize():
#     files = []
#     _downloads_path = os.path.join(dir_path, "downloaded/")
#     resized_dir = os.path.join(dir_path, "resized")

#     for file in os.listdir(_downloads_path):
#         if file.endswith(".mp4"):
#             # tp = os.path.join(fz, file)
#             tp = _downloads_path + "/" + file
#             resized_new = resizer_vid(tp)
#             # files.append(resized_new)
#             # print(os.path.join(file))

#     # for file in os.listdir(_downloads_path):
#     #     if file.endswith(".mp4"):
#     #         # tp = os.path.join(fz, file)
#     #         tp = resized_dir + "/" + file
#     #         # resized_new = resizer_vid(tp)
#     #         files.append(tp)
#     return files


def get_final_vids():
    files = []
    _downloads_path = os.path.join(dir_path, "resized/")

    for file in os.listdir(_downloads_path):
        if file.endswith(".mp4"):
            # tp = os.path.join(fz, file)
            tp = _downloads_path + "/" + file
            files.append(tp)
            # print(os.path.join(file))
    return files

def get_final_riddle_vids():
    files = []
    _downloads_path = os.path.join(dir_path, "downloaded/")

    for file in os.listdir(_downloads_path):
        if file.endswith(".mp4"):
            # tp = os.path.join(fz, file)
            tp = _downloads_path + "/" + file
            files.append(tp)
            # print(os.path.join(file))
    return files


def downloadVids(x):
    # _vid = ["https://assets.mixkit.co/videos/download/mixkit-northern-lights-of-blue-and-green-colors-in-the-night-4038.mp4"]

    heads = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11',
       'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
       'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
       'Accept-Encoding': 'none',
       'Accept-Language': 'en-US,en;q=0.8',
       'Connection': 'keep-alive'}
    # imgs = ["89994Xinspirational-quote-life-unknown-author-pretty-monarch-butterfly-perched-flower-43678437.jpg", "D3IK1Linspirational-quote-happiness-c-e-jerningham-two-adorable-poodles-enjoying-life-to-fullest-43678289.jpg","SE8AJ8inspirational-phrases-be-positive-believe-yourself-enjoy-life-motivational-notes-papers-48980497.jpg" ]

    dir_path = os.path.dirname(os.path.realpath(__file__))
    downloads_dir = os.path.join(dir_path, "downloaded")

    image_url = x
    filename = id_generator() + ".mp4"
    r = requests.get(image_url,headers=heads, stream = True)
    print(r)
    if r.status_code == 200:
        r.raw.decode_content = True
        with open(filename,'wb') as f:
            shutil.copyfileobj(r.raw, f)

        shutil.move(str(filename), downloads_dir)
        print('Image sucessfully Downloaded: ', id_generator() + filename)
        return downloads_dir + '/' + filename
    else:
        print('Image Couldn\'t be retreived')
        return None


def trim_vid(x):
    _temp_path = os.path.join(dir_path, "temp/")
    clip = VideoFileClip(x)
    clipz = clip.subclip(0, 12) 
    f_name = id_generator() + '.mp4'
    clipz.write_videofile(_temp_path +  f_name)
    return _temp_path +  f_name


def download_riddle(x):
  downloads_dir = os.path.join(dir_path, "downloaded")
  subprocess.call(f"curl -O -J -L {x}", shell=True, cwd=downloads_dir)


def do_download(_audio, is_short, is_riddle, is_motivation):
    f_lens = []

    if is_short:
      for i in range(2):
          j = random.choice(vids)
          raw = f"https://assets.mixkit.co/videos/download/mixkit-{j.split('/')[2]}-medium.mp4"
          x_raw = downloadVids(raw)
          resizer_shorts(x_raw)
    elif is_riddle:
      for i in range(2):
          j = random.choice(pexels_id)
          raw = f"https://www.pexels.com/video/{j}/download/?h=1280&w=720"
          x_raw = download_riddle(raw)

    elif is_motivation:
      for i in range(2):
          j = random.choice(items_riddle)
          raw = f"https://assets.mixkit.co/videos/download/mixkit-{j.split('/')[2]}-medium.mp4"
          x_raw = downloadVids(raw)
          resizer_shorts(x_raw)

    else:
      while True:
        if sum(f_lens) >= _audio:
          break
        else:
          i = random.choice(vids)
          raw = f"https://assets.mixkit.co/videos/download/mixkit-{i.split('/')[2]}-medium.mp4"
          x_raw = downloadVids(raw)
          clip_dur = VideoFileClip(x_raw).duration
          
          if clip_dur <= VIDS_NUM_DURATION:
            # temp_downloaded
            f_lens.append(clip_dur)
            if is_short:
              resizer_shorts(x_raw)
            else:
              resizer_vid(x_raw)
            # f_vids.append(i)
          else:
            x_trim = trim_vid(x_raw)
            if is_short:
              resizer_shorts(x_raw)
            else:
              resizer_vid(x_trim)
            f_lens.append(VIDS_NUM_DURATION)


def download_images(tex):
    _target = os.path.join(dir_path, "downloaded") 
    subprocess.run(f"googleimagesdownload -k '{tex}' -l 6 -o '{_target}'", shell=True)
    sleep(10)


def get_bg_music():
    _bg_m_path = os.path.join(dir_path, "bg_music") 
    files = []
    for file in os.listdir(_bg_m_path):
        if file.endswith(".mp3"):
            files.append(os.path.join(dir_path, "bg_music")  + "/" + file)
    f = random.choice(files)
    return f


def generateVedio(_audio, is_short, is_riddle, is_motivation, _msg):
    _audio_path = _audio
    _bg_music_path = get_bg_music()
    _final_audio_path = os.path.join(dir_path, id_generator() + '.mp3') 
    _subs_path = os.path.join(dir_path, "subs_png.png") 
    _like_subs_path = os.path.join(dir_path, "like_subs.wav") 

    destination_dir = os.path.join(dir_path, "outputs")
    target = os.path.join(destination_dir, f"{id_generator()}.mp4")

    
    voice_audio = AudioFileClip(_audio_path)
    _total_duration = voice_audio.duration + 4


    bg_music = AudioFileClip(_bg_music_path)
    bg_music = bg_music.fx(volumex, 0.3)
    new_bg_music = bg_music.subclip(0, (_total_duration))


    # audioclip = AudioFileClip(music).set_duration(15)
    final_audio = concatenate_audioclips([voice_audio, AudioFileClip(_like_subs_path)])
    final_audio2 = CompositeAudioClip([final_audio, new_bg_music])
    final_audio2.write_audiofile(_final_audio_path, fps=new_bg_music.fps)

    
    # Get resized vids 
    if is_short:
      vids_list = get_final_vids()
    elif is_riddle:
      vids_list = get_final_riddle_vids()
    elif is_motivation:
      vids_list = get_final_riddle_vids()


    if is_short:
      avg_dur = (_total_duration) / len(vids_list)
      clips = [VideoFileClip(m).set_duration(int(avg_dur)).crossfadein(2.0)
              for m in vids_list]
    else:
      clips = [VideoFileClip(m).crossfadein(2.0)
              for m in vids_list]

    audio_clip = AudioFileClip(_final_audio_path)
    concat_clip = concatenate_videoclips(clips, method="compose").set_audio(audio_clip)



    if is_riddle:
      txt1 = TextClip("Comment Your Answer!", font="Amiri", stroke_width=3, stroke_color='black', fontsize = 50, color='white').set_pos(('center', 50)).set_duration(_total_duration) 

      x = textwrap.fill(_msg, 25)
      txt2 = TextClip(x, fontsize = 43, stroke_width=3, stroke_color='black', font='Mangal-bold', color = 'white').set_pos('center').set_duration(_total_duration) 

      txt3 = TextClip("Riddle", stroke_width=10, fontsize = 52, color = 'white').set_pos(('center', 'bottom')).set_duration(_total_duration) 
      overlay_clip = ImageClip(_subs_path) 
      masked_clip = overlay_clip.resize(0.9).set_position(('center', 'top')).set_duration(_total_duration)

      final_video = CompositeVideoClip([concat_clip, txt1, txt2, txt3, masked_clip]) 

    else:
      # Applying green screen subsribe btn
      overlay_clip = ImageClip(_subs_path) 
      # masked_clip = vfx.mask_color(overlay_clip, color=[0,255,0], thr=190, s=5) 
      masked_clip = overlay_clip.set_position(('center', 'top')).set_duration(_total_duration)
      final_video = CompositeVideoClip([concat_clip, masked_clip])


    # concat_clip.write_videofile(target, fps=fps, codec="mpeg4")
    final_video.write_videofile(target, fps=fps, threads = 8, logger=None)
    deleteResized()
    deletedownloads()
    # deleteResized()
    print('Vid successfully generated.')


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

def move_content():    
    # move to /root folder
    subprocess.run("sudo mv /home/circleci/project/ytdeb_content/outputs/*  /root/", shell=True)


def make_vid():
    fact = random.choice(items)
    tex_res = translate_text(fact)
    
    _audio = generate_speech(tex_res)
    _audio_duration = AudioFileClip(_audio).duration
    do_download(_audio_duration, is_short=False, is_riddle=False, is_motivation=False)
    generateVedio(_audio, is_short=False)


def make_content_shorts():
    fact = random.choice(items)
    # tex_res = translate_text(fact)
    
    _audio = generate_speech(fact)
    _audio_duration = AudioFileClip(_audio).duration
    do_download(_audio_duration, is_short=True, is_riddle=False, is_motivation=False)
    generateVedio(_audio, is_short=True, is_riddle=False, is_motivation=False, _msg=None)


def make_content_riddle():
    fact = random.choice(items_riddle)
    x_fact = translate_text(fact)

    _audio = generate_speech(x_fact)
    _audio_duration = AudioFileClip(_audio).duration
    do_download(_audio_duration, is_short=False, is_riddle=True, is_motivation=False)
    generateVedio(_audio, is_short=False, is_riddle=True, is_motivation=False, _msg=x_fact)


def yt_engine(_type_content):
    if _type_content == "shorts":
      make_content_shorts()
      move_content()
      print("Short generated.") 
    else:
      make_content_riddle()
      move_content()
      print("Riddle generated.") 

