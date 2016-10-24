'''
+-------------------------------------------+
|   Alison Hau, pd 2, 1/2/14            |
|                                 |
|   Lab 5:    Something About Railroads?      |
|                                 |
|   I have no idea what's happening.      |
|                                 |
+-------------------------------------------+
'''
def main():
   names = makeNameListFromFileRomania('romFullNames.txt')
   nodes = makeNodeListFromFileRomania('romNodes.txt', names)
   edgeList = makeEdgeDictFromFile('romEdges.txt',names)
   print(nodes)
   print(len(nodes))
   
   startStation = ensureStationValid(input('Start station?  '),nodes)
   targetStation = ensureStationValid(input('End station?  '),nodes)

   print('\nTrip:  %s ----> %s' % (startStation, targetStation))

   print(edgeList)

   nodesDict = makeNodesDict(nodes)
   path, num, dist = astar(edgeList, startStation, targetStation, names, nodesDict)

   printListPretty(path)
   print ('Pops:  ' + str(num))
   print ('Distance: '+ str(dist))
   
#----------------------------------------------------------------------
def makeNodesDict(listOfNodes):
   nodesDict = {}
   for n in range(len(listOfNodes)):
      a,b,c = listOfNodes[n]
      a = a.strip()
      b = b.strip()
      c = c.strip()
      nodesDict[a] = (b,c)
   return nodesDict
#----------------------------------------------------------------------
def makeEdgeDictFromFile(openfile,namelist):
   filename = open(openfile, 'rb')
   edgelist = list(filename)
   for n in range(len(edgelist)):
      edgelist[n] = edgelist[n].decode('utf-8')
      edgelist[n] = edgelist[n].strip()
      edgelist[n] = edgelist[n].split(' ') 
      a,b = edgelist[n]
      for name in namelist:
         if a is name[0]:
            a = name
         elif b is name[0]:
            b = name
      edgelist[n] = a.strip(),b.strip()
   edgeDict = {}
   for n in range(len(edgelist)):
      key, val = edgelist[n]
      edgeDict[key] = getNeighbors(key, edgelist)
   for n in namelist:
      if n not in edgeDict.keys():
         edgeDict[n] = []
   return edgeDict
#----------------------------------------------------------------------
def getNeighbors(word,wordlist):
   neighborlist = []
   for n in range(len(wordlist)):
      a,b = wordlist[n]
      if a is word:
         neighborlist.append(b.strip())
   return neighborlist
#----------------------------------------------------------------------
def heur(start, end, nodes):
   starty, startx = nodes[start]
   endy, endx = nodes[end]
   return calcd(starty,startx,endy,endx)
#----------------------------------------------------------------------
#
# Torbert, 22 Sept 2014
#
from math import pi , acos , sin , cos
#
def calcd(y1,x1, y2,x2):
   #
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   #
   R   = 3958.76 # miles
   #
   y1 *= pi/180.0
   x1 *= pi/180.0
   y2 *= pi/180.0
   x2 *= pi/180.0
   #
   # approximate great circle distance with law of cosines
   #
   return acos( sin(y1)*sin(y2) + cos(y1)*cos(y2)*cos(x2-x1) ) * R
   #
#
# end of file
#
#----------------------------------------------------------------------
def astar(Dict, start, end, lst, nodes):
   startnode = (0, start, [], 0)
   #goadnode = () not used
   priorityQ = []
   priorityQ.append(startnode)   # tuple: (g+h, name, path from room, dist from start (g))
   print ('Getting path...')

   closedDict = {}   # for nodes and their g values
   popcount = 0
   distcount = 0

   # q.sort() sorts least to greatest
   while priorityQ:
      (fVal, name, path, gVal) = priorityQ.pop(0)
      popcount += 1
      if name == end:
         path.append(name)
         return path, popcount, distcount
      closedDict[name] = gVal
      for child in Dict[name]:
         cpath = path + [name]
         #newg = len(cpath) g value isn't the length of the path
         newg = gVal + heur(child, name, nodes)
         temptuple = (newg + heur(child, end, nodes), child, cpath, newg)
         #distcount += heur(child, end, nodes) not needed, gvalue is the total distance traveled
         #print (' child: ', str(heur(child, end, nodes))) ??
         if child in closedDict:
            if closedDict[child] > newg:
               del closedDict[child]
               priorityQ.append(temptuple)
         #elif sortQueue(priorityQ, child): what? this is an incomplete if statement
         elif sortQueue(priorityQ, child) == -1: 
            priorityQ.append(temptuple)
            closedDict[child] = newg
         else:
            a = sortQueue(priorityQ, child)
            if priorityQ[a][3] > newg:
               priorityQ.remove(priorityQ[a])
               priorityQ.append(temptuple)
      priorityQ.sort()
#----------------------------------------------------------------------
def sortQueue(lst, pq, target): 
   there = -1
   for i in range(len(pq)): 
      #if lst[i][1] == target: #if pq[i][1] not lst[i][1]
      if pq[i][1] == target:
         there = i
   return there
#----------------------------------------------------------------------
def ensureStationValid(word, valid):
   word = word.strip()
   word = word[0].upper()+word[1:]
   while word not in keys(valid):
      word = input('Please enter a valid station:  ')
      word = word[0].upper()+word[1:]
   return word
#---------------------------------------------------------------------

def keys(lst):
   keylist = []
   for n in range(len(lst)):
      a,b = lst[n]
      keylist.append(a)
   return keylist

#---------------------------------------------------------------------
def makeNodeListFromFileRomania(nodefile, namelist):
   filename = open (nodefile, 'rb')
   nodelist = list(filename)
   for n in range(len(nodelist)):
      nodelist[n] = nodelist[n].decode('utf-8')
      nodelist[n] = nodelist[n].strip()
      nodelist[n] = nodelist[n].split(' ')
      a,b,c = nodelist[n]
      nodelist[n] = namelist[n].strip(),b.strip(),c.strip()
   return nodelist
#---------------------------------------------------------------------
def makeNameListFromFileRomania(name):
   filename = open(name, 'rb') #rb not r
   tmp = filename.read().split('\n') #dont use list(), just read().split('\n')
   return tmp
#---------------------------------------------------------------------
def printListPretty(somelist):
   for n in range(len(somelist)):
      print ('\t',somelist[n])
#---------------------------------------------------------------------
from time import clock; START_TIME = clock(); main();
print (' | %5.2f seconds |' %(clock()-START_TIME))