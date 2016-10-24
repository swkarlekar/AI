from tkinter import Tk, Canvas, YES, BOTH, PhotoImage, NW
from time import clock
from random import choice
from math import sqrt, atan2, tan, degrees, cos, radians
from types import *
root = Tk()
START = clock()
WIDTH = 512
HEIGHT = 512
COLORFLAG = False
HIGH = 45
LOW = 10

def main():
	image = [0] * HEIGHT * WIDTH
	#displayImageInWindow(image) #completely black image
	#imageNoise(image)
	#displayImageInWindow(image) #white noise image
	#drawLine(0, 50, image)
	#drawLine(5, 0, image)
	drawCircle(100, 20, image)
	#drawLineRT(170, 30, image)
	#draw30lines(image)
	displayImageInWindow(image) #diagonal line image
	root.mainloop()

def imageNoise(image, points=500): 
	from random import randint
	for n in range(points):
		r = randint(0, HEIGHT-1)
		c = randint(0, WIDTH-1)
		image[WIDTH*r + c] = 255
 
def drawCircle(start, r, image):
	for x in range(-r, r):
		y = int(sqrt(r**2-x**2))
		index1 = (y+100)*WIDTH + (x+100)
		index2 = (-y+100)*WIDTH + (x+100)
		if 0<=index1<len(image) and 0<=index2<len(image):
			image[index1] = 255
			image[index2] = 255

def drawLineRT(r, t, image):
	xcoor = r/cos(radians(t))
	print(xcoor)
	ycoor = r/cos(radians(90-t))
	print(ycoor)
	m = (0 - ycoor)/(xcoor)
	drawLine(m, ycoor, image)

def draw30lines(image):
	r = WIDTH/2
	for theta in range(12, 360, 12):
		m = 1/tan(radians(theta))
		b = r+r/tan(radians(theta))
		drawLine(-m, b, image)
	for row in range(WIDTH):
		for col in range(HEIGHT):
			if col == WIDTH/2:
				index = row*WIDTH + col
				image[index] = 255

def drawLine(m, b, image):
	for x in range(WIDTH):
		index = int(m*x+b)*WIDTH+x
		if 0<=index<len(image):
			image[index] = 255

def printElapsedTime(msg = 'time'):
	length = 30
	msg = msg[:length]
	tab = '.'*(length-len(msg))
	print('--' + msg.upper() + tab + ' ', end = "")
	time = round(clock()-START, 1)
	print('%2d'%int(time/60), ' min :', '%4.1f'%round(time%60, 1), \
		' sec', sep = '')

def displayImageInWindow(image):
	global x
	x = ImageFrame(image)

class ImageFrame:
	def __init__(self, image, COLORFLAG = False):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT): 
			for col in range(WIDTH):
				num = image[row*WIDTH + col]
				if COLORFLAG == True:
					kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])
				else:
					kolor = '#%02x%02x%02x' % (num, num, num)
				self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)
		printElapsedTime('displayed image')

if __name__ == '__main__': main()