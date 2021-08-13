##Nathan Hinton
##This is a transition to using pygame for the main engine not tkinter.
##This main program should mostly be an empty shell that allows other files to do the background work.

h = input('Height: ')
if h == '':h = 600
else:h = int(h)

with open('size', 'w') as s:
    s.write(str(h-50))

import pygame
from time import time, sleep
from threading import Thread
from util.dictionary import Dictionary
from util.playWord import play
from util.entry import InputBox
from util.score import Score
from random import choice

class Game:
    def __init__(self):
        self.v = True
        self.profile = input('Enter name or press enter to use default profile: ')

        # load from file the configuration:
        try:
            with open('%s.cfg'%self.profile, 'r') as f:
                file_data = f.read()
                print('Welcome %s'%self.profile)
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

        #Load all the data
        #Pygame data:
        self.background_colour = (150, 150, 150)
        (self.width, self.height) = (int(h/0.75), int(h))
        if self.width > self.height:
            self.short = self.height-50
        else:
            self.short = self.width-50

        self.imagex = (self.width-self.short)/2
        pygame.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption('Fingerspelling')
        self.screen.fill(self.background_colour)
        pygame.display.flip()

        #User data:
        self.play_speed = float(data[0]) #The score will change the programs attributes
        self.increase_rate = float(data[1])
        self.decrease_rate = float(data[2])
        self.score_int = int(data[3])
        self.dictionary_path = str(data[4])
        
        #Image data:
        self.smile = pygame.image.load('Images/smile.jpg')#Takes 0.17815
        self.smile = pygame.transform.scale(self.smile, (self.short, self.short))#takes 0.00352

        #Dictionary:
        self.d = Dictionary(self.dictionary_path, False)

        #Setup the entry box
        if self.v:print(self.width, self.height)
        if self.v:print((self.width/2)-50, h-50, 100, 50)
        self.entry = InputBox((self.width/2)-100, h-50, 96, 50, pygame, self.background_colour, False)

        #Setup the score:
        if self.v:print('starting the score counter...')
        self.scoreCount = Score(self.width, self.height, pygame, str(self.score_int), self.background_colour, False)#Last is the debug var

        #Start the screen updating thread:
        # screen_update_thread = Thread(target=self.updateScreen, args=(self, ))
        # screen_update_thread.start()

        self.run()

    def save_data(self):
        file = ''
        file += str(self.play_speed) + '\n'
        file += str(self.increase_rate) + '\n'
        file += str(self.decrease_rate) + '\n'
        file += str(self.score_int) + '\n'
        file += str(self.dictionary_path)

        with open('%s.cfg'%self.profile, 'w') as f:
            f.write(file)

    def run(self):
        running = True
        self.state = 'choose_new_word'
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                word = self.entry.handle_event(event)

            if self.state == 'choose_new_word':
                self.word = choice(self.d.words).lower()
                self.state = 'play_word'
            elif self.state == 'play_word':
                self.play_word()
                self.state = 'wait_for_input'
            elif self.state == 'wait_for_input':
                if word != None:
                    if self.v:print(word, self.word)
                    if word.lower() == self.word:#The input was correct:
                        self.play_speed += self.increase_rate
                        self.scoreCount.add(self.screen)
                        self.state = 'victory_screen'
                    elif word == '':
                        self.play_word()
                        sleep(0.2)
                    else:
                        self.play_speed -= self.decrease_rate
                        self.scoreCount.subtract(self.screen)
                        sleep(0.2)
                sleep(0.05)
            elif self.state == 'victory_screen':
                self.screen.blit(self.smile, (self.imagex, 0))
                pygame.display.flip()
                sleep(1)
                self.state = 'choose_new_word'
            else:
                print("ERROR: State = %s"%self.state)
                running = False
            self.entry.update()
            self.entry.draw(self.screen)
            self.scoreCount.draw(self.screen)
            pygame.display.flip()
        pygame.quit()
        self.save_data()

    # def updateScreen(self):
    #     sleep(0.5)
    #     self.updateScreen()

    def play_word(self):
        processThread = Thread(target=play, args=(self.word.lower(), self.play_speed, self.screen, self.imagex, True))#Last of verbose
        processThread.start()



main = Game()

print('Finished')