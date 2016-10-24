def setUpCanvas(root): 
	root.title("Wolfram's cellular automata: A Tk/Python Graphics Program")
	canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def displayStatistics():
	print('RUN TIME = %6.2F'% round(clock()-START_TIME, 2), 'seconds.')
	root.title('THE FRACTAL FLOWER IS COMPLETE.')

def frange(start, stop, step):
	i = start
	while i < stop: 
		yield i
		i+= step

def line(x1, y1, x2, y2, kolor = 'WHITE', width = 1): #you need to place a for loop in this function
	canvas.create_line(x1, y1, x2, y2, width = width, fill = kolor)

def drawFlower(cx, cy, radius): #make this recursive
	#base case
	if radius < 3:
		return
	#set color
	kolor = 'GREEN'
	width = 2
	if radius <240:
		kolor = 'WHITE'
		width = 1
	if radius < 10: 
		kolor = 'RED'
		width = 1
	#draw flower
	for t in frange(0, 6.28, 0.9):
		cx1 = cx
		cy1 = cy
		for k in range(7):
			if random() < 0.2:
				t+=0.2
			else: t-=0.2
			x = cx1 + radius/7*sin(t)
			y = cy1 + radius/7*cos(t)
			line(cx1, cy1, x, y, kolor, width)
			cx1 = x
			cy1 = y
		drawFlower(x, y, radius/3)
	canvas.update()

from tkinter import Tk, Canvas, BOTH, YES 
from math import sin, cos, atan2, pi, hypot
from random import random
from time import clock
root = Tk()
canvas = setUpCanvas(root)
WIDTH = root.winfo_screenwidth()
HEIGHT = root.winfo_screenheight()
START_TIME = clock()

def main():
	drawFlower(WIDTH/2, HEIGHT/2-50, 240)
	displayStatistics()
	canvas.update()
	root.mainloop()

if __name__ == '__main__': main()