##Nathan Hinton
##Main program for the fingerspelling trining !!!DO NOT ADD UNTIL THE SAFE MARKER!!!

import tkinter as tk
from time import time, sleep
from random import choice
from util.addImageset import generateNewImages

profile = input('Enter name or press enter to use default profile: ')

# load from file the configuration:
try:
    with open('%s.cfg'%profile, 'r') as f:
        file_data = f.read()
        print('Welcome %s'%profile)
except FileNotFoundError:
    print('using default profile')
    with open('config.cfg', 'r') as f:
        file_data = f.read()

data = []
for line in file_data.split('\n'):
    if line == '' or line[0] == '#':
        pass
    else:
        data.append(line)

game_score = float(data[0]) #The score will change the programs attributes
increase_rate = float(data[1])
decrease_rate = float(data[2])
score_int = int(data[3])

def save_data():
    file = ''
    file += str(game_score) + '\n'
    file += str(increase_rate) + '\n'
    file += str(decrease_rate) + '\n'
    file += str(score_int)
    with open('%s.cfg'%profile, 'w') as f:
        f.write(file)

v = True
if v:print('loading the window...')

show_letters = False

#Start the window
window = tk.Tk()
window.geometry("500x650")
window.title('Fingerspelling training')
speed_var = tk.IntVar()
word_input = tk.StringVar()
word_length_var = tk.IntVar()

from data.defaultImages import *

for x in range(0, 4):
    try:
        open('imageSet%s.pk'%(x+1), 'r')
        open('./data/images%s.py'%(x+1), 'r')
    except FileNotFoundError:
        generateNewImages(x+1)
        print('generated %s'%(x+1))

from util.playWord import play_word

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

word = ''

def checkWordWorkaround(null):
    checkWord(word)

def play_word_workaround(word):
    global game_score
    game_score -= decrease_rate
    speed = game_score
    if v:print(speed)
    play_word(word, speed, display_image, window, show_letters)

def generateNewWord():
    global word
    save_data()
    word = choice(d.words)
    if len(word) >= min_length:
        play_word_workaround(word)
    else:
        generateNewWord()

def checkWord(word):
    global score_int
    global game_score
    global speed
    text = word_input.get()
    if text == '':
        speed_var.set(game_score * 1.8)
        play_word_workaround(word)
    else:
        word_input.set('')
        if v:print(word, text)
        if text == word:
            score_int += 1
            game_score += increase_rate+decrease_rate #Every time the word is played it will go down so this will nullify the next one
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
            game_score -= decrease_rate
            score.configure(text = '%s'%score_int)
            score.text = 'Score: %s'%score_int
            window.update()

display_image = tk.Label(master = image_frame, image = blankRender)

display_image.configure(image = blankRender)
display_image.image = blankRender


hello = tk.Label(master = hello_frame, text = 'Welcome to fingerspelling training!')
check_word = tk.Button(master = input_frame, text = 'check', command = lambda: checkWord(word))
new_word = tk.Button(master = replay_frame, text = 'new word', command = lambda: generateNewWord())
replay_word = tk.Button(master = replay_frame, text = 'play', command = lambda: play_word_workaround(word))
entry = tk.Entry(master = input_frame, textvariable = word_input, fg="yellow", bg="blue", width=15)
score = tk.Label(master = score_frame, text = 'Score: %s'%score_int)

if v:print('finishing up...')

hello.pack()
display_image.pack()
new_word.pack(side = tk.LEFT)
replay_word.pack(side = tk.RIGHT)
entry.pack(side = tk.LEFT)
check_word.pack(side = tk.RIGHT)
score.pack()
# analyze_data.pack(side = tk.LEFT)

speed = 180#int(input('speed: '))#Speed will be measured in chars per min
speed_var.set(180)
min_length = 4
word_length_var.set(3)

if v:print('starting!')

generateNewWord()
#print('Secret word: %s'%word)

window.bind("<Return>", checkWordWorkaround)
window.bind('<space>', play_word_workaround)
window.mainloop()
