'''
+===========================================+
|											|
|	Machine Vision							|
|	Detects edges in .ppm pictures			|
|	Alison Hau								|
|	Period 2, 10 - 25 February 2015			|
|											|
+===========================================+
'''
#------------------------------------------------------------------------------------- Edge Detector --
def openFile(name):
	filename = open(name, 'r')

	tmpNums = filename.read().split()
	nums = []
	for n in tmpNums:
		nums.append(int(n))

	filename.close()
	return nums
#------------------------------------------------------------------------------------- Edge Detector --
def gaussianSmoothing(image):
	mask = [1, 2, 1, 2, 4, 2, 1, 2, 1]
	grayFile = openFile('grayScale.ppm')
	image2 = []

	for e in range(len(grayFile)):
		if (e <= WIDTH) or (e >= (len(grayFile) - WIDTH)) or (e % WIDTH == 0) or (e % WIDTH == WIDTH - 1):
			image2.append(image[e])
		else:
			masked = applyMask(e, mask, image)
			val = round((1/16)  * masked)
			image2.append(val)

	return image2
#------------------------------------------------------------------------------------- Edge Detector --
def sobelMask(image):
	Sy = [1, 2, 1, 0, 0, 0, -1, -2, -1]
	Sx = [-1, 0, 1, -2, 0, 2, -1, 0, 1]

	smoothedFile = openFile('smoothedGrayScale.ppm')
	image2 = []		# list of lists, each sublist [magnitude, angle approx, edge, been here, to print]

	for e in range(len(smoothedFile)):
		if (e <= WIDTH) or (e >= (len(smoothedFile) - WIDTH)) or (e % WIDTH == 0) or (e % WIDTH == WIDTH - 1):
			image2.append([image[e], 0, 0, 1, 0])	# direction of edges?
		else:
			Gy = applyMask(e, Sy, image)
			Gx = applyMask(e, Sx, image)

			mag = sqrt(Gx*Gx + Gy*Gy)
			deg = theta(Gy, Gx)

			image2.append([mag, deg, 0, 0, 0])

	return image2
#------------------------------------------------------------------------------------- Edge Detector --
def theta(y, x):
	rawAngle = degrees(atan2(y, x))
	if rawAngle < 0:
		rawAngle += 180
	theta = int(((abs(rawAngle + 22.5) // 45)) % 4)

	return theta
#------------------------------------------------------------------------------------- Edge Detector --
def cannyTransform(image):
	image2 = []
	for e in range(len(image)):
		if (e <= WIDTH) or (e >= (len(image) - WIDTH)) or (e % WIDTH == 0) or (e % WIDTH == WIDTH - 1):
			continue
		else:
			deg = image[e][1]
			if deg == 0:
				cellsLookedAt = (e - 1, e + 1)	# (W, E)
			elif deg == 1:
				cellsLookedAt = (e - WIDTH + 1, e + WIDTH - 1)	# (NE, NW)
			elif deg == 2:
				cellsLookedAt = (e - WIDTH, e + WIDTH)			# (S, N)
			elif deg == 3:
				cellsLookedAt = (e - WIDTH - 1, e + WIDTH + 1)	# (NW, SE)
			else:
				exit('shit')

			if (image[e][0] > image[cellsLookedAt[0]][0]) and (image[e][0] > image[cellsLookedAt[1]][0]):
				image[e][2] = 1

	image2 = doubleThreshold(image)

	return image2
#------------------------------------------------------------------------------------- Edge Detector --
def doubleThreshold(image):
	for e in range(len(image)):
		if image[e][2] == 0:
			continue
		elif (image[e][2] == 1) and (image[e][0] > HIGH):
			image[e][4] = 1
			checkNeighbors(e, image)
	return image
#------------------------------------------------------------------------------------- Edge Detector --
def checkNeighbors(e, image):
	cellsToVisit = [e - WIDTH, e - 1, e + 1, e + WIDTH]		#[N, W, E, S]
	if image[e][3] == 1:
		return
	image[e][3] = 1
	for index in cellsToVisit:
		if (index > 0) and (image[index][2] == 1) and (image[index][0] > LOW) and (index < WIDTH * HEIGHT):
			image[index][3] = 1
			if image[index][4] == 0:
				image[index][4] = 1
				checkNeighbors(index, image)
#------------------------------------------------------------------------------------- Edge Detector --
def applyMask(e, mask, image):

	NW = mask[0] * image[e - WIDTH - 1]
	N = mask[1] * image[e - WIDTH]
	NE = mask[2] * image[e - WIDTH + 1]
	W = mask[3] * image[e - 1]
	C = mask[4] * image[e]
	E = mask[5] * image[e + 1]
	SW = mask[6] * image[e + WIDTH - 1]
	S = mask[7] * image[e + WIDTH]
	SE = mask[8] * image[e + WIDTH + 1]

	return NW + N + NE + W + C + E + SW + S + SE

	return val
#------------------------------------------------------------------------------------- Edge Detector --
def normalize(image, intensity = 255):
	m = max(image)
	printElapsedTime('normalizing')
	return [int(x*intensity/m) for x in image]
#------------------------------------------------------------------------------------- Edge Detector --
def displayImageInWindow(image):
	global x		 # necessary
	x = ImageFrame(image)
#------------------------------------------------------------------------------------- Edge Detector --
def printElapsedTime(msg = 'time'):
	length = 30
	msg = msg[:length]
	tab = '.' * (length-len(msg))	# <-- msg length truncated at 30 chars
	print ('--' + msg.upper() + tab + ' ', end = '')
	time = round(clock() - START, 1)
	print ('%2d'%int(time/60), ' min : ', '%4.1f'%round(time%60, 1), ' sec', sep = '')
#------------------------------------------------------------------------------------- Edge Detector --
class ImageFrame:
	def __init__(self, image, COLORFLAG = False):
		self.img = PhotoImage(width = WIDTH, height = HEIGHT)
		for row in range(HEIGHT):
			for col in range(WIDTH):
				num = image[row * WIDTH + col]
				if COLORFLAG == True:
					kolor = '#%02x%02x%02x' % (num[0], num[1], num[2])		# color
				else:
					kolor = '#%02x%02x%02x' % (num, num, num)				# grayscale
				self.img.put(kolor, (col,row))
		c = Canvas(root, width = WIDTH, height = HEIGHT); c.pack()
		c.create_image(0, 0, image = self.img, anchor = NW)
		printElapsedTime ('image displayed')
#=============================================== Main ================================ Edge Detector ==
def main():
# #-- Pull image data from PPM graphics file into a list of string-type numbers
# 	file1 = open ('lena.ppm', 'r')
# 	stng = file1.readline().strip()		# stng = 'P3 512 512 255'
# 	widthAndHeight = file1.readline().split(' ')
# 	WIDTH = int(widthAndHeight[0].strip())
# 	HEIGHT = int(widthAndHeight[1].strip())
# 	MAX_BRIGHTNESS = int(file1.readline().strip())

# 	nums = file1.read().split()	# nums is a list of the data numbers from ppm file
# 	file1.close()

# #-- Create a list of gray-values from file numbers (don't forget to cast strings into ints)
# 	image = []
# 	for pos in range(0, len(nums), 3):
# 		RGB = ( int(nums[pos+0]), int(nums[pos+1]), int(nums[pos+2]) )
# 		image.append( int(0.2*RGB[0] + 0.7*RGB[1] + 0.1*RGB[2]) )
# 	printElapsedTime ('Gray numbers have been created')

# #-- Write gray-values to file
# 	file1 = open('grayScale.ppm', 'w')
# 	for elt in image:
# 		file1.write ( str(elt) + ' ')
# 	printElapsedTime ('gray file numbers saved')
# 	file1.close()

# #-- Smoothing using Gaussian mask (6 times)
# 	for n in range(NUMBER_OF_TIMES_TO_SMOOTH_IMAGE):
# 		image = gaussianSmoothing(image)
# 	printElapsedTime ('smoothed w gaussian mask')

# #-- Write smoothed gray-values to file
# 	file1 = open('smoothedGrayScale.ppm', 'w')
# 	for elt in image:
# 		file1.write(str(elt) + ' ')
# 	printElapsedTime('smoothed file numbers saved')
# 	file1.close()

	image = openFile('smoothedGrayScale.ppm')

#-- Apply Sobel masks to create gradient
	image = sobelMask(image)
	# image = normalize([x[0] for x in image])
	printElapsedTime('sobel mask applied')

#-- Canny transform
	image = cannyTransform(image)
	tmp = []
	for e in image:
		if e[4] == 1:
			# tmp.append(800)
			tmp.append(255)
		else:
			tmp.append(0)
	image = normalize(tmp)
	# image = normalize([x[0] for x in image])
	printElapsedTime('canny transform')

#-- Display modified file as an image
	displayImageInWindow (image)

	root.mainloop()		# <-- required for graphics programs
#---<Globals>------------------------------------------------------------------------- Edge Detector --
# from tkinter import Tk, Canvas, PhotoImage
from tkinter import *
from time import clock
from math import sqrt, atan2, degrees

root = Tk()
START = clock()
WIDTH = 512 		# get this value from the file
HEIGHT = 512 		# get this value from the file
MAX_BRIGHTNESS = 255
COLORFLAG = False 	# True = color image; False = grayscale
HIGH = 45
LOW = 10
NUMBER_OF_TIMES_TO_SMOOTH_IMAGE = 6
#-------------------------------------------------------------------------------------- Edge Detector --
if __name__ == '__main__': main()