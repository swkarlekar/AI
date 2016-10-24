'''
######################
|Sweta Karlekar Pd 4 |
|10/04/14            |
######################
'''
import itertools;

def main(): 
   a1 = input("Augend: ")
   a2 = input("Addend: ")
   a3 = input("Sum: ")
   fdict, s1, s2, s3 = findSolution(a1, a2, a3)
   for k, v in fdict.items(): 
      print(k, v)
   print(s1, s2, s3)

def findSolution(a1, a2, a3):
   combin = a1 + a2 + a3
   lst = []
   dict = {}
   for i in range(len(combin)):
      if combin[i] not in lst:
         lst.append(combin[i]) 
   for group in itertools.permutations(range(10)): 
      for i in range(len(lst)): 
         dict[lst[i]] = group[i]
      augend = turnIntoNum(a1, dict)
      addend = turnIntoNum(a2, dict)
      sum = turnIntoNum(a3, dict)
      if augend + addend == sum: 
         return dict, augend, addend, sum
   exit("No possible solutions.")
   
def turnIntoNum(st, dict): 
   tempst = ""
   for i in range(len(st)): 
      tempst += str(dict[st[i]])
   tempnum = int(tempst)
   return tempnum
   
main()