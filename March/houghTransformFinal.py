from tkinter import Tk, PhotoImage, Canvas, NW
from time import clock
from math import sin, cos, tan, atan2, pi, sqrt
root = Tk()
START = clock()
WIDTH = 512
HEIGHT = 512
ACCUMULATOR_WIDTH = 314 + 157
ACCUMULATOR_HEIGHT = int(sqrt(WIDTH**2 + HEIGHT**2) + HEIGHT)

class ImageFrame:
	def __init__(self, image):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT): 
			for col in range(WIDTH):
				num = image[row*WIDTH + col]
				if (num == 255) or (num < 252): 
					kolor = '#%02x%02x%02x' % (num, num, num) #gray
				if num == 254: 
					kolor = '#%02x%02x%02x' % (num, 0, 0) #red
				if num == 253:
					kolor = '#%02x%02x%02x' % (0, num, 0) #green
				if num == 252:
					kolor = '#%02x%02x%02x' % (0, 0, num) #blue
				if not (0<= num < 256):
					exit('ERROR: num = ' + num)
				self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)
		printElapsedTime('displayed image')

def printElapsedTime(msg = 'time'):
	length = 30
	msg = msg[:length]
	tab = '.'*(length-len(msg))
	print('--' + msg.upper() + tab + ' ', end = '')
	time = round(clock() - START, 1)
	print('%2d'%int(time/60), ' min:', '%4.1f'%round(time%60,1),' sec', sep = '')

def frange(start, stop, step):
	i = start
	while i < stop: 
		yield i
		i += step

def printStatistics(r, theta, msg = ''):
	print(msg + ': r = ', round(r, 3), 'theta =', round(theta, 2))
	m = -1/tan(theta)
	b = r/sin(theta)
	print(msg + ': m = ', round(m, 2), 'b =', round(b, 2))

def displayImageInWindow(image, flag = True):
	global x
	if flag: x = ImageFrame(image)
	root.mainloop()

def createImage():
	image = [0]*(HEIGHT*WIDTH)
	IMAGE = drawImageNoise(image, num=500)
	r = 300; theta = pi/4
	image = drawLineRT(image, r, theta)
	printStatistics(r, theta, 'Line 1')
	image = drawCircle(image, cx =256, cy =256, radius=100)
	printElapsedTime('Image created w/ line & circle')
	return image

def drawImageNoise(image, num):
	from random import randint
	for n in range(num):
		r = randint(0, len(image))
		image[r] = 255
	return image

def plot(x, y, image, kolor = 0):
	if kolor not in {0, 1, 2, 3}:
		kolor = 0
	maxIndex = len(image)
	index = int(y)*WIDTH+int(x)
	if (0<=index<maxIndex) and (0 <= x < WIDTH):
		num = 255
		image[index] = [255, 254, 253, 252][kolor]

def drawLineMB(image, m, b, kolor = 0):
	if -1<=m<=1:
		for x in range(WIDTH):
			y = m*x+b
			plot(x, y, image, kolor)
	else: 
		for y in range(HEIGHT):
			x = (y-b)/m
			plot(x, y, image, kolor)
	return image

def drawLineRT(image, r, theta, kolor = 0):
	m = -1/tan(theta)
	if -1<=m<=1:
		for x in range(WIDTH):
			y = (r-x*cos(theta))/sin(theta)
			plot(x, y, image, kolor)
	else: 
		for y in range(HEIGHT):
			x = (r-y*sin(theta))/cos(theta)
			plot(x, y, image, kolor)
	return image

def drawCircle(image, cx, cy, radius):
	maxIndex = len(image)
	for t in frange(0, 6.28, 0.01):
		x = int(cx+radius*cos(t))
		y = int(cy+radius*sin(t))
		index = y*WIDTH+x
		if(0<=index<maxIndex) and (0<=x < WIDTH):
			image[index] = 255
	print('Circle center (cx, cy) =', cx, cy, 'radius =', radius)
	return image

def drawNumLinesThroughSamePoint(image, num, cx, cy):
	rtheta = []
	for phi in frange(0, pi, pi/num):
		m = tan(phi)
		b = cy-m*cx
		t = phi-(pi/2)
		r = b*sin(t)
		rtheta.append((r, t))
	return rtheta

def indexAssociatedWith_r_and_theta(r, theta):
	col = int((theta+(pi/2)) *100)
	row = int(r+WIDTH)
	return row*ACCUMULATOR_WIDTH + col

def performHoughTransform(image):
	accumulator = [0]*(ACCUMULATOR_WIDTH*ACCUMULATOR_HEIGHT)
	for y in range(HEIGHT):
		for x in range(WIDTH):
			if image[y*WIDTH+x] == 0: 
				continue
			rtheta = drawNumLinesThroughSamePoint(image, 100, x, y)
			for r, theta in rtheta: 
				accumulator[indexAssociatedWith_r_and_theta(r, theta)] += 1
	return accumulator

def drawDetectedLINEonImage(position, image):
	row = position//ACCUMULATOR_WIDTH
	col = position%ACCUMULATOR_WIDTH
	r = row-WIDTH
	theta = (col - 157.0796327)/100.0#col/100-(pi/2)
	drawLineRT(image, r, theta, 1)
	printStatistics(r, theta, 'Line 2')

def main():
	image = createImage()
	accumulator = performHoughTransform(image)
	maxPosition = accumulator.index(max(accumulator))
	drawDetectedLINEonImage(maxPosition, image)
	displayImageInWindow(image, True)

if __name__ == '__main__': START_TIME = clock(); main()