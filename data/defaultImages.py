##Nathan Hinton
# This file was generated from addImageset.py

from PIL import Image, ImageTk

size = (400, 400)

smileload = Image.open('images/smile.jpg')
smileload = smileload.resize(size)
smileRender = ImageTk.PhotoImage(smileload)

blankload = Image.open('images/blank.jpg')
blankload = blankload.resize(size)
blankRender = ImageTk.PhotoImage(blankload)