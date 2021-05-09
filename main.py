##Nathan Hinton
##Main program for the fingerspelling trining !!!DO NOT ADD UNTIL THE SAFE MARKER!!!

import tkinter as tk
from time import time, sleep
from random import choice, randint
from PIL import Image, ImageTk
from util.addImageset import generateNewImages

v = True
if v:print('loading the window...')

#Start the window
window = tk.Tk()
window.geometry("500x650")
speed_var = tk.IntVar()
word_input = tk.StringVar()
word_length_var = tk.IntVar()

from data.defaultImages import *

add = False
if add:
    for x in range(0, 3):
        generateNewImages()


from data.images3 import *
from data.images2 import *
from data.images1 import *




def play_word(word):
    global dataTracking
    dataTracking[word][1] += 1
    startTime = time()
    interval = 60/speed
    index = 0
    lastLetter = ''
    letter = word[index]
    r = randint(1, 2)
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
            if r == 0:
                print("ERROR")
            if r == 1:
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
            elif r == 2:
                if letter == 'a':
                    if double:
                        display_image.configure(image = A22render)
                        display_image.image = A22render
                    else:
                        display_image.configure(image = A2render)
                        display_image.image = A2render
                    window.update()
                elif letter == 'b':
                    if double:
                        display_image.configure(image = B22render)
                        display_image.image = B22render
                    else:
                        display_image.configure(image = B2render)
                        display_image.image = B2render
                    window.update()
                elif letter == 'c':
                    if double:
                        display_image.configure(image = C22render)
                        display_image.image = C22render
                    else:
                        display_image.configure(image = C2render)
                        display_image.image = C2render
                    window.update()
                elif letter == 'd':
                    if double:
                        display_image.configure(image = D22render)
                        display_image.image = D22render
                    else:
                        display_image.configure(image = D2render)
                        display_image.image =D2render
                    window.update()
                elif letter == 'e':
                    if double:
                        display_image.configure(image = E22render)
                        display_image.image = E22render
                    else:
                        display_image.configure(image = E2render)
                        display_image.image = E2render
                    window.update()
                elif letter == 'f':
                    if double:
                        display_image.configure(image = F22render)
                        display_image.image = F22render
                    else:
                        display_image.configure(image = F2render)
                        display_image.image = F2render
                    window.update()
                elif letter == 'g':
                    if double:
                        display_image.configure(image = G22render)
                        display_image.image = G22render
                    else:
                        display_image.configure(image = G2render)
                        display_image.image = G2render
                    window.update()
                elif letter == 'h':
                    if double:
                        display_image.configure(image = H22render)
                        display_image.image = H22render
                    else:
                        display_image.configure(image = H2render)
                        display_image.image = H2render
                    window.update()
                elif letter == 'i':
                    if double:
                        display_image.configure(image = I22render)
                        display_image.image = I22render
                    else:
                        display_image.configure(image = I2render)
                        display_image.image = I2render
                    window.update()
                elif letter == 'j':
                    if double:
                        display_image.configure(image = J22render)
                        display_image.image = J22render
                    else:
                        display_image.configure(image = J2render)
                        display_image.image = J2render
                    window.update()
                elif letter == 'k':
                    if double:
                        display_image.configure(image = K22render)
                        display_image.image = K22render
                    else:
                        display_image.configure(image = K2render)
                        display_image.image = K2render
                    window.update()
                elif letter == 'l':
                    if double:
                        display_image.configure(image = L22render)
                        display_image.image = L22render
                    else:
                        display_image.configure(image = L2render)
                        display_image.image = L2render
                    window.update()
                elif letter == 'm':
                    if double:
                        display_image.configure(image = M22render)
                        display_image.image = M22render
                    else:
                        display_image.configure(image = M2render)
                        display_image.image = M2render
                    window.update()
                elif letter == 'n':
                    if double:
                        display_image.configure(image = N22render)
                        display_image.image = N22render
                    else:
                        display_image.configure(image = N2render)
                        display_image.image = N2render
                    window.update()
                elif letter == 'o':
                    if double:
                        display_image.configure(image = O22render)
                        display_image.image = O22render
                    else:
                        display_image.configure(image = O2render)
                        display_image.image = O2render
                    window.update()
                elif letter == 'p':
                    if double:
                        display_image.configure(image = P22render)
                        display_image.image = P22render
                    else:
                        display_image.configure(image = P2render)
                        display_image.image = P2render
                    window.update()
                elif letter == 'q':
                    if double:
                        display_image.configure(image = Q22render)
                        display_image.image = Q22render
                    else:
                        display_image.configure(image = Q2render)
                        display_image.image = Q2render
                    window.update()
                elif letter == 'r':
                    if double:
                        display_image.configure(image = R22render)
                        display_image.image = R22render
                    else:
                        display_image.configure(image = R2render)
                        display_image.image = R2render
                    window.update()
                elif letter == 's':
                    if double:
                        display_image.configure(image = S22render)
                        display_image.image = S22render
                    else:
                        display_image.configure(image = S2render)
                        display_image.image = S2render
                    window.update()
                elif letter == 't':
                    if double:
                        display_image.configure(image = T22render)
                        display_image.image = T22render
                    else:
                        display_image.configure(image = T2render)
                        display_image.image = T2render
                    window.update()
                elif letter == 'u':
                    if double:
                        display_image.configure(image = U22render)
                        display_image.image = U22render
                    else:
                        display_image.configure(image = U2render)
                        display_image.image = U2render
                    window.update()
                elif letter == 'v':
                    if double:
                        display_image.configure(image = V22render)
                        display_image.image = V22render
                    else:
                        display_image.configure(image = V2render)
                        display_image.image = V2render
                    window.update()
                elif letter == 'w':
                    if double:
                        display_image.configure(image = W22render)
                        display_image.image = W22render
                    else:
                        display_image.configure(image = W2render)
                        display_image.image = W2render
                    window.update()
                elif letter == 'x':
                    if double:
                        display_image.configure(image = X22render)
                        display_image.image = X22render
                    else:
                        display_image.configure(image = X2render)
                        display_image.image = X2render
                    window.update()
                elif letter == 'y':
                    if double:
                        display_image.configure(image = Y22render)
                        display_image.image = Y22render
                    else:
                        display_image.configure(image = Y2render)
                        display_image.image = Y2render
                    window.update()
                elif letter == 'z':
                    if double:
                        display_image.configure(image = Z22render)
                        display_image.image = Z22render
                    else:
                        display_image.configure(image = Z2render)
                        display_image.image = Z2render
                    window.update()
                else:
                    print("!!!ERROR!!!")
            elif r == 3:
                if letter == 'a':
                    if double:
                        display_image.configure(image = A32render)
                        display_image.image = A32render
                    else:
                        display_image.configure(image = A3render)
                        display_image.image = A3render
                    window.update()
                elif letter == 'b':
                    if double:
                        display_image.configure(image = B32render)
                        display_image.image = B32render
                    else:
                        display_image.configure(image = B3render)
                        display_image.image = B3render
                    window.update()
                elif letter == 'c':
                    if double:
                        display_image.configure(image = C32render)
                        display_image.image = C32render
                    else:
                        display_image.configure(image = C3render)
                        display_image.image = C3render
                    window.update()
                elif letter == 'd':
                    if double:
                        display_image.configure(image = D32render)
                        display_image.image = D32render
                    else:
                        display_image.configure(image = D3render)
                        display_image.image =D3render
                    window.update()
                elif letter == 'e':
                    if double:
                        display_image.configure(image = E32render)
                        display_image.image = E32render
                    else:
                        display_image.configure(image = E3render)
                        display_image.image = E3render
                    window.update()
                elif letter == 'f':
                    if double:
                        display_image.configure(image = F32render)
                        display_image.image = F32render
                    else:
                        display_image.configure(image = F3render)
                        display_image.image = F3render
                    window.update()
                elif letter == 'g':
                    if double:
                        display_image.configure(image = G32render)
                        display_image.image = G32render
                    else:
                        display_image.configure(image = G3render)
                        display_image.image = G3render
                    window.update()
                elif letter == 'h':
                    if double:
                        display_image.configure(image = H32render)
                        display_image.image = H32render
                    else:
                        display_image.configure(image = H3render)
                        display_image.image = H3render
                    window.update()
                elif letter == 'i':
                    if double:
                        display_image.configure(image = I32render)
                        display_image.image = I32render
                    else:
                        display_image.configure(image = I3render)
                        display_image.image = I3render
                    window.update()
                elif letter == 'j':
                    if double:
                        display_image.configure(image = J32render)
                        display_image.image = J32render
                    else:
                        display_image.configure(image = J3render)
                        display_image.image = J3render
                    window.update()
                elif letter == 'k':
                    if double:
                        display_image.configure(image = K32render)
                        display_image.image = K32render
                    else:
                        display_image.configure(image = K3render)
                        display_image.image = K3render
                    window.update()
                elif letter == 'l':
                    if double:
                        display_image.configure(image = L32render)
                        display_image.image = L32render
                    else:
                        display_image.configure(image = L3render)
                        display_image.image = L3render
                    window.update()
                elif letter == 'm':
                    if double:
                        display_image.configure(image = M32render)
                        display_image.image = M32render
                    else:
                        display_image.configure(image = M3render)
                        display_image.image = M3render
                    window.update()
                elif letter == 'n':
                    if double:
                        display_image.configure(image = N32render)
                        display_image.image = N32render
                    else:
                        display_image.configure(image = N3render)
                        display_image.image = N3render
                    window.update()
                elif letter == 'o':
                    if double:
                        display_image.configure(image = O32render)
                        display_image.image = O32render
                    else:
                        display_image.configure(image = O3render)
                        display_image.image = O3render
                    window.update()
                elif letter == 'p':
                    if double:
                        display_image.configure(image = P32render)
                        display_image.image = P32render
                    else:
                        display_image.configure(image = P3render)
                        display_image.image = P3render
                    window.update()
                elif letter == 'q':
                    if double:
                        display_image.configure(image = Q32render)
                        display_image.image = Q32render
                    else:
                        display_image.configure(image = Q3render)
                        display_image.image = Q3render
                    window.update()
                elif letter == 'r':
                    if double:
                        display_image.configure(image = R32render)
                        display_image.image = R32render
                    else:
                        display_image.configure(image = R3render)
                        display_image.image = R3render
                    window.update()
                elif letter == 's':
                    if double:
                        display_image.configure(image = S32render)
                        display_image.image = S32render
                    else:
                        display_image.configure(image = S3render)
                        display_image.image = S3render
                    window.update()
                elif letter == 't':
                    if double:
                        display_image.configure(image = T32render)
                        display_image.image = T32render
                    else:
                        display_image.configure(image = T3render)
                        display_image.image = T3render
                    window.update()
                elif letter == 'u':
                    if double:
                        display_image.configure(image = U32render)
                        display_image.image = U32render
                    else:
                        display_image.configure(image = U3render)
                        display_image.image = U3render
                    window.update()
                elif letter == 'v':
                    if double:
                        display_image.configure(image = V32render)
                        display_image.image = V32render
                    else:
                        display_image.configure(image = V3render)
                        display_image.image = V3render
                    window.update()
                elif letter == 'w':
                    if double:
                        display_image.configure(image = W32render)
                        display_image.image = W32render
                    else:
                        display_image.configure(image = W3render)
                        display_image.image = W3render
                    window.update()
                elif letter == 'x':
                    if double:
                        display_image.configure(image = X32render)
                        display_image.image = X32render
                    else:
                        display_image.configure(image = X3render)
                        display_image.image = X3render
                    window.update()
                elif letter == 'y':
                    if double:
                        display_image.configure(image = Y32render)
                        display_image.image = Y32render
                    else:
                        display_image.configure(image = Y3render)
                        display_image.image = Y3render
                    window.update()
                elif letter == 'z':
                    if double:
                        display_image.configure(image = Z32render)
                        display_image.image = Z32render
                    else:
                        display_image.configure(image = Z3render)
                        display_image.image = Z3render
                    window.update()
                else:
                    print("!!!ERROR!!!")
    display_image.configure(image = blankRender)
    display_image.image = blankRender



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

word = ''
def generateNewWord():
    global word
    global dataTracking
    word = choice(d.words)
    if len(word) >= min_length:
        dataTracking.update({word:[0, 0, [time()], 0]})
        play_word(word)
    else:
        generateNewWord()

def analyze():
    from util import analyze

def checkWord(word):
    global score_int
    global dataTracking
    text = word_input.get()
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

blank_load = Image.open('images/blank.jpg')
blank_load = blank_load.resize((450, 450))
blankRender = ImageTk.PhotoImage(blank_load)

display_image = tk.Label(master = image_frame, image = blankRender)

display_image.configure(image = blankRender)
display_image.image = blankRender


hello = tk.Label(master = hello_frame, text = 'Welcome to fingerspelling training!')
check_word = tk.Button(master = input_frame, text = 'check', command = lambda: checkWord(word))
new_word = tk.Button(master = replay_frame, text = 'new word', command = lambda: generateNewWord())
replay_word = tk.Button(master = replay_frame, text = 'play', command = lambda: play_word(word))
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

if v:print('starting!')

generateNewWord()
#print('Secret word: %s'%word)


window.bind("<Return>", checkWordWorkaround)
window.bind('<space>', play_word)
window.mainloop()
