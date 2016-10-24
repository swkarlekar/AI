'''
######################
|Sweta Karlekar Pd 4 |
|9/16/14             |
######################
'''
filename = open('words.txt', 'rb')
lst = filename.read().split('\n')

def main():
   parent = "silver"
   target = "sliver"
   outfile = open('output.txt', 'wb') 
   dict = {}
   for n in range(len(lst)):
      dict[lst[n]] = neighbors(lst[n], parent)
   print("Breadth-First Search w/ Priority Queue: ")
   print(bfprioritysearch(parent, target, dict))
   parent2 = "silver"
   target2 = "sliver"
   dict2 = {}
   for n in range(len(lst)):
      dict2[lst[n]] = neighbors(lst[n], parent)
   print("Depth-First Search: ")
   print(dfsearch(parent2, target2, dict2))
   
def neighbors(myword, parent):
   outerlst = []
   temp = []
   for n in range(len(lst)):
      diff = 0
      for i in range(6):
         if lst[n][i] != myword[i]:
            diff = diff + 1
      if diff == 1: 
         temp.append(lst[n])
   outerlst.append(temp)
   if myword != parent:
      outerlst.append(-1)
      outerlst.append("?")
   else: 
      outerlst.append("0")
      outerlst.append("head")
   return outerlst    

def heuristic(word, stopWord):
   return sum([stopWord[n] != word[n] for n in range (0, 6)])
 
def bfprioritysearch(parent, target, dict):
   queue = []
   count = 0
   queue.append(parent)
   while parent != target:
      if len(queue) == 0: 
         exit('No reachable paths.')
      queue.sort(key = lambda word: heuristic(word, target))
      parent = queue.pop(0)
      count+=1
      for child in dict[parent][0]:
         if dict[child][1] == -1: 
            dict[child][1] = int(dict[parent][1]) + 1
            dict[child][2] = parent
            queue.append(child)
   path = [target]
   while dict[target][2] != "head":
      path.append(dict[target][2])
      target = dict[target][2]
   path.reverse()
   return path, count

def dfsearch(parent, target, dict):
   queue = []
   count = 0
   queue.append(parent)
   while parent != target:
      if len(queue) == 0: 
         exit('No reachable paths.')
      parent = queue.pop()
      count+=1
      for child in dict[parent][0]:
         if dict[child][1] == -1: 
            dict[child][1] = int(dict[parent][1]) + 1
            dict[child][2] = parent
            queue.append(child)
   path = [target]
   while dict[target][2] != "head":
      path.append(dict[target][2])
      target = dict[target][2]
   path.reverse()
   return path, count
   
if __name__ == '__main__': main()
