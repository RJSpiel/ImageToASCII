'''Name: Raymond Spieldenner
Final Project: Basic Image to ASCII Converter
Date: 3/7/2022'''

'''This is a script that converts basic images into ASCII using the Python Image Library(PIL) and Termcolor for altering
the color of the ASCII characters.'''

'''Instructions:
        1) select an image of your choosing and copy its filepath.
        2) input a width value of 150 or below.
        3) select a color from the provided list.
    If there is an issue with the program, the best fix to try is selecting a smaller image.
    
    You must has the python extensions PIL and termcolor installed for the program to function in this state.'''

import sys
from PIL import Image
from termcolor import colored

userInput = input('Enter file path: ')
userWidth = int(input('Enter Desired Width: '))
userColor = input('Colors:\nRed\nGreen\nBlue\nor other for B&W\nPick a color: ')


path = sys.argv
img = Image.open(userInput)
width, heigth = img.size
aspect_ratio = heigth / width
new_width = userWidth
new_height = aspect_ratio * new_width
img = img.resize((new_width, int(new_height)))

img = img.convert('L')
pixel = img.getdata()

character = ["@", "#", "S", "?", "*", "+", ";", ":", ",", "."]

new_pixel = [character[pixels // 150] for pixels in pixel]
new_pixel = ''.join(new_pixel)
new_pixel_count = len(new_pixel)
final_image = [new_pixel[index:index + new_width] for index in range(0, new_pixel_count, new_width)]
final_image = '\n'.join(final_image)

if userColor == 'red':
    coloredImage = colored(final_image, 'red')
    print(coloredImage, end=' ')

if userColor == 'green':
    coloredImage = colored(final_image, 'green')
    print(coloredImage, end=' ')

if userColor == 'blue':
    coloredImage = colored(final_image, 'blue')
    print(coloredImage, end=' ')

if userColor == 'other':
    print(final_image, end=' ')

