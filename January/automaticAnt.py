def setUpCanvas(root):
	root.title("THE AUTOMATIC ANT by Sweta Karlekar.")
	canvas = Canvas(root, width = root.winfo_screenwidth(), height = root.winfo_screenheight(), bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def placeFrameAroundWindow():
	canvas.create_rectangle(5, 5, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, outline = 'GOLD')

def displayStatistics(startTime):
	elaspedTime = round(clock()-startTime, 2)
	speedPerThousand = round(1000*elaspedTime/STEPS, 2)
	print('+================< Automated Ant Student >===================+')
	print('| ANT MOVES = ', STEPS, 'steps.                                  |')
	print('| RUN TIME = %6.2f'% elaspedTime,         'seconds.              |')
	print('| SPEED = %6.2f'% speedPerThousand,      'seconds-per-1000-moves.            |')
	print('+============================================================+')
	message = 'PROGRAM DONE. Final image is' + str(STEPS) + 'ant moves in ' + str(elaspedTime) + ' seconds.'
	root.title(message)

def displayMatrix(matrix): 
	print('---MATRIX:')
	for row in matrix: 
		[print(x, ' ', end = ' ') for x in row]
		print()
	print('    =============================================')

def plot(x, y, color = 'WHITE'):
	canvas.create_rectangle(x, y, x+5, y+5, width = 1, fill = color)

def createPixelWorld():
	ROW = SCREEN_HEIGHT + 5
	COL = SCREEN_WIDTH + 5

	matrix = [[0 for c in range(COL)] 
				for r in range(ROW)]
	
	placeFrameAroundWindow()
	canvas.create_line(0, 0, SCREEN_WIDTH, SCREEN_HEIGHT, width = 1, fill = 'RED')
	ant = [0, ANT_START_ROW, ANT_START_COL]
	return ant, matrix

def move(ant): 
	direction = ant[0]
	if direction == 0: 
		ant[2] -= 5
	if direction == 1: 
		ant[1] -= 5
	if direction == 2: 
		ant[2] += 5
	if direction == 3: 
		ant[1] += 5

	if ant[1] > SCREEN_WIDTH:
		ant[1] = 5
	if ant[1] < 5:
		ant[1] = SCREEN_WIDTH

	if ant[2] > SCREEN_HEIGHT:
		ant[2] = 5
	if ant[2] < 5: 
		ant[2] = SCREEN_HEIGHT
	return ant

def modifyColors(ant, matrix):
	#pass
	c = ant[1]
	r = ant[2]
	color = matrix[r][c]
	if color == 0 or color == 3: 
		ant[0] += 1 #turns left
		if ant[0] == 4: ant[0] = 0
	else: 
		ant[0] -= 1 #turns right
		if ant[0] == -1: ant[0] = 3
	matrix[r][c] += 1
	if matrix[r][c] >= len(COLORS):
		matrix[r][c] = 0
	plot(ant[1], ant[2], COLORS[matrix[r][c]])

def makeTheAntsJourney(ant, matrix):
	message = 'PROGRAM CURRENTLY RUNNING ' + str(STEPS) + ' ant moves in ' + str(SPEED_INC) + ' increments.'
	print(message)
	root.title(message)
	startTime = clock()
	for n in range(STEPS):
		move(ant)
		modifyColors(ant, matrix)
		if n% SPEED_INC == 0: 
			canvas.update()
	canvas.update()
	displayStatistics(startTime)

from tkinter import Tk, Canvas, YES, BOTH
from time import clock
from random import choice
root = Tk()
canvas = setUpCanvas(root)
SCREEN_WIDTH = root.winfo_screenwidth()//5*5 - 15
SCREEN_HEIGHT = root.winfo_screenheight()//5*5 -90
ANT_START_ROW = SCREEN_WIDTH//(5*2) *5
ANT_START_COL = SCREEN_HEIGHT//(5*2) *5
STEPS = 20000
SPEED_INC = 20
COLORS = ('MAGENTA', 'BLUE', 'CYAN', 'RED') #('WHITE', 'RED', 'BLUE', 'YELLOW',) 
HEADING_RULE = (0, 1)
assert len(HEADING_RULE) < len(COLORS)
NUMBER_OF_COLORS = len(HEADING_RULE)

def main():
	ant, matrix = createPixelWorld()
	makeTheAntsJourney(ant, matrix)
	root.mainloop()

if __name__ == '__main__': main()