##Nathan Hinton
##Main program for the fingerspelling trining !!!DO NOT ADD UNTIL THE SAFE MARKER!!!

import tkinter as tk
from time import time, sleep
from random import choice
import threading
from util.addImageset import generateNewImages
from util import updateManager

v = True
if v:print('loading the window...')

#Start the window
window = tk.Tk()
window.geometry("500x650")
speed_var = tk.IntVar()
word_input = tk.StringVar()
word_length_var = tk.IntVar()

from data.defaultImages import *

if v:print('checking for cache files...')
gen = True
x = 0
while gen:
    x += 1
    try:
        open('imageSet%s.pk'%(x+1), 'r')
        open('./data/images%s.py'%(x+1), 'r')
    except FileNotFoundError:
        check = generateNewImages(x+1)
        if check == 'Fail':
            gen = False
            if v:print('found %s sets of images...'%x)
        else:
            print('generated %s'%(x+1))

from data.images4 import *
from data.images3 import *
from data.images2 import *
from data.images1 import *

from util.playWord import play_word


##########SAFE#######################
if v:print('loading dictionary...')
from data.Dictionary import Dictionary

d = Dictionary('filteredDictionary.txt', v)
score_int = 0

#window.wm_attributes()
hello_frame = tk.Frame(master = window)
image_frame = tk.Frame(master = window)
replay_frame = tk.Frame(master = window)
input_frame = tk.Frame(master = window)
score_frame = tk.Frame(master = window)
adjustment_frame = tk.Frame(master = window)
other = tk.Frame(master = window)

hello_frame.pack()
image_frame.pack()
replay_frame.pack()
input_frame.pack()
score_frame.pack()
adjustment_frame.pack()
other.pack()

##Data that is tracked: {word:[attempts, times_watched, [start_time, end_time], speed]}
dataTracking = {}

def checkWordWorkaround(null):
    checkWord(word)

def play_word_workaround(word):
    global dataTracking
    dataTracking[word][1] += 1
    play_word(word, speed, display_image, window, v)
    # print('starting thread')
    # t = threading.Thread(target=play_word, args=(word, speed, display_image, window, v, ))
    # t.start()

word = ''
def generateNewWord():
    global word
    global dataTracking
    word = choice(d.words)
    if len(word) >= min_length:
        dataTracking.update({word:[0, 0, [time()], 0]})
        dataTracking[word][1] += 1
        play_word_workaround(word)
    else:
        generateNewWord()

def analyze():
    from util import analyze

def checkWord(word):
    global score_int
    global dataTracking
    text = word_input.get()
    if text == '':
        dataTracking[word][1] += 1
        play_word_workaround(word)
    else:
        word_input.set('')
        if v:print(word, text)
        tmp_data = dataTracking[word]
        tmp_data[0] += 1
        tmp_data.append(speed)
        if text == word:
            tmp_data[2].append(time())
            dataTracking.update({word:tmp_data})
            score_int += 1
            score.configure(text = '%s'%score_int)
            score.text = 'Score: %s'%score_int
            display_image.configure(image = smileRender)
            display_image.image = smileRender
            window.update()
            sleep(1)
            display_image.configure(image = blankRender)
            display_image.image = blankRender
            window.update()
            sleep(0.25)
            generateNewWord()
        else:
            score_int -= 1
            score.configure(text = '%s'%score_int)
            score.text = 'Score: %s'%score_int
            window.update()

def applySettings():
    global speed
    global min_length
    speed = int(speed_var.get())
    min_length = int(word_length_var.get())
    print(min_length, speed)

def printStats():
    print(dataTracking)

def saveStats(name = False):
    from pickle import dump
    if not name:
        name = input('enter your name: ')
    tmpData = dataTracking
    tmpData.pop(word)
    dump(tmpData, open('%s.sta'%name, 'wb'))
    print('stats saved!')

def loadStats():
    global dataTracking
    from pickle import load
    name = input('enter your name: ')
    try:
        tmp = load(open('%s.sta'%name, 'rb'))
        dataTracking.update(tmp)
        print('Data loaded!')
    except FileNotFoundError:
        print('Profile file not found. Not loading data...')

display_image = tk.Label(master = image_frame, image = blankRender)

display_image.configure(image = blankRender)
display_image.image = blankRender


hello = tk.Label(master = hello_frame, text = 'Welcome to fingerspelling training!')
check_word = tk.Button(master = input_frame, text = 'check', command = lambda: checkWord(word))
new_word = tk.Button(master = replay_frame, text = 'new word', command = lambda: generateNewWord())
replay_word = tk.Button(master = replay_frame, text = 'play', command = lambda: play_word_workaround(word))
entry = tk.Entry(master = input_frame, textvariable = word_input, fg="yellow", bg="blue", width=15)
score = tk.Label(master = score_frame, text = 'Score: %s'%score_int)
speed_setting = tk.Entry(master = adjustment_frame, textvariable = speed_var, fg = 'yellow', bg = 'blue', width = 5)
length_setting = tk.Entry(master = adjustment_frame, textvariable = word_length_var, fg = 'yellow', bg = 'blue', width = 5)
apply_settings = tk.Button(master = adjustment_frame, text = 'Apply Settings', command = applySettings)
see_stuff = tk.Button(master = other, text = 'Stats', command = printStats)
save_data = tk.Button(master = other, text = 'Save stats to file', command = saveStats)
load_data = tk.Button(master = other, text = 'Load stats from file', command = loadStats)
analyze_data = tk.Button(master = other, text = 'Analyze data', command = analyze)

# if v:print('waiting for images to finish loading...')
# loadImages.join()
if v:print('finishing up...')

hello.pack()
display_image.pack()
new_word.pack(side = tk.LEFT)
replay_word.pack(side = tk.RIGHT)
entry.pack(side = tk.LEFT)
check_word.pack(side = tk.RIGHT)
score.pack()
length_setting.pack(side = tk.LEFT)
speed_setting.pack(side = tk.LEFT)
apply_settings.pack(side = tk.RIGHT)
see_stuff.pack(side = tk.LEFT)
save_data.pack(side = tk.LEFT)
load_data.pack(side = tk.LEFT)
analyze_data.pack(side = tk.LEFT)

speed = 180#int(input('speed: '))#Speed will be measured in chars per min
speed_var.set(180)
min_length = 4
word_length_var.set(3)

if v:print('starting background update check...')
update_thread = threading.Thread(target=updateManager.runUpdateManager)
update_thread.start()

if v:print('starting!')

generateNewWord()
#print('Secret word: %s'%word)

window.bind("<Return>", checkWordWorkaround)
window.bind('<space>', play_word_workaround)
window.mainloop()
