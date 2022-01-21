#Task: Create two images one with a white circle at center and another with a white rentangle at center and performe all logical gate operations on both images and display the output images.


from PIL import Image, ImageDraw
import matplotlib.pyplot as plt

import numpy as np
import matplotlib.pyplot as plt

c_img = Image.new(mode= 'L', size=(200, 200), color = 0)
circle = ImageDraw.Draw(c_img)
circle.ellipse([(40, 40), (160, 160)], fill = 'white', outline='white')
imgplot = plt.imshow(c_img, cmap = 'gray')
plt.title('c_img')
plt.show()


r_img = Image.new(mode= 'L', size=(200, 200), color = 0)
rectangle = ImageDraw.Draw(r_img)
rectangle.rectangle([(30,50), (170,150)], fill = 'white', outline= 'white')
imgplot = plt.imshow(r_img, cmap='gray')
plt.title('r_img')
plt.show()

c_img = np.asarray(c_img)
r_img = np.asarray(r_img)

# AND gate
and_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(c_img[i,j] == 255 and r_img[i,j] == 255):
            and_img[i,j] = 255

imgplot = plt.imshow(and_img, cmap='gray')
plt.title('AND gate')
plt.show()

# OR gate
or_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(c_img[i,j] == 255 or r_img[i,j] == 255):
            or_img[i,j] = 255

imgplot = plt.imshow(or_img, cmap='gray')
plt.title('OR Gate')
plt.show()


#NAND Gate
nand_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(not(c_img[i,j] == 255 and r_img[i,j] == 255)):
            nand_img[i,j] = 255

imgplot = plt.imshow(nand_img, cmap='gray')
plt.title('NAND Gate')
plt.show()

# NOR gate
nor_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(not(c_img[i,j] == 255 or r_img[i,j] == 255)):
            nor_img[i,j] = 255

imgplot = plt.imshow(nor_img, cmap='gray')
plt.title('NOR Gate')
plt.show()

# XOR gate
xor_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(c_img[i,j] != r_img[i,j]):
            xor_img[i,j] = 255

imgplot = plt.imshow(xor_img, cmap='gray')
plt.title('XOR Gate')
plt.show()

#NOT gate
not_img = np.zeros((200, 200))
for i in range(200):
    for j in range(200):
        if(xor_img[i,j] == 0):
            not_img[i,j] = 255

imgplot = plt.imshow(not_img, cmap='gray')
plt.title('NOT Gate')
plt.show()
