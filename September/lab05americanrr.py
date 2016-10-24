'''
######################
|Sweta Karlekar Pd 4 |
|10/04/14            |
######################
'''
import pickle
file1 = open('rrNodeCity.txt', 'rb')
names = file1.read().split('\n')
file2 = open('rrEdges.txt', 'rb')
edges = file2.read().split('\n')
file3 = open('rrNodes.txt', 'rb')
cities = file3.read().split('\n')
dictEdges = {}
dictNames = {}
dictCoordinates = {}
import copy
from math import sin, cos, acos, pi
from types import *

def main():
   global dictEdges
   dictEdges = bdictEdges()
   global dictCoordinates
   dictCoordinates = bdictCoordinates()
   global dictNames
   dictNames = bdictNames()
   strparent = input("Parent: ")
   strtarget = input("Target: ")
   target = dictNames[strtarget]
   parent = dictNames[strparent]
   print("From " + parent + " to " + target + ":\n")
   print("A-star: ")
   print(astar(parent, target))
   print("\n")
   print("Uniform-Cost Search: ") 
   print(astar(parent, target, False))


def bdictEdges():
   dict = {}
   for edge in edges: 
      dict[edge[0:7]] = []
      dict[edge[8:15]] = []
   for edge in edges: 
      dict[edge[0:7]].append(edge[8:15])
      dict[edge[8:15]].append(edge[0:7])
   return dict

def bdictNames():
   dict = {} 
   for name in names: 
      dict[name[8:len(name)]] = name[0:7]
   return dict

def bdictCoordinates():
   dict = {}
   for i in range(len(cities)):
      templst = cities[i].split(" ")
      dict[templst[0]] = []
      dict[templst[0]].append(templst[1])
      dict[templst[0]].append(templst[2])
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

 
def astar(parent, target, bool = True):
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
   print (' | %5.2f seconds |' %(clock()-START_TIME))
