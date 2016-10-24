'''
######################
|Sweta Karlekar Pd 4 |
|9/16/14             |
######################
'''
filename = open('words.txt', 'rb')
lst = filename.read().split('\n')
count = 0

def main():
   outfile = open('output.txt', 'wb') 
   dict = {}
   parent = "banker"
   target = "golden"
   for n in range(len(lst)):
      dict[lst[n]] = neighbors(lst[n], parent)
   print(bfsearch(parent, target, dict))
   print("Number of pops: " + str(count))
   
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

 
def bfsearch(parent, target, dict):
   queue = []
   queue.append(parent)
   while parent != target:
      if len(queue) == 0: 
         exit('No reachable paths.')
      parent = queue.pop(0)
      global count
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
   return path 
   
if __name__ == '__main__': main()
