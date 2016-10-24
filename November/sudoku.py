MAX =	9
import copy
#methods	to	write: printVerification(), displayTheSudokuBoard(), makeAllPossibleSimpleChangesToMatrix(),	coordinatesofCellWithSmallestValueSet()
changesMade = True
while changesMade == True:
   changesMade = False: 
      for r in range(MAX):
         for c in range(MAx):
            
def main():
	matrix =	createSudokuBoard()
	print(matrix)
	#oldMatrix = copy.deepcopy(matrix)
	#restoreValues(matrix, oldMatrix)
	matrix =	recursivelySolveTheSudoku(matrix)
	displayTheSudokuBoard(matrix)
	printVerification(matrix)

def createSudokuBoard():
	M = [	[4, 8, 1, 5, 0, 9, 6, 7, 0],
			[3, 0, 0, 8, 1, 6, 0, 0, 2], 
			[5, 0, 0, 7, 0, 3, 0, 0, 8], 
			[2, 0, 0, 0, 0, 0, 0, 0, 9], 
			[9, 0, 0, 0, 0, 0, 0, 0, 1], 
			[8, 0, 0, 0, 0, 0, 0, 0, 4], 
			[0, 3, 9, 2, 7, 5, 4, 8, 0], 
			[6, 0, 0, 0, 0, 0, 9, 2, 7],
			[7, 0, 0, 0, 0, 0, 3, 1, 0], ]
	matrix =	[]
	for r	in	range(MAX):
		row =	[]
		for c	in	range(MAX):
			row.append(Cell(M[r][c], r, c, matrix))
		matrix.append(row)
	return matrix
	
def restoreValues(matrix, oldMatrix):
	for r	in	range(MAX):
		for c	in	range(MAX):
			matrix[r][c].value =	oldMatrix[r][c].value
	return matrix

def recursivelySolveTheSudoku(matrix):
	matrix =	makeAllPossibleSimpleChangesToMatrix(matrix)
	if	badMatrix(matrix)	or	solutionIsCorrect(matrix):
		return matrix
	oldMatrix =	deepcopy(matrix)
	r,	c = coordinatesofCellWithSmallestValueSet(matrix)
	for guess in matrix[r][c].value:
		matrix[r][c].value =	{guess,}
		matrix =	recursivelySolveTheSudoku(matrix)
		if	solutionisCorect(matrix):
			return matrix
		matrix =	restoreValues(matrix, oldMatrix)
	return matrix

def solutionIsCorrect(matrix):
	rows = [[],	[], [], [],	[], [], [],	[], []]
	cols = [[],	[], [], [],	[], [], [],	[], []]
	for r	in	range(MAX):
		for c	in	range(MAX):
			rows[r].append(matrix[r][c].value)
			cols[c].append(matrix[r][c].value)
	block	= [[], [], [],	[], [], [],	[], [], []]
	
	block[0]	= [matrix[0][0].value, matrix[0][1].value, matrix[0][2].value,
				  matrix[1][0].value, matrix[1][1].value,	matrix[1][2].value,
				  matrix[2][0].value, matrix[2][1].value,	matrix[2][2].value,]
	
	block[1]	= [matrix[0][3].value, matrix[0][4].value, matrix[0][5].value,
				  matrix[1][3].value, matrix[1][4].value,	matrix[1][5].value,
				  matrix[2][3].value, matrix[2][4].value,	matrix[2][5].value,]
	
	block[2]	= [matrix[0][6].value, matrix[0][7].value, matrix[0][8].value,
				  matrix[1][6].value, matrix[1][7].value,	matrix[1][8].value,
				  matrix[2][6].value, matrix[2][7].value,	matrix[2][8].value,]
	
	block[3]	= [matrix[3][0].value, matrix[3][1].value, matrix[3][2].value,
				  matrix[4][0].value, matrix[4][1].value,	matrix[4][2].value,
				  matrix[5][0].value, matrix[5][1].value,	matrix[5][2].value,]
	
	block[4]	= [matrix[3][3].value, matrix[3][4].value, matrix[3][5].value,
				  matrix[4][3].value, matrix[4][4].value,	matrix[4][5].value,
				  matrix[5][3].value, matrix[5][4].value,	matrix[5][5].value,]
	
	block[5]	= [matrix[3][6].value, matrix[3][7].value, matrix[3][8].value,
				  matrix[4][6].value, matrix[4][7].value,	matrix[4][8].value,
				  matrix[5][6].value, matrix[5][7].value,	matrix[5][8].value,]
  
	block[6]	= [matrix[6][0].value, matrix[6][1].value, matrix[6][2].value,
				  matrix[7][0].value, matrix[7][1].value,	matrix[7][2].value,
				  matrix[8][0].value, matrix[8][1].value,	matrix[8][2].value,]
	
	block[7]	= [matrix[6][3].value, matrix[6][4].value, matrix[6][5].value,
				  matrix[7][3].value, matrix[7][4].value,	matrix[7][5].value,
				  matrix[8][3].value, matrix[8][4].value,	matrix[8][5].value,]
	
	block[8]	= [matrix[6][6].value, matrix[6][7].value, matrix[6][8].value,
				  matrix[7][6].value, matrix[7][7].value,	matrix[7][8].value,
				  matrix[8][6].value, matrix[8][7].value,	matrix[8][8].value,]
	
	for r	in	rows:	
		for n	in	range(1,	MAX+1):
			if	{n} not in r:
				return False
	for c	in	cols:	
		for n	in	range(1,	MAX+1):
			if	{n} not in c: 
				return False
	for b	in	block:
		for n	in	range(1,	MAX+1):
			if	{n} not in b: 
				return False
	return True
	
class	Cell(object):
	matrix =	None
	def __init__(self, val,	r,	c,	matrix):
		if	val != 0:
			self.value = {val,}
		else:
			self.value = {1,2,3,4,5,6,7,8,9}
		self.row	= r
		self.col	= c
		self.block = self.blockNumber(r,c)
		Cell.matrix	= matrix
	def blockNumber(self, row,	col):
		if			(self.row <	3)	and		(self.col <	3): return 0
		if			(self.row <	3)	and	(2	< self.col < 6): return	1
		if			(self.row <	3)	and	(5	< self.col):	return 2
		if		(2	< self.row < 6) and		(self.col <	3): return 3
		if		(2	< self.row < 6) and	(2	< self.col < 6): return	4
		if		(2	< self.row < 6) and	(5	< self.col):	return 5
		if			(self.row >	5)	and		(self.col <	3): return 6
		if			(self.row >	5)	and	(2	< self.col < 6): return	7
		if			(self.row >	5)	and	(5	< self.col):	return 8

def badMatrix(matrix):
	for r	in	range(MAX):
		for c	in	range(MAX):
			if	matrix[r][c].value == set():
				return True
	return False
	
main()