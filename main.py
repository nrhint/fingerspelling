##Nathan Hinton
##Main program for the fingerspelling trining

import tkinter as tk
from time import time, sleep
from random import choice

v = False
if v:print('loading dictionary...')
from data.Dictionary import Dictionary

d = Dictionary('filteredDictionary.txt', v)
score_int = 0

if v:print('loading the window...')

#Start the window
window = tk.Tk()
window.geometry("300x300")
speed_var = tk.IntVar()
word_input = tk.StringVar()

#window.wm_attributes()
hello_frame = tk.Frame(master = window)
image_frame = tk.Frame(master = window)
input_frame = tk.Frame(master = window)
score_frame = tk.Frame(master = window)
adjustment_frame = tk.Frame(master = window)
other = tk.Frame(master = window)

hello_frame.pack()
image_frame.pack()
input_frame.pack()
score_frame.pack()
adjustment_frame.pack()
other.pack()

##Data that is tracked: {word:[attempts, start_time, end_time]}
dataTracking = {}

def checkWordWorkaround(null):
    checkWord(word)

def checkWord(word):
    global score_int
    global dataTracking
    text = word_input.get()
    word_input.set('')
    if v:print(word, text)
    tmp_data = dataTracking[word]
    tmp_data[0] += 1
    if text == word:
        tmp_data[1].append(time())
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
    speed = int(speed_var.get())
    print(speed)

def printStats():
    print(dataTracking)

def saveStats():
    from pickle import dump
    name = input('enter your name: ')
    dump(dataTracking, open('%s.sta'%name, 'wb'))

def loadStats():
    from pickle import load
    name = input('enter your name: ')
    try:
        load(open('%s.sta'%name, 'rb'))
    except FileNotFoundError:
        print('Profile file not found. Not loading data...')

if v:print('Loading the images...')
from data.images import *

if v:print('finishing up...')

display_image = tk.Label(master = image_frame, image = F1render)

def play_word(word):
    startTime = time()
    interval = 60/speed
    index = 0
    lastLetter = ''
    letter = word[index]
    while index < len(word):
        if time() >= startTime+interval*(index+1):
            index += 1
            lastLetter = letter
            if index == len(word):
                break
            letter = word[index]
            if v:print(lastLetter, letter)
        else:
            if lastLetter == letter:
                double = True
            else:
                double = False
            if letter == 'a':
                if double:
                    display_image.configure(image = A12render)
                    display_image.image = A12render
                else:
                    display_image.configure(image = A1render)
                    display_image.image = A1render
                window.update()
            elif letter == 'b':
                if double:
                    display_image.configure(image = B12render)
                    display_image.image = B12render
                else:
                    display_image.configure(image = B1render)
                    display_image.image = B1render
                window.update()
            elif letter == 'c':
                if double:
                    display_image.configure(image = C12render)
                    display_image.image = C12render
                else:
                    display_image.configure(image = C1render)
                    display_image.image = C1render
                window.update()
            elif letter == 'd':
                if double:
                    display_image.configure(image = D12render)
                    display_image.image = D12render
                else:
                    display_image.configure(image = D1render)
                    display_image.image =D1render
                window.update()
            elif letter == 'e':
                if double:
                    display_image.configure(image = E12render)
                    display_image.image = E12render
                else:
                    display_image.configure(image = E1render)
                    display_image.image = E1render
                window.update()
            elif letter == 'f':
                if double:
                    display_image.configure(image = F12render)
                    display_image.image = F12render
                else:
                    display_image.configure(image = F1render)
                    display_image.image = F1render
                window.update()
            elif letter == 'g':
                if double:
                    display_image.configure(image = G12render)
                    display_image.image = G12render
                else:
                    display_image.configure(image = G1render)
                    display_image.image = G1render
                window.update()
            elif letter == 'h':
                if double:
                    display_image.configure(image = H12render)
                    display_image.image = H12render
                else:
                    display_image.configure(image = H1render)
                    display_image.image = H1render
                window.update()
            elif letter == 'i':
                if double:
                    display_image.configure(image = I12render)
                    display_image.image = I12render
                else:
                    display_image.configure(image = I1render)
                    display_image.image = I1render
                window.update()
            elif letter == 'j':
                if double:
                    display_image.configure(image = J12render)
                    display_image.image = J12render
                else:
                    display_image.configure(image = J1render)
                    display_image.image = J1render
                window.update()
            elif letter == 'k':
                if double:
                    display_image.configure(image = K12render)
                    display_image.image = K12render
                else:
                    display_image.configure(image = K1render)
                    display_image.image = K1render
                window.update()
            elif letter == 'l':
                if double:
                    display_image.configure(image = L12render)
                    display_image.image = L12render
                else:
                    display_image.configure(image = L1render)
                    display_image.image = L1render
                window.update()
            elif letter == 'm':
                if double:
                    display_image.configure(image = M12render)
                    display_image.image = M12render
                else:
                    display_image.configure(image = M1render)
                    display_image.image = M1render
                window.update()
            elif letter == 'n':
                if double:
                    display_image.configure(image = N12render)
                    display_image.image = N12render
                else:
                    display_image.configure(image = N1render)
                    display_image.image = N1render
                window.update()
            elif letter == 'o':
                if double:
                    display_image.configure(image = O12render)
                    display_image.image = O12render
                else:
                    display_image.configure(image = O1render)
                    display_image.image = O1render
                window.update()
            elif letter == 'p':
                if double:
                    display_image.configure(image = P12render)
                    display_image.image = P12render
                else:
                    display_image.configure(image = P1render)
                    display_image.image = P1render
                window.update()
            elif letter == 'q':
                if double:
                    display_image.configure(image = Q12render)
                    display_image.image = Q12render
                else:
                    display_image.configure(image = Q1render)
                    display_image.image = Q1render
                window.update()
            elif letter == 'r':
                if double:
                    display_image.configure(image = R12render)
                    display_image.image = R12render
                else:
                    display_image.configure(image = R1render)
                    display_image.image = R1render
                window.update()
            elif letter == 's':
                if double:
                    display_image.configure(image = S12render)
                    display_image.image = S12render
                else:
                    display_image.configure(image = S1render)
                    display_image.image = S1render
                window.update()
            elif letter == 't':
                if double:
                    display_image.configure(image = T12render)
                    display_image.image = T12render
                else:
                    display_image.configure(image = T1render)
                    display_image.image = T1render
                window.update()
            elif letter == 'u':
                if double:
                    display_image.configure(image = U12render)
                    display_image.image = U12render
                else:
                    display_image.configure(image = U1render)
                    display_image.image = U1render
                window.update()
            elif letter == 'v':
                if double:
                    display_image.configure(image = V12render)
                    display_image.image = V12render
                else:
                    display_image.configure(image = V1render)
                    display_image.image = V1render
                window.update()
            elif letter == 'w':
                if double:
                    display_image.configure(image = W12render)
                    display_image.image = W12render
                else:
                    display_image.configure(image = W1render)
                    display_image.image = W1render
                window.update()
            elif letter == 'x':
                if double:
                    display_image.configure(image = X12render)
                    display_image.image = X12render
                else:
                    display_image.configure(image = X1render)
                    display_image.image = X1render
                window.update()
            elif letter == 'y':
                if double:
                    display_image.configure(image = Y12render)
                    display_image.image = Y12render
                else:
                    display_image.configure(image = Y1render)
                    display_image.image = Y1render
                window.update()
            elif letter == 'z':
                if double:
                    display_image.configure(image = Z12render)
                    display_image.image = Z12render
                else:
                    display_image.configure(image = Z1render)
                    display_image.image = Z1render
                window.update()
            else:
                print("!!!ERROR!!!")
    display_image.configure(image = blankRender)
    display_image.image = blankRender

hello = tk.Label(master = hello_frame, text = 'Welcome to fingerspelling training!')
check_word = tk.Button(master = input_frame, text = 'check', command = lambda: checkWord(word))
replay_word = tk.Button(master = image_frame, text = 'play', command = lambda: play_word(word))
entry = tk.Entry(master = input_frame, textvariable = word_input, fg="yellow", bg="blue", width=15)
score = tk.Label(master = score_frame, text = 'Score: %s'%score_int)
speed_setting = tk.Entry(master = adjustment_frame, textvariable = speed_var, fg = 'yellow', bg = 'blue', width = 5)
apply_settings = tk.Button(master = adjustment_frame, text = 'Apply Settings', command = applySettings)
see_stuff = tk.Button(master = other, text = 'Stats', command = printStats)
save_data = tk.Button(master = other, text = 'Save stats to file', command = saveStats)
load_data = tk.Button(master = other, text = 'Load stats from file', command = loadStats)

hello.pack()
display_image.pack()
replay_word.pack()
entry.pack(side = tk.LEFT)
check_word.pack(side = tk.RIGHT)
score.pack()
speed_setting.pack(side = tk.LEFT)
apply_settings.pack(side = tk.RIGHT)
see_stuff.pack(side = tk.LEFT)
save_data.pack(side = tk.LEFT)
load_data.pack(side = tk.LEFT)

word = ''
def generateNewWord():
    global word
    global dataTracking
    word = choice(d.words)
    dataTracking.update({word:[0, [time()]]})
    play_word(word)

speed = 180#int(input('speed: '))#Speed will be measured in chars per min


generateNewWord()
#print('Secret word: %s'%word)

if v:print('starting!')

window.bind("<Return>", checkWordWorkaround)
window.bind('<space>', play_word)
window.mainloop()
