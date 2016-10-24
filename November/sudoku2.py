'''
######################
|Sweta Karlekar Pd 4 |
|Sudoku Lab          |
|10/04/14            |
######################
'''
MAX = 9
from copy import deepcopy
from collections import Counter
def main(): 
   board = createSudokuBoard()
   print("Original Board:")
   printMatrix(board)
   board = recursivelySolveTheSudoku(board)
   print("Solved Board:")
   printMatrix(board)         
   if solutionIsCorrect(board):
      print("Board verified.")
   else: 
      print("Wrong solution.")

def printMatrix(board):
   for row in range(MAX): 
      for col in range(MAX):
         if col == 0:
            print("|", end = '') 
         if len(board[row][col].value) == 1:
            print(board[row][col].value, end = ' ')
         else: 
            print({0}, end = ' ')
         if (col+1)%3==0:
            print("|", end = "")
      if (row+1)%3==0:
         print("\n_________________________________________")
      print()

def makeAllPossibleSimpleChangesToMatrix(matrix):
   oldmatrix = deepcopy(matrix)
   changesMade = False

   matrix = solveSimpleSolutionsRow(matrix)

   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
      
   matrix = solveSimpleSolutionsCol(matrix)
   
   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
            
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
      
   matrix = solveSimpleSolutionsBlock(matrix)
   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)

   matrix = trickTwoRows(matrix)
   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
      
   matrix = trickTwoCols(matrix)
   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
   
   matrix = trickTwoBlocks(matrix)
   for r in range(MAX):
      for c in range(MAX):
         if matrix[r][c].value != oldmatrix[r][c].value:
            changesMade = True
   if changesMade:
      matrix = makeAllPossibleSimpleChangesToMatrix(matrix)
   return matrix 
   
def createBlocks(matrix):
   block	= [[], [], [],	[], [], [],	[], [], []]
	
   block[0]	= [matrix[0][0], matrix[0][1], matrix[0][2],
      		  matrix[1][0], matrix[1][1],	matrix[1][2],
      		  matrix[2][0], matrix[2][1],	matrix[2][2],]
	
   block[1]	= [matrix[0][3], matrix[0][4], matrix[0][5],
      		  matrix[1][3], matrix[1][4],	matrix[1][5],
      		  matrix[2][3], matrix[2][4],	matrix[2][5],]
	
   block[2]	= [matrix[0][6], matrix[0][7], matrix[0][8],
      		  matrix[1][6], matrix[1][7],	matrix[1][8],
      		  matrix[2][6], matrix[2][7],	matrix[2][8],]
	
   block[3]	= [matrix[3][0], matrix[3][1], matrix[3][2],
      		  matrix[4][0], matrix[4][1],	matrix[4][2],
      		  matrix[5][0], matrix[5][1],	matrix[5][2],]
	
   block[4]	= [matrix[3][3], matrix[3][4], matrix[3][5],
      		  matrix[4][3], matrix[4][4],	matrix[4][5],
      		  matrix[5][3], matrix[5][4],	matrix[5][5],]
	
   block[5]	= [matrix[3][6], matrix[3][7], matrix[3][8],
      		  matrix[4][6], matrix[4][7],	matrix[4][8],
      		  matrix[5][6], matrix[5][7],	matrix[5][8],]
  
   block[6]	= [matrix[6][0], matrix[6][1], matrix[6][2],
      		  matrix[7][0], matrix[7][1],	matrix[7][2],
      		  matrix[8][0], matrix[8][1],	matrix[8][2],]
	
   block[7]	= [matrix[6][3], matrix[6][4], matrix[6][5],
      		  matrix[7][3], matrix[7][4],	matrix[7][5],
      		  matrix[8][3], matrix[8][4],	matrix[8][5],]
	
   block[8]	= [matrix[6][6], matrix[6][7], matrix[6][8],
      		  matrix[7][6], matrix[7][7],	matrix[7][8],
      		  matrix[8][6], matrix[8][7],	matrix[8][8],]
   
   return block
   
def solveSimpleSolutionsBlock(matrix):
   block = createBlocks(matrix)
   for blockindex in range(MAX):
      st = set()
      for cell in range(MAX):
         if len(block[blockindex][cell].value) == 1:
            temp = st | block[blockindex][cell].value
            st = temp
      for cell in range(MAX):
         if len(block[blockindex][cell].value) > 1:
            block[blockindex][cell].value = block[blockindex][cell].value - st
   return matrix

def trickTwoRows(matrix):
   for row in range(MAX):
      guesses = []
      for col in range(MAX):
         if len(matrix[row][col].value) > 1:
            for values in matrix[row][col].value: 
               guesses.append(values)
      for col in range(MAX):
         if len(matrix[row][col].value) > 1:
            for values in matrix[row][col].value:
               if countTimesInList(guesses, values) == 1:
                  matrix[row][col].value = {values}
   return matrix

def trickTwoCols(matrix):
   for col in range(MAX):
      guesses = []
      for row in range(MAX):
         if len(matrix[row][col].value) > 1: 
            for values in matrix[row][col].value: 
               guesses.append(values)            
      for row in range(MAX):
         if len(matrix[row][col].value) > 1:
            for values in matrix[row][col].value:
               if countTimesInList(guesses, values) == 1:
                  matrix[row][col].value = {values}
   return matrix

def trickTwoBlocks(matrix):
   block = createBlocks(matrix)
   for blockindex in range(MAX):
      guesses = []
      for cell in range(MAX):
         if len(block[blockindex][cell].value) > 1:
            for values in block[blockindex][cell].value: 
               guesses.append(values)  
      for cell in range(MAX):
         if len(block[blockindex][cell].value) > 1:
            for values in block[blockindex][cell].value:
               if countTimesInList(guesses, values) == 1:
                  block[blockindex][cell].value = {values}
   return matrix
   
def countTimesInList(lst, values):
   count = 0
   for n in range(len(lst)):
      if lst[n] == values:
         count+=1
   return count

def solveSimpleSolutionsRow(matrix):
   for row in range(MAX):
      st = set()
      for col in range(MAX):
         if len(matrix[row][col].value) == 1: 
            temp = st | matrix[row][col].value
            st = temp
      for col in range(MAX):
         if len(matrix[row][col].value) > 1:
            matrix[row][col].value = matrix[row][col].value - st
   return matrix

def solveSimpleSolutionsCol(matrix):
   for col in range(MAX):
      st = set()
      for row in range(MAX):
         if len(matrix[row][col].value) == 1: 
            temp = st | matrix[row][col].value
            st = temp
      for row in range(MAX):
         if len(matrix[row][col].value) > 1:
            matrix[row][col].value = matrix[row][col].value - st
   return matrix
   
def createSudokuBoard():
   M = [	[8, 0, 0, 0, 0, 0, 0, 0, 0],
			[0, 0, 3, 6, 0, 0, 0, 0, 0], 
			[0, 7, 0, 0, 9, 0, 2, 0, 0], 
			[0, 5, 0, 0, 0, 7, 0, 0, 0], 
			[0, 0, 0, 0, 4, 5, 7, 0, 0], 
			[0, 0, 0, 1, 0, 0, 0, 3, 0], 
			[0, 0, 1, 0, 0, 0, 0, 6, 8], 
			[0, 0, 8, 5, 0, 0, 0, 1, 0],
			[0, 9, 0, 0, 0, 0, 4, 0, 0], ]
   '''
   M = [	[4, 8, 1, 5, 0, 9, 6, 7, 0],
			[3, 0, 0, 8, 1, 6, 0, 0, 2], 
			[5, 0, 0, 7, 0, 3, 0, 0, 8], 
			[2, 0, 0, 0, 0, 0, 0, 0, 9], 
			[9, 0, 0, 0, 0, 0, 0, 0, 1], 
			[8, 0, 0, 0, 0, 0, 0, 0, 4], 
			[0, 3, 9, 2, 7, 5, 4, 8, 0], 
			[6, 0, 0, 0, 0, 0, 9, 2, 7],
			[7, 0, 0, 0, 0, 0, 3, 1, 0], ]
   '''
   matrix =	[]
   for r	in	range(MAX):
      row =	[]
      for c	in	range(MAX):
         row.append(Cell(M[r][c], r, c, matrix))
      matrix.append(row)
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
      if	solutionIsCorrect(matrix):
         return matrix
      matrix =	restoreValues(matrix, oldMatrix)
   return matrix
   
def restoreValues(matrix, oldMatrix):
   for r	in	range(MAX):
      for c	in	range(MAX):
         matrix[r][c].value =	oldMatrix[r][c].value
   return matrix
   
def badMatrix(matrix):
   bool = solutionIsCorrect(matrix)
   count = 0
   for r	in	range(MAX):
      for c	in	range(MAX):
         if	matrix[r][c].value == set():
            return True
   for r in range(MAX):
      for c in range(MAX):
         if len(matrix[r][c].value) == 1 and not bool:
            count+=1
   if count == MAX*MAX:
      return True
   return False

def coordinatesofCellWithSmallestValueSet(matrix):
   min = 200
   row = 0
   col = 0
   for r in range(MAX):
      for c in range(MAX):
         if len(matrix[r][c].value) < min and len(matrix[r][c].value) >=2:
            min = len(matrix[r][c].value)
            row = r
            col = c
   return row, col

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
      
from time import clock; START_TIME = clock(); main();
print (' | %5.2f seconds |' %(clock()-START_TIME))