##Nathan Hinton
##making a file that will add new images for use in the program.

import importlib

alpha = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']

def generateNewImages(number = False):
    if not number:
        number = int(input('what number of set is this? '))
    try:
        open('./Images/A%s.jpg'%number)
    except FileNotFoundError:
        #print('FAIL')
        #print(number)
        return 'Fail'
    print('This may take a while, preloading the images for set %s future use...'%number)
    newFile = '''##Nathan Hinton
# This file was generated from addImageset.py

from PIL import Image
from pickle import dump

size = (400, 400)

print('loading image set %s...')'''%number
    for letter in alpha:
        one = letter + str(number)
        two = letter + str(number) + '2'
        newFile += """
##############
%sload = Image.open('images/%s.jpg')
%sload = %sload.resize(size)

%sload = Image.open('images/%s.jpg')
%sload = %sload.resize(size)
"""%(one, one, one, one, two, two, two, two)

    newFile += "resizedImages = [A%s2load, B%s2load, C%s2load, D%s2load, E%s2load, F%s2load, G%s2load, H%s2load, I%s2load, J%s2load, K%s2load, L%s2load, M%s2load, N%s2load, O%s2load, P%s2load, Q%s2load, R%s2load, S%s2load, T%s2load, U%s2load, V%s2load, W%s2load, X%s2load, Y%s2load, Z%s2load, A%sload, B%sload, C%sload, D%sload, E%sload, F%sload, G%sload, H%sload, I%sload, J%sload, K%sload, L%sload, M%sload, N%sload, O%sload, P%sload, Q%sload, R%sload, S%sload, T%sload, U%sload, V%sload, W%sload, X%sload, Y%sload, Z%sload]"%(number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number)
    newFile += "\ndump(resizedImages, open('imageSet%s.pk', 'wb'))"%number
    newFile += "\nprint('finished preloading loading image set %s...')"%number

    open('./data/preloadImageSet.py', 'w').write(newFile)
    import data.preloadImageSet
    importlib.reload(data.preloadImageSet)

    newFile = '''##Nathan Hinton
# This file was generated from addImageset.py

from PIL import Image, ImageTk
from pickle import load

print('loading image set %s from database...')
try:
    A%s2load, B%s2load, C%s2load, D%s2load, E%s2load, F%s2load, G%s2load, H%s2load, I%s2load, J%s2load, K%s2load, L%s2load, M%s2load, N%s2load, O%s2load, P%s2load, Q%s2load, R%s2load, S%s2load, T%s2load, U%s2load, V%s2load, W%s2load, X%s2load, Y%s2load, Z%s2load, A%sload, B%sload, C%sload, D%sload, E%sload, F%sload, G%sload, H%sload, I%sload, J%sload, K%sload, L%sload, M%sload, N%sload, O%sload, P%sload, Q%sload, R%sload, S%sload, T%sload, U%sload, V%sload, W%sload, X%sload, Y%sload, Z%sload = load(open('imageSet%s.pk', 'rb'))
except FileNotFoundError:
    from util.addImageset import generateNewImages
    generateNewImages(%s)
'''%(number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number, number)
    for letter in alpha:
        newFile += '%s%srender = ImageTk.PhotoImage(%s%sload)\n'%(letter, number, letter, number)
        newFile += '%s%s2render = ImageTk.PhotoImage(%s%s2load)\n'%(letter, number, letter, number)
    open('./data/images%s.py'%number, 'w').write(newFile)

    ##Regenerate the main.py file
    data = open('./util/playWord.py', 'r').read()
    data = data.split('\n')
    newText = '''
            elif r == %s:
                if letter == 'a':
                    if double:
                        display_image.configure(image = A%s2render)
                        display_image.image = A%s2render
                    else:
                        display_image.configure(image = A%srender)
                        display_image.image = A%srender
                    window.update()\n'''%(number, number, number, number, number)
    for letter in alpha[1:]:
        newText+= '''
                elif letter == '%s':
                    if double:
                        display_image.configure(image = %s%s2render)
                        display_image.image = %s%s2render
                    else:
                        display_image.configure(image = %s%srender)
                        display_image.image = %s%srender
                    window.update()'''%(letter.lower(), letter, number, letter, number, letter, number, letter, number)
    data.insert(32,newText)
    newText = ''
    for line in data:
        newText += line+'\n'
    open('./util/playWord.py', 'w').write(newText)
    return 'Pass'

    # file = open('main.py', 'r')
    # print('restart the program for the change to be applied...')
    # # from time import sleep
    # sleep(5)
    # quit()
