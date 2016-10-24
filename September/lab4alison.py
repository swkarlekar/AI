'''
+-----------------------------------+
|	Alison Hau, pd 2, 9/22/14		|
|									|
|	Use the A* algorithm to make a 	|
|	word ladder. 					|
|									|
+-----------------------------------+
'''
import pickle
import copy
def main():	
	filename = open('words.txt', 'rb')
	lst = list(filename)
	for n in range(len(lst)-1):
		lst[n] = lst[n].strip()

	savefile = open('dict.txt', 'rb')
	Dict = pickle.load(savefile)
	savefile.close()

	startWord = ensureSixLetters(input('Start word?  '))
	targetWord = ensureSixLetters(input('End word?  '))

	print('\nForward:  %s ----> %s' % (startWord, targetWord))
	path, num = astar(Dict, startWord, targetWord, lst)
	printListPretty(path)
	print ('Pops:  ' + str(num))

	print('\nReverse:  %s ----> %s' % (targetWord, startWord))
	path, num = astar(Dict, targetWord, startWord, lst)
	printListPretty(path)
	print ('Pops:  ' + str(num))

#----------------------------------------------------------------------------
def printListPretty(list):
	count = 1
	for word in list:
		print ('\t'+str(count)+'. '+ word)
		count = count+1
#----------------------------------------------------------------------------
def ensureSixLetters(word):
	while len(word) != 6:
		word = input('Please entar a six letter word:  ')
	return word
#----------------------------------------------------------------------------
def astar(Dict, start, end, lst):
	startnode = (0, start, [], 0)
	goadnode = ()
	priorityQ = []
	priorityQ.append(startnode)	# tuple: (g+h, name, path from room, dist from start (g))
	print ('Getting path...')

	closedDict = {}	# for nodes and their g values
	popcount = 0

	# q.sort() sorts least to greatest
	while priorityQ:
		(fVal, name, path, gVal) = priorityQ.pop(0)
		popcount += 1
		if name == end:
			path.append(name)
			return path, popcount
		closedDict[name] = gVal
		for child in Dict[name]:
			cpath = path + [name]
			newg = len(cpath)
			temptuple = (newg + heur(child, end), child, cpath, newg)
			if child in closedDict:
				if closedDict[child] > newg:
					del closedDict[child]
					priorityQ.append(temptuple)
			elif sortQueue(lst, priorityQ, child):
				priorityQ.append(temptuple)
				closedDict[child] = newg
			else:
				a = sortQueue(priorityQ, child)
				if priorityQ[a][3] > newg:
					priorityQ.remove(priorityQ[a])
					priorityQ.append(temptuple)
		priorityQ.sort()
#----------------------------------------------------------------------------
def heur(start, end):
	return sum([end[n] != start[n] for n in range (6)])
#----------------------------------------------------------------------------
def sortQueue(lst, pq, target): 
	there = -1
	for i in range(len(pq)): 
		if lst[i][1] == target:
			there = i
	return there
#----------------------------------------------------------------------------
from time import clock; START_TIME = clock(); main();
print (' | %5.2f seconds |' %(clock()-START_TIME))