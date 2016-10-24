filename = open('words.txt', 'r')
lst = list(filename)
myword = 'silver'
for n in range(len(lst)):
   diff = 0
   for i in range(6):
      if lst[n][i] != myword[i]:
         diff = diff + 1
   if diff == 1: 
      print(lst[n])
'''


def main(): 
   word = "wallet"
   parent = "XXXXX"
   print(neighbors(word, parent))
   
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
      temp.sort()
   outerlst.append(temp)
   if myword != parent:
      outerlst.append(-1)
      outerlst.append("?")
   else: 
      outerlst.append("0")
      outerlst.append("head")
   return outerlst
   
main()
'''
         
         
         