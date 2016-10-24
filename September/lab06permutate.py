'''
######################
|Sweta Karlekar Pd 4 |
|10/04/14            |
######################
'''
import itertools;
from re import findall
from string import maketrans

def main(): 
   a1 = str(input("Augend: "))
   a2 = str(input("Addend: "))
   a3 = str(input("Sum: "))
   findSolution(a1, a2, a3)
   

def findSolution(a1, a2, a3):
   count = 0
   puzzle = a1 + "*" + a2 + "==" + a3
   puzzle = puzzle.upper()
   words = findall('[A-Z]+', puzzle)
   keys = set("".join(words))
   firsts = set(word[0] for word in words)
   keys = "".join(firsts) + "".join(keys - firsts)
   for group in itertools.permutations("1234567890", len(keys)): 
      table = maketrans(keys, "".join(group))
      equation = puzzle.translate(table)
      if "0" not in group[:len(firsts)]:
         if eval(equation):
            print(puzzle, equation)
            count+=1
            solutionFound = True
   if not solutionFound: 
      print('No solutions exist.')
   else:
      print(str(count) + " solutions have been found.")

#---------------------------------------------------------------------
from time import clock; START_TIME = clock(); main();
print (' | %5.2f seconds |' %(clock()-START_TIME))