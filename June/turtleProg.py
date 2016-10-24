from math import sin, cos, pi
from turtle import *
from time import sleep 
from random import random, randint
from math import sqrt
from copy import deepcopy 
from time import clock

def main(): 
	r = 100
	radians()
	MAX = 2*pi
	t = 0
	bgcolor("BLACK")
	color('WHITE')
	width(2)
	speed(10000000)
	#drawLine(-100, -100, 100, 100)
	#circlexy(0, 0, 20)
	polygon(0, 0, 200)
	sleep(100)

def circlexy(x, y, r): 
	r = abs(r)
	up()
	goto(x+r, y)
	setheading(90)
	down()
	circle(r)

def nephroid(r): 
	circle(r)
	for theta in range(360): 
		x = r * cos(theta * (pi/180))
		y = r * sin(theta * (pi/180))
		circlexy(x, y, x)

def cardiod(x, y, r): 
	circlexy(x, y, r)
	for theta in range(360): 
		x = r * cos(theta * (pi/180))
		y = r * sin(theta * (pi/180))
		radius = sqrt((x-r)**2 + y**2)
		circlexy(x, y, radius)

def polygon(x, y, r): 
	#circlexy(x, y, 200)
	lst = []
	n = 15
	thetaLst = [(360/n)*t for t in range(n)]
	for theta in thetaLst:
		t = theta * (pi/180)
		x = r * cos(t)
		y = r * sin(t)
		lst.append([x, y])
	for n1 in range(len(lst)): 
		for n2 in range(len(lst)): 
			drawLine(lst[n1][0], lst[n1][1], lst[n2][0], lst[n2][1])

def drawLine(a, b, c, d): 
	up()
	goto(a, b)
	down()
	goto(c, d)

main()

