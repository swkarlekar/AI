def main(): 
	lst = [1, 0, 3, 0, 9, 2]
	kk = []
	for x in range(1000):
		kk.append(lst[findProbableIndex(lst)])
	count9 = kk.count(9)
	count3 = kk.count(3)
	count1 = kk.count(1)
	count2 = kk.count(2)
	print('9:', round(count9/1000 * 100, 2), round(9/15*100, 2))
	print('3:', round(count3/1000 * 100, 2), round(3/15*100, 2))

def findProbableIndex(moves):
	lst = [0]
	for x in range(len(moves)): 
		lst.append(moves[x]/(sum(moves)))
	rand = random()
	for x in range(1, len(lst)): 
		if sum(lst[0:x]) < rand < sum(lst[0:x+1]): return x-1

from random import random
main()