##########################
# Sweta Karlekar         #
# Period 4               #
# FizzBuzz Program       #
# April 7th, 2015        #
##########################
from random import random

#----------------------------------------------------------------------------------------
def main():
	#part1()
	r = input("# of rows: ")
	c = input("# of cols: ")
	part2(int(r), int(c))
	part3(int(r), int(c))
#----------------------------------------------------------------------------------------
def part1():
	for x in range(1, 101):
		statement = str(x)
		if x%5 == 0: statement = "Fizz"
		if x%3 == 0: statement = "Buzz"
		if x%15 == 0: statement = "Fizz and Buzz"
		print(statement)
#----------------------------------------------------------------------------------------
def part2(r, c):
	print("\nMatrix Building, Formatting, and Printing\n")
	M = [[round(float(random()*5000+0.01), 2) for COL in range(c)] for ROW in range(r)]
	for row in M: 
		for col in row: 
			print('%8.2f'%(col), end = ' ')
		print()
	print("===================================")
#----------------------------------------------------------------------------------------
def part3(n, m): #n = columns of vector and rows of matrix, m = columns of matrix
	print("\nMatrix and Vector Multiplication\n")
	V = [round(float(random()*100+0.01), 2) for COL in range(n)]
	M = [[round(float(random()*100+0.01), 2) for COL in range(m)] for ROW in range(n)]
	for row in M: 
		for col in row: 
			print('%8.2f'%(col), end = ' ')
		print()
	print(' MATRIX', "="*70, '\n')
	for row in V: 
		print('%8.2f'%(row), end = ' ')
	print("\n", 'VECTOR', '='*70, '\n')
	A = [sum([(V[c]*M[c][COL]) for c in range(n)]) for COL in range(m)]
	for col in A: 
		print('%8.2f'%(col), end = ' ')
	print("\n", 'PRODUCT', '='*69, '\n')
#----------------------------------------------------------------------------------------
if __name__ == '__main__': 
	from time import clock; START_TIME = clock();main();
	print (' | %5.2f seconds |' %(clock()-START_TIME))
#----------------------------------------------------------------------------------------
'''
Why would a recruiter not hire the programmer who scores the highest on the code-puzzle test?: 
1) As the program is a summer internship (and not a job), it should be designed to help students learn new 
   programming skills. Therefore, the person who scores the highest will not benefit the most from the intership 
   and the spot should be given to someone else. 
2) People with high IQs may be incredibly smart, but also potentially antisocial, and therefore might not be able 
   to work well in a team. 
3) Programmers with high coding IQs may not be open to changing their coding style and learning new things. As the
   internship is focused on new experiences, it would not be the correct place for someone who is not willing to 
   learn new things. 
'''