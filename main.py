##Nathan Hinton
##This is a transition to using pygame for the main engine not tkinter.
##This main program should mostly be an empty shell that allows other files to do the background work.

import pygame
from time import time
from util.dictionary import Dictionary
from util.playWord import play
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
        (self.width, self.height) = (800, 600)
        if self.width > self.height:
            self.short = self.height-50
        else:
            self.short = self.width-50
        self.imagex = (self.width-self.short)/2
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
        self.blank = pygame.image.load('Images/blank.jpg')#Takes 0.17815
        self.blank = pygame.transform.scale(self.blank, (self.short, self.short))#takes 0.00352

        #Dictionary:
        self.d = Dictionary(self.dictionary_path, self.v)

        self.run()

    def save_data(self):
        file = ''
        file += str(self.play_speed) + '\n'
        file += str(self.increase_rate) + '\n'
        file += str(self.decrease_rate) + '\n'
        file += str(self.score_int)
        with open('%s.cfg'%self.profile, 'w') as f:
            f.write(file)

    def run(self):
        running = True
        self.state = 'choose_new_word'
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            self.screen.blit(self.blank, (self.imagex, 0))
            if self.state == 'choose_new_word':
                self.word = choice(self.d.words)
                self.state = 'play_word'
            elif self.state == 'play_word':
                play(self.word, self.play_speed, self.v)
            else:
                print("ERROR: State = %s"%self.state)
                running = False
            pygame.display.flip()
        pygame.quit()
        self.save_data()



main = Game()

print('Finished')