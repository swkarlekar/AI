##########################
# Sweta Karlekar         #
# Period 4               #
# Hill-Climber Program   #
# April 21st, 2015       #
##########################

from math import pi, sin, cos
from time import clock
from random import random

START = clock()
MAX_X = 10
MAX_Y = 10
RADIUS = 0.001
MINPOINTS = 1000
NEIGHBORS = 64
sintable = []
costable = []

def main():
	createLookUpTable()

	best = hillClimb()
	printBestList(best)
	printElapsedTime("REGULAR HILL CLIMBER")

	best = hillClimbLookUp()
	printBestList(best)
	printElapsedTime("HILLCLIMBER WITH LOOK UP TABLE")

	best = hillClimbRandom()
	printBestList(best)
	printElapsedTime("HILLCLIMBER WITH RANDOM")

	best = hillClimbGrid()
	printBestList(best)
	printElapsedTime("HILLCLIMBER WITH GRID")

	best = hillClimbNelderMead()
	printBestList(best)
	printElapsedTime("HILLCLIMBER WITH NELDER MEAD")


def printElapsedTime(msg = 'time'):
	length = 30
	msg = msg[:length]
	tab = '.'*(length-len(msg))
	print('--' + msg.upper() + tab + ' ', end = "")
	time = round(clock()-START, 7)
	print('%0.2d'%int(time/60), ' min :', '%5.6f'%round(time%60, 7), \
		' sec', sep = '')
	
def frange(start, stop, step):
	i = start
	terminate = stop - (step/10)
	while i < terminate:
		yield i
		i += step

def f(x, y):
	if x <= 0 or x >= 10 or y <= 0 or y >= 10:
		return float('inf')
	return (x*sin(4*x) + 1.1*y*sin(2*y))

def hillClimb():
	global START
	START = clock()
	best = [float('inf'), float('inf'), float('inf')]
	for (x,y) in randomPoints(MINPOINTS):
		best = compareSurroundingPts(NEIGHBORS, best, x, y)
	return best

def hillClimbLookUp():
	global START
	START = clock()
	best = [float('inf'), float('inf'), float('inf')]
	for (x,y) in randomPoints(MINPOINTS):
		best = compareSurroundingPtsLookUpTable(NEIGHBORS, best, x, y)
	return best

def hillClimbRandom():
	global START
	START = clock()
	best = [float('inf'), float('inf'), float('inf')]
	for (x,y) in randomPoints(MINPOINTS):
		best = [x, y, f(x, y)]
	return best

def hillClimbNelderMead():
	global START
	START = clock()
	nelder = []
	ax = random()*10
	ay = random()*10
	nelder.append([f(ax, ay), ax, ay])
	bx = random()*10
	by = random()*10
	nelder.append([f(bx, by), bx, by])
	for n in range(5000):
		cx = random()*10
		cy = random()*10
		nelder.append([f(cx, cy), cx, cy])
		dx = bx + cx - ax 
		dy = by + cy - ay 
		nelder.append([f(dx, dy), dx, dy])
		ex = (1/2)*(3*bx + 3*cx - 4*ax)
		ey = (1/2)*(3*by + 3*cy - 4*ay)
		nelder.append([f(ex, ey), ex, ey])
		fx = (1/4)*(3*bx + 3*cx - 2*ax)
		fy = (1/4)*(3*bx + 3*cx - 2*ax)
		nelder.append([f(fx, fy), fx, fy])
		gx = (1/4)*(2*ax+bx+cx)
		gy = (1/4)*(2*ax+bx+cx)
		nelder.append([f(gx, gy), gx, gy])
		nelder.sort()
		ax = nelder[6][1]
		ay = nelder[6][2]
		bx = nelder[0][1]
		by = nelder[0][2]
	return [bx, by, f(bx, by)]



def hillClimbGrid():
	global START
	START = clock()
	best = [float('inf'), float('inf'), float('inf')]
	for (x,y) in createGenerator():
		best = compareSurroundingPts(NEIGHBORS, best, x, y)
	return best

def createLookUpTable(): 
	for t in frange (0, 2*pi, 2*pi/NEIGHBORS):
		costable.append(RADIUS*cos(t))
		sintable.append(RADIUS*sin(t))
	assert(len(costable) == 64)

def randomPoints(points):
	from random import random
	pts = []
	for n in range(points):
		x = random()*MAX_X
		y = random()*MAX_Y
		pts.append((x,y))
	return pts

def compareSurroundingPts(points, best, x, y):
	for t in frange (0, 2*pi, 2*pi/NEIGHBORS):
		trialX = x + RADIUS*cos(t)
		trialY = y + RADIUS*sin(t)
		trialF = f(trialX, trialY)
		if trialF < best[2]:
			best[0] = trialX
			best[1] = trialY
			best[2] = trialF
	return best

def compareSurroundingPtsRandom(points, best, x, y):
	for t in frange (0, 2*pi, 2*pi/NEIGHBORS):
		trialX = random()*10
		trialY = random()*10
		trialF = f(trialX, trialY)
		if trialF < best[2]:
			best[0] = trialX
			best[1] = trialY
			best[2] = trialF
	return best

def createGenerator():
	for x in range(0, MAX_X):
		for y in range(0, MAX_Y):
			yield(x, y)


def compareSurroundingPtsLookUpTable(points, best, x, y):
	for t in frange (0, NEIGHBORS, 1):
		trialX = x + costable[t]
		trialY = y + sintable[t]
		trialF = f(trialX, trialY)
		if trialF < best[2]:
			best[0] = trialX
			best[1] = trialY
			best[2] = trialF
	return best

def compareSurroundingPtsGrid(points, best, x, y):
	for t in frange (0, NEIGHBORS, 1):
		trialX = x + costable[t]
		trialY = y + sintable[t]
		trialF = f(trialX, trialY)
		if trialF < best[2]:
			best[0] = trialX
			best[1] = trialY
			best[2] = trialF
	return best

def printBestList(best):
	print ('x: ', round(best[0], 2) )
	print ('y: ', round(best[1], 2) )
	print ('f: ', round(best[2], 2) )


from time import clock; START_TIME = clock(); main();
print (' | %5.6f seconds |' %(clock()-START_TIME))

'''

f(x,y) = z = x*sin(4*) + 1.1*y*sin(2*y)
with 0 <= x <= 10 and 0 <= y <= 10

'''