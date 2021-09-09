##Nathan Hinton
##This file is for playing the letters on the screen. 

########BUGS:########
##If the first and last letter are the same it will play the first letter as the second in a serries. This is caused by the way it checks indexes of the word so that it treats it as if it was a circle so the last two letters are basically nxt to each other.


import threading
from time import sleep, time
from random import randint
from threading import Lock

lock = threading.Lock()

from util.loadImages import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def play(word, speed, surface, xPos, v):
    if v:print('getting lock...')
    if v:print('playing word')
    startTime = time()
    interval = 60/speed
    index = -1
    wait_count = 0
    lastLetter = ''
    letter = word[index]
    r = randint(0, int(len(images)/2))
    if v:print(r)
    if v:looped = 0#Using for testing
    double = False
    while index < len(word):
        lock.acquire()

        # if time() >= startTime+interval*(index+1):
        # t = time()
        # print(t - startTime+interval*(index+1))
        index += 1
        lastLetter = letter
        if index == len(word):
            break
        letter = word[index]
        if v:print(letter)
    # else:
        if v:looped += 1
        if lastLetter == letter:
            double = not double
        if double:
            i = images[r][1][letters.index(letter)]
        else:
            i = images[r][0][letters.index(letter)]
        # rect = i.get_rect()
        # remainder = (startTime+(interval*(index+1))-time()) / 2
        # if v:print('Time left: %s'%remainder)
        # inter = remainder/17
        # x = 0
        # while time() < startTime+remainder+(interval*index):
        #     if time() >= startTime+(interval*(index))+(inter*x) and x < 17:
        #         print(time(), startTime+(interval*(index))+(inter*x))
        #         x += 1
        #         if v:print(x*15)
        #         i.set_alpha(x*15)
        #         surface.blit(i, (xPos, 0))
        #         pygame.display.update(rect)
        # if x < 100:
        #     i.set_alpha(150)
        #     surface.blit(i, (xPos, 0))
        surface.blit(i, (xPos, 0))
        pygame.display.flip()
        if v:print('Removing lock...')
        lock.release()
        if v:print('Sleeping for %s seconds'%str(startTime+(interval*(index+1))-time()))
        try:
            sleep(startTime+(interval*(index+1))-time())
        except ValueError:
            pass
    lock.release()
    surface.blit(blankRender, (xPos, 0))
    if v:print('looped %s times'%looped)