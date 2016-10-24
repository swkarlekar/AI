POP = 12
NUMGENES = 10
NUMTIMES = 0
from random import choice, randint

def main(): 
	pop = createPopulation()
	print('\nOriginial Population\n')
	printPopulation(pop)
	while not isHomo(pop):
		pop = randomMating(pop)
	print('\nHomogenous Artificially Selected Population\n')
	printPopulation(pop)
	print("Number of generations:", NUMTIMES)

def createPopulation(): 
	lst = []
	lst = [[choice([0,1]) for y in range(NUMGENES)] for x in range(POP)]
	return lst

def fitness(lst):
	for x in range(len(lst)):
		lst[x].insert(0, sum(lst[x]))
	lst.sort()
	lst.reverse()

def isHomo(lst): 
	for r in range(len(lst)-1): 
		if lst[r] != lst[r+1]:
			return False
	return True

def randomMating(lst): 
	global NUMTIMES
	NUMTIMES += 1
	fitness(lst)
	parent1 = lst[0]
	newpop = []
	for index in range(1, 7): 
		parent2 = lst[index]
		crossover = randint(1, 9)
		offspring1 = parent1[1:crossover]+parent2[crossover:]
		offspring2 = parent2[1:crossover]+parent1[crossover:]
		newpop.append(offspring1)
		newpop.append(offspring2)
	return newpop

def printPopulation(pop):
	for ind in range(POP): 
		print("Individual", ind+1, end = '\t')
		for gene in range(NUMGENES):
			print(pop[ind][gene], end = ' ')
		print()
	print()

if __name__ == '__main__': 
	from time import clock; START_TIME = clock();main();
	print (' | %5.2f seconds |' %(clock()-START_TIME))
