'''
######################
|Sweta Karlekar Pd 4 |
|10/03/14            |
######################
'''
import pickle
file1 = open('romFullNames.txt', 'rb')
names = file1.read().split('\n')
file2 = open('romEdges.txt', 'rb')
edges = file2.read().split('\n')
file3 = open('romNodes.txt', 'rb')
cities = file3.read().split('\n')
dictEdges = {}
dictNames = {}
dictCoordinates = {}
import copy
from math import sin, cos, acos, pi

def main():
   global dictEdges
   dictEdges = bdictEdges()
   global dictNames
   dictNames = bdictNames()
   global dictCoordinates
   dictCoordinates = bdictCoordinates()
   parent = input("Parent: ")
   target = input("Target: ")
   print("From " + parent + " to " + target + ":\n")
   print("A-star: ")
   tempstr = "".join(str(dictNames[city] + ", ") for city in astar(parent, target)) #w/ heuristic
   print("[" + tempstr[0:len(tempstr)-2] + "]\n")  
   print("Uniform-Cost Search: ") 
   tempstr = "".join(str(dictNames[city] + ", ") for city in astar(parent, target, False)) #w/out heuristic
   print("[" + tempstr[0:len(tempstr)-2] + "]")
   
def bdictEdges():
   dict = {}
   for name in names: 
      dict[name[0]] = []
   for edge in edges: 
      dict[edge[0]].append(edge[2])
      dict[edge[2]].append(edge[0])
   return dict

def bdictNames():
   dict = {} 
   for name in names: 
      dict[name[0].upper()] = name
   return dict

def bdictCoordinates():
   dict = {}
   for i in range(len(cities)):
      dict[cities[i][0]] = []
      dict[cities[i][0]].append(float(cities[i][2:9]))
      dict[cities[i][0]].append(float(cities[i][10:17]))
   return dict

def findDist(x1, y1, x2, y2):
   y1  = float(y1)
   x1  = float(x1)
   y2  = float(y2)
   x2  = float(x2)
   R   = float(3958.76) # miles
   y1 *= float(pi/180.0)
   x1 *= float(pi/180.0)
   y2 *= float(pi/180.0)
   x2 *= float(pi/180.0)
   return acos(float(str(sin(x1)*sin(x2) + cos(x1)*cos(x2)*cos(y2-y1))))*R
   

 
def astar(tparent, ttarget, bool = True):
   parent = tparent[0].upper()
   target = ttarget[0].upper()
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
         print(str(gvalue) + " miles")
         return path
      CLOSED[node] = gvalue
      for child in dictEdges[node]:
         childpath = path + [node]
         g = gvalue + findDist(dictCoordinates[child][0], dictCoordinates[child][1], dictCoordinates[node][0], dictCoordinates[node][1])
         if bool == True: 
            tuple = (g + findDist(dictCoordinates[child][0], dictCoordinates[child][1], dictCoordinates[target][0], dictCoordinates[target][1]), child, childpath, g)
         else:
            tuple = (g, child, childpath, g)
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
        
if __name__ == '__main__': 
   from random import random, randint; from math import sqrt; from copy import deepcopy; 
   from time import clock; START_TIME = clock(); main(); 