##Nathan Hinton
##This file is for playing the letters on the screen. 

########BUGS:########
##If the first and last letter are the same it will play the first letter as the second in a serries. This is caused by the way it checks indexes of the word so that it treats it as if it was a circle so the last two letters are basically nxt to each other.
##TODO: Update the data storage method to be in a set of lists not in a bunch of vars


from time import time
from random import randint

from util.loadImages import *

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def play(word, speed, surface, xPos, v):
    if v:print('playing word')
    startTime = time()
    interval = 60/speed
    index = -1
    lastLetter = ''
    letter = word[index]
    r = randint(0, 1)
    if v:print(r)
    if v:looped = 0#Using for testing
    double = False
    while index < len(word):
        if time() >= startTime+interval*(index+1):
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
                surface.blit(images[r][1][letters.index(letter)], (xPos, 0))
                pygame.display.flip()
                # display_image.image = images[r][1][letters.index(letter)]
            else:
                surface.blit(images[r][0][letters.index(letter)], (xPos, 0))
                pygame.display.flip()

                # display_image.image = images[r][0][letters.index(letter)]

    surface.blit(blankRender, (xPos, 0))
    if v:print('looped %s times'%looped)