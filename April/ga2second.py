POP = 200
NUMGENES = 20
NUMTIMES = 0
MINFITNESS = 0
from random import choice, randint
from math import sin, cos

def main(): 
	pop = createPopulation()
	print('\nMinimum Fitness Value\n')
	pop = genAlgo(pop)
	global NUMTIMES
	while not isHomo(pop):
		pop = genAlgo(pop)
		NUMTIMES+=1
	print(MINFITNESS,'\n')
	print(NUMTIMES)

def createPopulation(): 
	return [[0,''.join([str(randint(0, 1)) for c in range(NUMGENES)])] for r in range(POP)]

def fitness(lst):
	for k in range(len(lst)):
		st = lst[k][1]
		H = len(st)//2
		x = scaleNum(int(st[0:H], 2))
		y = scaleNum(int(st[H:], 2))
		lst[k][0] = x*sin(4*x) + 1.1*y*sin(2*y)
	lst.sort()

def isHomo(lst): 
	for r in range(len(lst)-1): 
		if lst[r][1] != lst[r+1][1]:
			return False
	return True

def genAlgo(lst): 
	global NUMTIMES
	NUMTIMES += 1
	fitness(lst)
	parent1 = lst[0][1]
	global MINFITNESS
	MINFITNESS = lst[0][0]
	newpop = []
	for index in range(1, POP//2): 
		parent2 = lst[index][1]
		crossover = randint(1, NUMGENES)
		offspring1 = parent1[0:crossover]+parent2[crossover:]
		offspring2 = parent2[0:crossover]+parent1[crossover:]
		newpop.append([0, offspring1])
		newpop.append([0, offspring2])
	return newpop

def scaleNum(x):
	return float(x*10)/1023

if __name__ == '__main__': 
	from time import clock; START_TIME = clock();main();
	print (' | %5.2f seconds |' %(clock()-START_TIME))
