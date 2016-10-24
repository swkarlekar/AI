##########################
# Sweta Karlekar         #
# Period 4               #
# Neural Network         #
# May 21st, 2015         #
##########################
from random import random, choice, uniform, shuffle, randint
from math import exp
INPUTS = [[1, 0, 0, 0, 0, 0, 0, 0, -1], [0, 1, 0, 0, 0, 0, 0, 0, -1], [0, 0, 1, 0, 0, 0, 0, 0, -1], [0, 0, 0, 1, 0, 0, 0, 0, -1], [0, 0, 0, 0, 1, 0, 0, 0, -1], [0, 0, 0, 0, 0, 1, 0, 0, -1], [0, 0, 0, 0, 0, 0, 1, 0, -1], [0, 0, 0, 0, 0, 0, 0, 1, -1],]
TRIALS = 9000
ALPHA = 0.25
SMALL = 0.4
LENGTH = 3

def main(): 
	epochs, w, v = trainNetwork()
	verifyNetwork(epochs, w, v)

def verifyNetwork(epochs, w, v):
	print('Results of Neural Network Back Propagation: ')
	print('Epochs =', epochs)
	pos = 0
	for x in INPUTS:
		t = x[pos]
		dp, h, DP, y = feedForward(x, w, v)
		y = [int(element>.5) for element in y]
		print(('%5s'% ((int(x[pos] > 0.5)) ==t), '-->', [x[i] for i in range(len(y)-1)], x))
		pos+=1
 #----------------------------------------------------------------------------------------
def randomlyAssignWeights():
	w = [[uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), ] for row in range(9)]
	v = [[uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), uniform(-2, 2), uniform(-2, 2)] for row in range(4)]

	#w = [[ 0.1, -0.2, 0.3,], [0.4, 0.1, 0.1,], [0.3, 0.3, 0.7,], [0.6, 0.7, -0.8,], [-0.5, 0.4, 0.2,], [0.1, 0.5, 0.5,], [0.4, 0.6, 0.3,], [0.2, 0.9, -0.1,], [-0.4, -0.1, 0.6]]
	#v = [[0.4, -0.8, 0.2, 0.6, 0.7, -0.5, 0.2, -0.4,], [0.9, 0.7, 0.3, 0.2, -0.1, 0.6, 0.4, -0.8,], [0.1, 0.2, 0.7, -0.8, 0.5, 0.4, 0.1, 0.1,], [0.9, 0.1, 0.8, -0.4, 0.2, 0.7, -0.3, 0.8,],]

	return w, v
#----------------------------------------------------------------------------------------
def printAllData(w, h, v, y): 
	pass
#----------------------------------------------------------------------------------------
def f(x):
	return 1/(1 + exp(-x))
#----------------------------------------------------------------------------------------
def feedForward(x, w, v): 
	dp = mult(x, w)
	h = [ f(x) for x in dp] + [-1]
	DP = mult(h, v)
	y = [ f(x) for x in DP] 
	#print('h = ', h)
	return dp, h, DP, y
#----------------------------------------------------------------------------------------
def backPropagation(x, w, dp, h, v, DP, y, wIncs, vIncs):
	delta = [(y[r]-x[r])*y[r]*(1-y[r]) for r in range(len(w)-1)]

	for j in range(len(v)):
		for k in range(len(v[0])):
			vIncs[j][k] = delta[k]*h[j]

	for i in range(len(w)):
		item = [] 
		for j in range(len(w[0])):
			deltaSum = delta[0]*v[j][0] + delta[1]*v[j][1] + delta[2]*v[j][2] + delta[3]*v[j][3] + delta[4]*v[j][4] + delta[5]*v[j][5] + delta[6]*v[j][6] + delta[7]*v[j][7]
			wIncs[i][j] += deltaSum*h[j]*(1-h[j])*x[i]
	
	return wIncs, vIncs
#----------------------------------------------------------------------------------------
def trainNetwork():
	epochs = 0
	w, v = randomlyAssignWeights()
	trained = False
	while epochs < TRIALS and not trained: 
		wIncs = [[0 for c in range(len(w[0]))] for r in range(len(w))]
		vIncs = [[0 for c in range(len(v[0]))] for r in range(len(v))]
		for x in INPUTS: 
			dp, h, DP, y = feedForward(x, w, v)
			E = sum([.5*pow((y[i]-x[i]),2) for i in range(len(y))])
			for k in range(7):
				if int(y[k] > 0.5) != x and E > .02:
					trained = False
				else: 
					trained = True
					break
			wIncs, vIncs = backPropagation(x, w, dp, h, v, DP, y, wIncs, vIncs)
		

		#for r in range(len(y)):
			#print(round(y[r], 0), end = " ")
		#print()

		for row in range(len(w)):
			for col in range(len(w[0])):
				w[row][col] -= ALPHA*wIncs[row][col]

		for row in range(len(v)):
			for col in range(len(v[0])):
				v[row][col] -= ALPHA*vIncs[row][col]
		
		epochs += 1
		if epochs % 100 == 0:
			print('Epochs= ', epochs, '    Error: ', E)
		
		


	print("Trained? ", trained)

	e = sum([.5*pow((y[i]-x[i]),2) for i in range(len(y))])
	print('e', e)
	

	return epochs, w, v
#----------------------------------------------------------------------------------------
def mult(v, m): 
	assert len(v) == len(m), [len(v), len(m)]
	return [sum([v[i]*m[i][j] for i in range (len(v))]) for j in range(len(m[0]))]
#----------------------------------------------------------------------------------------
def yValue(x, w, v): 
	h = [0, 0, -1]
	h[0] = int( (w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
	h[1] = int( (w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
	y = int( (v[0]*h[0] + v[1]*h[1] + v[2]*h[2]) > 0)
	return y 
#----------------------------------------------------------------------------------------
def trained(w, v):
	for x in INPUTS: 
		dp, h, DP, y = feedFoward(x, w, v) 
		if E(y, x) != 0: 
			return False
	return True
#----------------------------------------------------------------------------------------
def intializeWeights(): 
	w = [[random()*2*choice([-1, 1]) for y in range(3)] for x in range(9)]
	v = [[random()*2*choice([-1, 1]) for y in range(8)] for x in range(4)]
	return w, v
#----------------------------------------------------------------------------------------
def improveWeights(w, v): 
	return w, v
#----------------------------------------------------------------------------------------
#def verifyNetwork(y, t): 
	#print('E = ', E(y, t))
#----------------------------------------------------------------------------------------
def E(y, t): 
	error = 0
	for n in range(0, 8):
		error += 0.5*(y[n] - t[n])**2
	return error
#----------------------------------------------------------------------------------------
def trainPerceptronsWeights():
	w = []
	for x in range(LENGTH):
		w.append(uniform(-1.0, 1.0))
	epochs = 0
	copy = INPUTS
	while not trained(w) and epochs < TRIALS:
		shuffle(copy)
		for x in copy:
			t = x[LENGTH]
			y = f(w, x)
			if f(w, x) != t:
				for n in range(LENGTH):
					w[n] = w[n] - alpha*(y-t)*x[n]
		epochs +=1 
	return w, epochs
#----------------------------------------------------------------------------------------
if __name__ == '__main__': from time import clock; START_TIME = clock(); main();
print("--> Run Time = ", round(clock() - START_TIME, 2), 'seconds <--\n'); 
#----------------------------------------------------------------------------------------
