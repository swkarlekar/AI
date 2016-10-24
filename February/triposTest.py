##########################
# Sweta Karlekar         #
# Period 4               #
# Tripos Test			 #
# February 16th, 2015    #
##########################

trials = 10000000
from random import random,  uniform

def main():
	print("Tripos Test:")
	print("Puzzle 1 answer: ", round(puzzle1()/trials, 3))
	print("Puzzle 2 answer: ", round(puzzle2()/trials, 3))
	print("Puzzle 3 answer: ", round(puzzle3()/trials, 3))
	print("Puzzle 4 answer: ", round(puzzle4()/trials, 3))

def puzzle1(): 
	breaks = [0, 0]
	triangles = 0
	for n in range(trials):
		breaks[0] = random()
		breaks[1] = random()
		if checkIfTriangle(breaks): triangles+=1
	return triangles
	
def puzzle2(): 
	breaks = [0, 0]
	triangles = 0
	for n in range(trials):
		breaks[0] = random()
		if breaks[0] <= 0.5:
			breaks[1] = uniform(breaks[0], 1)
		else: breaks[1] = uniform(0, breaks[0])
		if checkIfTriangle(breaks): triangles+=1
	return triangles

def puzzle3(): 
	breaks = [0, 0]
	triangles = 0
	for n in range(trials):
		breaks[0] = random()
		if random() <= 0.5:
			breaks[1] = uniform(0, breaks[0])
		else: breaks[1] = uniform(breaks[0], 1)
		if checkIfTriangle(breaks): triangles+=1
	return triangles
	
def puzzle4(): 
	breaks = [0, 0]
	triangles = 0
	for n in range(trials):
		breaks[0] = random()
		if random() <= breaks[0]:
			breaks[1] = uniform(0, breaks[0])
		else: breaks[1] = uniform(breaks[0], 1)
		if checkIfTriangle(breaks): triangles+=1
	return triangles

def checkIfTriangle(lst):
	lst.sort()
	x1 = lst[0]
	x2 = lst[1] - lst[0]
	x3 = 1 - lst[1]
	if max(x1, x2, x3) < 0.5: 
		return True

if __name__ == '__main__': 
	from time import clock; START_TIME = clock();main();
	print (' | %5.2f seconds |' %(clock()-START_TIME))
   
#######OUTPUT########
#Tripos Test:
#Puzzle 1 answer:  0.25
#Puzzle 2 answer:  0.386
#Puzzle 3 answer:  0.193
#Puzzle 4 answer:  0.25
# | 64.64 seconds |
#####################