# -*- coding: utf-8 -*-
"""
change_pixels.py modifies an image's pixels using nested for loops.

Uses procedural programming paradigm instead of functional programming paradigm.
"""
import matplotlib.pyplot as plt
import os.path
from itertools import chain # allows chaining of ranges for iterative operations
import numpy as np  # “as” lets us use standard abbreviations
from PIL import Image  # *1 Added in 2019 to address new behavior of matplotlib.pyplot (results in immutable ndarray)

###
# Read the image data
###

# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'RedOrBlue.jpg')
# Read the image data into an array
img = plt.imread(filename)  # This method results in an immutable ndarray of image data.

img_b = np.array(Image.open(filename))# see *1 This method results in a writable ndarray.
img_c = np.array(Image.open(filename))
###
# Make two rectangles of yellow pixels
###
height = len(img_b)
width = len(img_b[0])
for row in range(75, 85):
    for column in chain(range(176, 196), range(208, 228)):
        img_b[row][column] = [255, 255, 0]  # red + green = yellow
height = len(img_c)
width = len(img_c[0])
for row in range(30, 145):
    for column in chain(range(165, 230)):
        img_c[row][column] = [0, 255, 0]
height = len(img_c)
width = len(img_c[0])
for row in range(20, 134):
    for column in range(width):
        if sum(img_c[row][column]) > 400: #(max brightness is 3*255=765)
            img_c[row][column]=[255,0,255] # R + B = magenta


###
# Show the image data
###

# Create figure with 2 subplots
fig, ax = plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img_b, interpolation='none')
ax[2].imshow(img_c, interpolation='none')
# Show the figure on the screen
fig.show()
