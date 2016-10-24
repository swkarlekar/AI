##########################
# Sweta Karlekar         #
# Period 4               #
# Neural Network         #
# May 21st, 2015         #
##########################
from random import random, choice, uniform, shuffle

#INPUTS = [(0, 0, -1, 0), (0, 1, -1, 1), (1, 0, -1, 1), (1, 1, -1, 1)]
#INPUTS = [(0, 0, 1, -1, 0), (0, 1, 0, -1, 1), (1, 0, 0, -1, 1), (1, 1, 1, -1, 0)]
INPUTS = [(0, 4, -1, 0), (4, 0, -1, 0), (2.1, 2.1, -1, 1),]
TEST = INPUTS + [(4.1, 0, -1, 1), (0, 4.1, -1, 1)]
TRIALS = 30000
alpha = 0.25
SMALL = 0.4
LENGTH = 3

def main(): 
	w, epochs = trainPerceptronsWeights()
	verifyNetwork(w, epochs)
#----------------------------------------------------------------------------------------
def f(w, x): 
	#return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2] + w[3]*x[3]) > 0)
	return int((w[0]*x[0] + w[1]*x[1] + w[2]*x[2]) > 0)
#----------------------------------------------------------------------------------------
def yValue(x, w, v): 
	h = [0, 0, -1]
	h[0] = int( (w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
	h[1] = int( (w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
	y = int( (v[0]*h[0] + v[1]*h[1] + v[2]*h[2]) > 0)
	return y 
#----------------------------------------------------------------------------------------
def trained(w): 
	for x in INPUTS: 
		if f(w, x) != x[LENGTH]:
			return False
	return True
#----------------------------------------------------------------------------------------
def intializeWeights(): 
	w = random()
	[[-1, 1,], [-1, 1,], [-1.5, 0.5,],]
	v = [1, 1, 1.5]
	return w, v
#----------------------------------------------------------------------------------------
def improveWeights(w, v): 
	return w, v
#----------------------------------------------------------------------------------------
def trainNetwork(): 
	epochs = 0
	h = [0, 0, -1]
	w, v = initializeWeights()
	while epochs < TRIALS and not trained(w, v): 
		x = choice(INPUTS)
		w, v, = improveWeights(W, V)
		h[0] = int((w[0][0]*x[0] + w[1][0]*x[1] + w[2][0]*x[2]) > 0)
		h[1] = int((w[0][1]*x[0] + w[1][1]*x[1] + w[2][1]*x[2]) > 0)
		epoches += 1
	return epochs, w, v
#----------------------------------------------------------------------------------------
def verifyNetwork(w, epochs): 
	'''
	print('\nEpochs =', epochs)
	print(["---FAILURE---", "---SUCCESS---"][trained(w)])
	for x in INPUTS: 
		print(f(w,x) == x[LENGTH], f(w, x), x)
	#print(-w[0]/w[1], w[2]/w[1])
	'''
	print('\nEpochs =', epochs)
	for x in INPUTS: 
		t = x[3]
		y = yValue(x, w, v)
		print('%5s'% (y==t), '-->', yValue(x, w, v), x)
	print('\n=== STATISTICS ====')
	print(' x = %2d, %2d, %2d, %2d'%(x[0], x[1], x[2], x[3]))
	print(' w = %5.2f, %5.2f'%(w[0][0], w[0][1]))
	print(' %5.2f, %5.2f'%(w[1][0], w[1][1]))
	print(' %5.2f, %5.2f'%(w[2][0], w[2][1]))
	print(' v = %5.2f, %5.2f, %5.2f'%(v[0], v[1], v[2]))
	print(' y =', y)
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
