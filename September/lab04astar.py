'''
######################
|Sweta Karlekar Pd 4 |
|9/16/14   4286              |
######################
'''
import pickle
filename = open('words.txt', 'rb')
lst = filename.read().split('\n')
dict = pickle.load(open("output.txt", "rb"))
import copy

def main():
   parent = "silver"
   target = "sliver"
   astar(parent, target)

def heuristic(word, stopWord):
   return sum([stopWord[n] != word[n] for n in range (6)])
 
def astar(parent, target):
   OPEN = [(0, parent, [], 0)]
   CLOSED = {}
   count = 0
   while OPEN: 
      count += 1
      (fValue, node, path, gvalue) = OPEN.pop(0)
      if node == target:
         path.append(node)
         print("Number of pops: " + str(count))
         print("Length of Path: " + str(len(path)))
         exit(path)
      CLOSED[node] = gvalue
      for child in dict[node]:
         childpath = path + [node]
         g = len(childpath)
         tuple = (g + heuristic(child, target), child, childpath, g)
         if child in CLOSED: 
            if CLOSED[child] > g:
               del CLOSED[child]
               OPEN.append(tuple)
         elif sortOpenQueue(OPEN, child) == -1:
            OPEN.append(tuple)
            CLOSED[child] = g
         else: 
            index = sortOpenQueue(OPEN, child)
            if OPEN[index][3] > g:
               OPEN.remove(OPEN[index])
               OPEN.append(tuple)
      OPEN.sort()
   exit("No reachable paths.")

def sortOpenQueue(OPEN, target): 
   isThere = -1
   for i in range(len(OPEN)): 
      if OPEN[i][1] == target:
         isThere = i
   return isThere
        
if __name__ == '__main__': main()

