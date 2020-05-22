import matplotlib.pyplot as plt
from PIL import Image
from itertools import chain
import os.path
import numpy as np      # “as” lets us use standard abbreviations

'''Read the image data'''
# Get the directory of this python script
directory = os.path.dirname(os.path.abspath(__file__))
# Build an absolute filename from directory + filename
filename = os.path.join(directory, 'woman.jpg')
# Read the image data into an array
img = np.array(Image.open('tinyCat.jpg'))
print(type(img))
print(img)
print(len(img))
print(len(img[0]))
print(img[5][9])
print(img[4][10])
print(img[24][24])
print(img.flags)
'''Show the image data'''
# Create figure with 1 subplot
fig, ax = plt.subplots(1, 2)
# Show the image data in a subplot
ax[0].imshow(img, interpolation='none')
ax[1].imshow(img, interpolation='none')
# Show the figure on the screen
fig.show()