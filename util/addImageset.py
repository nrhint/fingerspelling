##Nathan Hinton
##making a file that will add new images for use in the program.

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def generateNewImages():
    number = int(input('what number of set is this? '))

    newFile = '''##Nathan Hinton
# This file was generated from addImageset.py

from PIL import Image, ImageTk

size = (400, 400)

print('loading image set %s...')'''%number
    for letter in alpha:
        one = letter + str(number)
        two = letter + str(number) + '2'
        newFile += """
##############
%sload = Image.open('images/%s.jpg')
%sload = %sload.resize(size)
%srender = ImageTk.PhotoImage(%sload)
%sload = Image.open('images/%s.jpg')
%sload = %sload.resize(size)
%srender = ImageTk.PhotoImage(%sload)"""%(one, one, one, one, one, one, two, two, two, two, two, two)

    newFile += "\nprint('finished loading image set %s...')"%number

    open('./data/images%s.py'%number, 'w').write(newFile)
    ##Regenerate the main.py file
    data = open('main.py', 'r').read()
    data = data.split('\n')
    data.insert(27, 'from data.images%s import *'%number)
    newMain = ''
    for line in data:
        newMain += line+'\n'
    open('main.py', 'w').write(newMain)
    print('restart the program for the change to be applied...')
    # from time import sleep
    # sleep(5)
    # quit()