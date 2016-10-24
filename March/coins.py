from tkinter import Tk, PhotoImage, Canvas, NW
from time import clock
from math import sin, cos, tan, atan2, pi, sqrt
root = Tk()
START = clock()
WIDTH = 400
HEIGHT = 353
T = 5 #theta
C = 4 #color

class ImageFrame:
	def __init__(self, image):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT): 
			for col in range(WIDTH):
				num = image[row*WIDTH + col][C]
				kolor = 'BLACK'
				if num == 1: 
					kolor = 'WHITE' #gray
				if num == 2: 
					kolor = 'RED'
				self.img.put(kolor, (col, row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)
		printElapsedTime('displayed image')

def extractStructuredDataFromFile(filename):
	'''
	import pickle
	file1 = open(filename, 'rb')
	imageLists = pickle.load(file1)
	file1.close()
	return imageLists
	'''
	file1 = open(filename, 'r')
	stng = file1.readline()
	print(stng)
	nums = file1.read().split()
	print(nums[:10])
	file1.close()

	image = []
	for pos in range(0, len(nums), 3):
		RGB = (int(nums[pos+0]), int(nums[pos+1]), int(nums[pos+2]))
		image.append(int(0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]))
	return image

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

def performHoughTransform(image):
	accumulator = [0]*WIDTH*HEIGHT
	coordinates = []
	for y in range(HEIGHT):
		for x in range(WIDTH):
			index = y*WIDTH+x
			if image[index][C] != 1: 
				continue
			coordinates.append(index) #list of indices that are edges
			drawTangentLine(image, x, y, index, accumulator)
	center = accumulator.index(max(accumulator))
	cy = center//WIDTH
	cx = center%WIDTH
	radiuslst = []
	for coor in coordinates:
		radiuslst.append(findDistance(center, coor)) #list of distances between outer edge and center
	radius = sum(radiuslst)/len(radiuslst) #the average distance between the outer edge and center is the radius
	image = drawCircle(image, cx, cy, radius)

def findDistance(index1, index2):
	y1 = index1//WIDTH
	x1 = index1%WIDTH
	y2 = index2//WIDTH
	x2 = index2%WIDTH
	return sqrt((y2-y1)**2 + (x2-x1)**2)

def drawTangentLine(image, x, y, index, accumulator):
	theta = image[index][T]
	m = -1/(tan(theta)+0.0000000000001) #so there's no dividing by zero
	b = y - m*x
	drawLineMB(image, m, b, accumulator)

def plot(x, y, image, accumulator):
	maxIndex = len(image)
	index = int(y)*WIDTH+int(x)
	if (0<=index<maxIndex) and (0 <= x < WIDTH):
		#image[index][C] = 2 #this line draws the tangent lines
		accumulator[index] += 1

def drawLineMB(image, m, b, accumulator):
	if -1<=m<=1:
		for x in range(WIDTH):
			y = m*x+b
			plot(x, y, image, accumulator)
	else: 
		for y in range(HEIGHT):
			x = (y-b)/m
			plot(x, y, image, accumulator)

def drawCircle(image, cx, cy, radius):
	maxIndex = len(image)
	for t in frange(0, 6.28, 0.01):
		x = int(cx+radius*cos(t))
		y = int(cy+radius*sin(t))
		index = y*WIDTH+x
		if(0<=index<maxIndex) and (0<=x < WIDTH):
			image[index][C] = 2
	print('Circle center (cx, cy) =', cx, cy, 'radius =', radius)
	return image

def displayImageInWindow(image, flag = True):
	global x
	if flag: x = ImageFrame(image)
	root.mainloop()

def main():
	image = extractStructuredDataFromFile("12circlesB_W_F.ppm")
	performHoughTransform(image)
	displayImageInWindow(image, True)

if __name__ == '__main__': START_TIME = clock(); main()