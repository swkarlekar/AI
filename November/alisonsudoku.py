'''
+---------------------------------------+
|		Alison Hau, pd. 2, 11/20		|
+---------------------------------------+
'''
MAX = 9

def main():
	print("Original Board")
	matrix = createMatrix()
	displayTheSudokuBoard(matrix)
	print("Solved Board")
	matrix = recursivelySolveTheSudoku(matrix)
	displayTheSudokuBoard(matrix)
	if solutionIsCorrect(matrix):
		print("Board Verified")
	else:
		print("Wrong Solution")
#-----------------------------------------------------------------------------------
def displayTheSudokuBoard(matrix):
	for row in matrix:
		for col in row:
			tmp = col.value
			if len(tmp) == 1:
				print(' '+str(next(iter(tmp)))+' ', end = '')
			else:
				print(' 0 ', end = '')
		print('')
	print('')
#-----------------------------------------------------------------------------------
class Cell(object):
	matrix = None
	def __init__(self, val, r, c, matrix):
		if val != 0:
			self.value = {val,}
		else:
			self.value = {1,2,3,4,5,6,7,8,9}
		self.row = r
		self.col = c
		self.block = self.blockNumber(r,c)
		Cell.matrix = matrix
	def blockNumber(self, row, col):
		if 		(self.row < 3) and 		(self.col < 3): return 0
		if 		(self.row < 3) and 	(2 < self.col < 6): return 1
		if 		(self.row < 3) and 	(5 < self.col): 	return 2
		if 	(2 < self.row < 6) and 		(self.col < 3): return 3
		if 	(2 < self.row < 6) and 	(2 < self.col < 6): return 4
		if 	(2 < self.row < 6) and 	(5 < self.col): 	return 5
		if 		(self.row > 5) and 		(self.col < 3): return 6
		if 		(self.row > 5) and 	(2 < self.col < 6): return 7
		if 		(self.row > 5) and 	(5 < self.col): 	return 8
#-----------------------------------------------------------------------------------
def createMatrix():
	'''
	M = [ [4,8,1,5,0,9,6,7,0,],
			[3,0,0,8,1,6,0,0,2,],
			[5,0,0,7,0,3,0,0,8,],
			[2,0,0,0,0,0,0,0,9,],
			[9,0,0,0,0,0,0,0,1,],
			[8,0,0,0,0,0,0,0,4,],
			[0,3,9,2,7,5,4,8,0,],
			[6,0,0,0,0,0,9,2,7,],
			[7,0,0,0,0,0,3,1,0,],]
	'''
	M = [	[8, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 3, 6, 0, 0, 0, 0, 0], 
			[0, 7, 0, 0, 9, 0, 2, 0, 0], 
			[0, 5, 0, 0, 0, 7, 0, 0, 0], 
			[0, 0, 0, 0, 4, 5, 7, 0, 0], 
			[0, 0, 0, 1, 0, 0, 0, 3, 0], 
			[0, 0, 1, 0, 0, 0, 0, 6, 8], 
			[0, 0, 8, 5, 0, 0, 0, 1, 0],
			[0, 9, 0, 0, 0, 0, 4, 0, 0], ]
	# M = [[1,0,2,3,4,5,7,8,9,],
	# 	[9,0,0,0,5,0,0,0,0,],
	# 	[2,0,0,0,7,0,0,0,0,],
	# 	[6,0,0,0,1,0,0,0,0,],
	# 	[8,0,0,0,2,0,0,0,0,],
	# 	[0,0,0,0,6,0,0,0,0,],
	# 	[4,0,0,0,0,0,0,0,0,],
	# 	[3,0,0,0,9,0,0,0,0,],
	# 	[5,0,0,0,8,0,0,0,0,],]

	# M = [[7,2,3,8,4,6,1,5,9,],
	# 	[6,1,5,3,9,2,4,7,8,],
	# 	[8,4,9,7,1,5,6,3,2,],
	# 	[3,7,8,6,5,4,9,2,1,],
	# 	[1,9,4,2,8,7,3,6,5,],
	# 	[2,5,6,9,3,1,8,4,7,],
	# 	[5,6,1,4,7,9,2,8,3,],
	# 	[4,8,7,1,2,3,5,9,6,],
	# 	[9,3,2,5,6,8,7,1,4,],]

	# M = [[1,3,2,4,7,0,6,8,9,],
	# 	 [0,5,6,0,0,0,0,0,0,],
	# 	 [4,8,9,0,0,0,0,0,0,],
	# 	 [7,0,0,1,9,3,0,0,0,],
	# 	 [9,0,0,6,2,4,0,0,0,],
	# 	 [6,0,0,5,0,7,0,0,0,],
	# 	 [8,0,0,0,0,0,2,5,1,],
	# 	 [5,0,0,0,0,0,3,0,7,],
	# 	 [2,0,0,0,0,0,9,6,4,],]

	# M = [[7,2,3,0,4,6,1,5,9,],
	# 	 [6,0,5,3,9,2,4,7,8,],
	# 	 [8,4,0,7,1,5,6,3,2,],
	# 	 [3,7,8,6,5,4,9,2,0,],
	# 	 [1,9,4,2,8,7,3,0,5,],
	# 	 [2,5,6,9,3,0,0,0,0,],
	# 	 [5,6,1,4,0,0,2,8,3,],
	# 	 [4,8,7,1,2,0,0,9,6,],
	# 	 [0,3,2,5,6,0,7,1,4,],]

	matrix = []
	for r in range(MAX):
		row = []
		for c in range(MAX):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	return matrix
#-----------------------------------------------------------------------------------
def restoreValues(matrix, oldMatrix):
	for r in range(MAX):
		for c in range(MAX):
			matrix[r][c].value = oldMatrix[r][c].value
	return matrix
#-----------------------------------------------------------------------------------
def recursivelySolveTheSudoku(matrix):
	matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
	if badMatrix(matrix) or solutionIsCorrect(matrix):
		return matrix
	oldMatrix = deepcopy(matrix)
	r, c = coordinatesofCellWithSmallestValueSet(matrix)
	for guess in matrix[r][c].value:
		matrix[r][c].value = {guess,}
		matrix = recursivelySolveTheSudoku(matrix)
		if solutionIsCorrect(matrix):
			return matrix
		matrix = restoreValues(matrix, oldMatrix)
	return matrix
#-----------------------------------------------------------------------------------
def coordinatesofCellWithSmallestValueSet(matrix):
	minr = 0
	minc = 0
	minlen = 9
	for r in range(MAX):
		for c in range(MAX):
			if 2 <= len(matrix[r][c].value) and len(matrix[r][c].value) < minlen:
				minlen = len(matrix[r][c].value)
				minr = r
				minc = c
	return minr, minc
#-----------------------------------------------------------------------------------
def trickOneRows(matrix):
	changesMade = False
	oldmatrix = deepcopy(matrix)
	for r in range(MAX):
		row = set()
		for c in range(MAX):
			if len(matrix[r][c].value) == 1:
				temp = row | (matrix[r][c].value)
				row = temp
		for c in range(MAX):
			if len(matrix[r][c].value) > 1:
				matrix[r][c].value = matrix[r][c].value - row
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True

	return matrix, changesMade
#-----------------------------------------------------------------------------------
def trickOneCols(matrix):
	changesMade = False
	oldmatrix = deepcopy(matrix)
	for c in range(MAX):
		col = set()
		for r in range(MAX):
			if len(matrix[r][c].value) == 1:
				temp = col | (matrix[r][c].value)
				col = temp
		for r in range(MAX):
			if len(matrix[r][c].value) > 1:
				matrix[r][c].value = matrix[r][c].value - col
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True
	return matrix, changesMade
#-----------------------------------------------------------------------------------
def trickOneBlocks(matrix):
	changesMade = False
	oldmatrix = deepcopy(matrix)
	blocks = makeBlockList(matrix)

	for block in range(MAX):
		bl = set()
		for cell in range(MAX):
			if len(blocks[block][cell].value) == 1:
				tmp = bl | (blocks[block][cell].value)
				bl = tmp
		for cell in range(MAX):
			if len(blocks[block][cell].value) > 1:
				blocks[block][cell].value = blocks[block][cell].value - bl
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True
	return matrix, changesMade
#-----------------------------------------------------------------------------------
def trickTwoRows(matrix):
	changesMade = False
	oldmatrix = deepcopy(matrix)
	for r in range(MAX):
		row = []
		for c in range(MAX):
			if len(matrix[r][c].value) > 1:
				tmp = set()
				while len(matrix[r][c].value) > 0:
					a = matrix[r][c].value.pop()
					row.append(a)
					tmp = tmp | {a}
				matrix[r][c].value = tmp
		for c in range(MAX):
			if len(matrix[r][c].value) > 1:
				for poss in matrix[r][c].value:
					if row.count(poss) == 1:
						matrix[r][c].value = {poss}
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True
	return matrix, changesMade
#-----------------------------------------------------------------------------------
def trickTwoCols(matrix):
	changesMade = False
	oldmatrix = deepcopy(matrix)
	for c in range(MAX):
		col = []
		for r in range(MAX):
			if len(matrix[r][c].value) > 1:
				tmp = set()
				while len(matrix[r][c].value) > 0:
					a = matrix[r][c].value.pop()
					col.append(a)
					tmp = tmp | {a}
				matrix[r][c].value = tmp
		for r in range(MAX):
			if len(matrix[r][c].value) > 1:
				for poss in matrix[r][c].value:
					if col.count(poss) == 1:
						matrix[r][c].value = {poss}
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True
	return matrix, changesMade
#-----------------------------------------------------------------------------------
def trickTwoBlocks(matrix):
	changesMade = False
	blocks = makeBlockList(matrix)
	oldmatrix = deepcopy(matrix)
	for block in range(MAX):
		blk = []
		for cell in range(MAX):
			if len(blocks[block][cell].value) > 1:
				tmp = set()
				while len(blocks[block][cell].value) > 0:
					a = blocks[block][cell].value.pop()
					blk.append(a)
					tmp = tmp | {a}
				blocks[block][cell].value = tmp
		for cell in range(MAX):
			if len(blocks[block][cell].value) > 1:
				for poss in blocks[block][cell].value:
					if blk.count(poss) == 1:
						blocks[block][cell].value = {poss}
	for r in range(MAX):
		for c in range(MAX):
			if oldmatrix[r][c].value != matrix[r][c].value:
				changesMade = True
	return matrix, changesMade
#-----------------------------------------------------------------------------------
def makeAllPossibleSimpleChangesToMatrix(matrix):	# in place and returns
	
	matrix, boo = trickOneRows(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	matrix, boo = trickOneCols(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	matrix, boo = trickOneBlocks(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	matrix, boo = trickTwoRows(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	matrix, boo = trickTwoCols(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	matrix, boo = trickTwoBlocks(matrix)
	if boo:
		matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

	return matrix
#-----------------------------------------------------------------------------------
def makeBlockList(matrix):
	block = [[], [], [], [], [], [], [], [], []]

	block[0] = [matrix[0][0], matrix[0][1], matrix[0][2],
				matrix[1][0], matrix[1][1], matrix[1][2],
				matrix[2][0], matrix[2][1], matrix[2][2],]

	block[1] = [matrix[0][3], matrix[0][4], matrix[0][5],
				matrix[1][3], matrix[1][4], matrix[1][5],
				matrix[2][3], matrix[2][4], matrix[2][5],]

	block[2] = [matrix[0][6], matrix[0][7], matrix[0][8],
				matrix[1][6], matrix[1][7], matrix[1][8],
				matrix[2][6], matrix[2][7], matrix[2][8],]

	block[3] = [matrix[3][0], matrix[3][1], matrix[3][2],
				matrix[4][0], matrix[4][1], matrix[4][2],
				matrix[5][0], matrix[5][1], matrix[5][2],]

	block[4] = [matrix[3][3], matrix[3][4], matrix[3][5],
				matrix[4][3], matrix[4][4], matrix[4][5],
				matrix[5][3], matrix[5][4], matrix[5][5],]
   
	block[5] = [matrix[3][6], matrix[3][7], matrix[3][8],
				matrix[4][6], matrix[4][7], matrix[4][8],
				matrix[5][6], matrix[5][7], matrix[5][8],]
  
	block[6] = [matrix[6][0], matrix[6][1], matrix[6][2],
				matrix[7][0], matrix[7][1], matrix[7][2],
				matrix[8][0], matrix[8][1], matrix[8][2],]
   
	block[7] = [matrix[6][3], matrix[6][4], matrix[6][5],
				matrix[7][3], matrix[7][4], matrix[7][5],
				matrix[8][3], matrix[8][4], matrix[8][5],]
   
	block[8] = [matrix[6][6], matrix[6][7], matrix[6][8],
				matrix[7][6], matrix[7][7], matrix[7][8],
				matrix[8][6], matrix[8][7], matrix[8][8],]


	return block
#-----------------------------------------------------------------------------------
def solutionIsCorrect(matrix):
	rows = [[], [], [], [], [], [], [], [], []]
	cols = [[], [], [], [], [], [], [], [], []]
	for r in range(MAX):
		for c in range(MAX):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)

	block = [[], [], [], [], [], [], [], [], []]

	block[0] = [matrix[0][0].value, matrix[0][1].value, matrix[0][2].value,
				matrix[1][0].value, matrix[1][1].value, matrix[1][2].value,
				matrix[2][0].value, matrix[2][1].value, matrix[2][2].value,]

	block[1] = [matrix[0][3].value, matrix[0][4].value, matrix[0][5].value,
				matrix[1][3].value, matrix[1][4].value, matrix[1][5].value,
				matrix[2][3].value, matrix[2][4].value, matrix[2][5].value,]

	block[2] = [matrix[0][6].value, matrix[0][7].value, matrix[0][8].value,
				matrix[1][6].value, matrix[1][7].value, matrix[1][8].value,
				matrix[2][6].value, matrix[2][7].value, matrix[2][8].value,]

	block[3] = [matrix[3][0].value, matrix[3][1].value, matrix[3][2].value,
				matrix[4][0].value, matrix[4][1].value, matrix[4][2].value,
				matrix[5][0].value, matrix[5][1].value, matrix[5][2].value,]

	block[4] = [matrix[3][3].value, matrix[3][4].value, matrix[3][5].value,
				matrix[4][3].value, matrix[4][4].value, matrix[4][5].value,
				matrix[5][3].value, matrix[5][4].value, matrix[5][5].value,]
   
	block[5] = [matrix[3][6].value, matrix[3][7].value, matrix[3][8].value,
				matrix[4][6].value, matrix[4][7].value, matrix[4][8].value,
				matrix[5][6].value, matrix[5][7].value, matrix[5][8].value,]
  
	block[6] = [matrix[6][0].value, matrix[6][1].value, matrix[6][2].value,
				matrix[7][0].value, matrix[7][1].value, matrix[7][2].value,
				matrix[8][0].value, matrix[8][1].value, matrix[8][2].value,]
   
	block[7] = [matrix[6][3].value, matrix[6][4].value, matrix[6][5].value,
				matrix[7][3].value, matrix[7][4].value, matrix[7][5].value,
				matrix[8][3].value, matrix[8][4].value, matrix[8][5].value,]
   
	block[8] = [matrix[6][6].value, matrix[6][7].value, matrix[6][8].value,
				matrix[7][6].value, matrix[7][7].value, matrix[7][8].value,
				matrix[8][6].value, matrix[8][7].value, matrix[8][8].value,]

	for r in rows: 
		for n in range(1, MAX+1):
			if {n} not in r:
				return False
	for c in cols: 
		for n in range(1, MAX+1):
			if {n} not in c: 
				return False
	for b in block:
		for n in range(1, MAX+1):
			if {n} not in b: 
				return False
	return True
#-----------------------------------------------------------------------------------
def badMatrix(matrix):
	col = [[],[],[],[],[],[],[],[],[]]
	for r in range(MAX):
		row = []
		for c in range(MAX):
			if len(matrix[r][c].value) == 1:
				row.append(next(iter(matrix[r][c].value)))
				col[c].append(next(iter(matrix[r][c].value)))
		if len(row) != len(set(row)):
			return True
	for c in col:
		if len(c) != len(set(c)):
			return True
	return False
#-----------------------------------------------------------------------------------
from copy import deepcopy
from time import clock; START_TIME = clock(); main();
print (' | %5.6f seconds |' %(clock()-START_TIME))