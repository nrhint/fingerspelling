##Nathan Hinton
##This program will load all of the images for use by the playWord script

import pygame
from os import listdir

size = 550

files = listdir('Images')

#Get the number of files that are there. There should be 52 * number_of_image_sets + 2 files
image_set_count = (len(files) - 2) / 52
alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']


if not image_set_count.is_integer():
    print("RECOVERABLE ERROR: Wrong number of images in the images folder. This may cause unintended errors or not all the images to be used!")
    image_set_count = int(image_set_count)

new_data = True
while new_data:
    try:
        with open('data/images.py', 'r') as f:
            lines = f.read().splitlines()
            if int(lines[2][1]) == image_set_count+1:
                new_data = False
    except FileNotFoundError:
        print('RECOVERABLE ERROR: images file not found!!!')
        print('Recreating the file outline...')
        with open('data/images.py', 'w') as f:
            f.write(
                """##Nathan Hinton
##This file should not be edited as it has information that if moved will make the program not function
#1

def run():
    imageSets = []
    
                        
"""
            )
    else:
        if new_data:
            print('New images found or old ones deleted. Regenerating the images file...')
            number = int(lines[2][1])
            data = '''##Nathan Hinton
# This file was generated from loadImages.py

import pygame

def run(imageSets):
    '''
            for letter in alpha:
                one = letter + str(number)
                two = letter + str(number) + '2'
                data += """
    ##############
    %sload = pygame.image.load('Images/%s.jpg')
    %sload = pygame.transform.scale(%sload, (%s, %s))

    %sload = pygame.image.load('Images/%s.jpg')
    %sload = pygame.transform.scale(%sload, (%s, %s))
        """%(one, one, one, one, size, size, two, two, two, two, size, size)
            data += "\n    imageSets.append([[A%s2load, B%s2load, C%s2load, D%s2load, E%s2load, F%s2load, G%s2load, H%s2load, I%s2load, J%s2load, K%s2load, L%s2load, M%s2load, N%s2load, O%s2load, P%s2load, Q%s2load, R%s2load, S%s2load, T%s2load, U%s2load, V%s2load, W%s2load, X%s2load, Y%s2load, Z%s2load], [A%sload, B%sload, C%sload, D%sload, E%sload, F%sload, G%sload, H%sload, I%sload, J%sload, K%sload, L%sload, M%sload, N%sload, O%sload, P%sload, Q%sload, R%sload, S%sload, T%sload, U%sload, V%sload, W%sload, X%sload, Y%sload, Z%sload]])"%(number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number)
            data += "\n    return imageSets"
            with open('data/images%s.py'%number, 'w') as tmp:
                tmp.write(data)
            with open('data/images.py', 'r+') as im:
                im.seek(121)
                im.write(str(int(lines[2][1])+1))
            with open('data/images.py', 'r+') as im:
                length = len(im.read())
                im.seek(length - 20)
                im.write("""
    
    print('loading image set %i...')
    import data.images%s
    imageSets = data.images%s.run(imageSets)
    return imageSets"""%(number, number, number))

from time import time
start = time()
import data.images
images = data.images.run()
blankRender = pygame.image.load('Images/blank.jpg')
blankRender = pygame.transform.scale(blankRender, (size, size))
smile = pygame.image.load('Images/smile.jpg')
smile = pygame.transform.scale(smile, (size, size))

end = time()
print('it too %s seconds to load the images'%str(end-start))
