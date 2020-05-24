# -*- coding: utf-8 -*-
"""
This code provides a solution to the
change_pixels.py project.
change_pixels.py modifies an image's pixels using
nested for loops.
by Gabriel A Pass 2020
"""
import matplotlib.pyplot as plt
import os.path
from itertools import chain  # allows chaining of ranges for iterative operations
import numpy as np  # â€œasâ€ lets us use standard abbreviations
from PIL import Image  # *1 Added in 2019 to address new




# Get the directory of this python script
directory =os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from
directory + filename
filename = os.path.join(directory, 'RedOrBlue.jpg')
#

img = plt.imread(filename)  # This methodresults in an immutabl endarrayofimagedata.

img_b =np.array(Image.open(filename))  # see *1 This method results in a writablendarray.

img_c = np.array(Image.open(filename))  # see *1 This methodresults in awritablendarray.

###
# Make two rectangles of yellow pixels
###
height = len(img_b)
width = len(img_b[0])
for row in range(75, 85):

for column in chain(range(176, 196), range(208, 228)):

img_b[row][column] = [255, 255, 0]  # red + green = yellow

###
# Morpheus in Magenta
###
height = len(img_c)
width = len(img_c[0])
for row in range(20,
                 134):
    for column in range(width):
        if sum(img_c[row][column]) >
400:
img_c[row][column] = [255, 0, 255]  # red + blue = magenta

###
# Show the image data
###

# Create figure with 2 subplots
fig, ax =
plt.subplots(1, 3)
# Show the image data in the first subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img_b,
             interpolation='none')
ax[2].imshow(img_c, interpolation='none')
# Show the
figure
on
the
screen
fig.show()