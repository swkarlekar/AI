def main():
	root = Node("*")
	file1 = open("ghostdict.py")
	for word in file1:
		root.insert(word.lower().strip())
	file1.close()
	stng = ""
	while True: 
		stng = requestAndCheckHumanMove(root, stng)
		stng = requestAndCheckComputerMove(root, stng)

def requestAndCheckComputerMove(root, stng):
	stng += root.searchForNextLetter(stng)
	print(" ", stng)
	if root.search(stng) and len(stng)>3:
		print('-----------------------------------------------')
		print(" COMPUTER LOSES! ", stng, " is a word. ")
		print("---------------< GAME OVER >-------------------")
		exit()
	return stng

def spellWordFromString(root, stng):
	if root.search(stng) == True: 
		return stng
	stng += root.searchForNextLetter(stng)
	return spellWordFromString(root, stng)

def requestAndCheckHumanMove(root, stng):
	stng += input("Human - choose your letter: ").lower()[0]
	print(" ", stng)
	if root.search(stng)  and len(stng)>3:
		print('-----------------------------------------------')
		print(" HUMAN LOSES! ", stng, " is a word. ")
		print("---------------< GAME OVER >-------------------")
		exit()
	if root.fragmentInDictionary(stng) == False:
		print("-----------------------------------------------")
		print(" HUMAN LOSES! ", stng, " does not begin any word.")
		print("The computer's word was ", spellWordFromString(root, stng[0:-1]), " .")
		print("---------------< GAME OVER >-------------------")
		exit()
	return stng

class Node(object):
	def __init__(self, value):
		self.value = value
		self.children = {}
	def __repr__(self):
		self.print()
		return ''
	def display(self):
		if self.value == '$': return
		print("====================NODE====================")
		print('--> self.value   =', self.value)
		print('--> self.children: [', end = '')

		for key in self.children:
			if key != '$':
				print(key, sep = "", end = ", ")
		print("]")		
		print('---------------------------------------------')

		for char in self.children:
				(self.children[char]).display()
	def insert(self, stng):
		str = stng
		str = str.replace('-', '')
		str = str.replace("'", '')
		if str =='':
			p = Node('$')
			self.children[p.value] = p
		if not str.isalpha():
			return ""
		elif str[0] in self.children:
			self.children[str[0]].insert(str[1:])
		elif str[0] not in self.children:
			p = Node(str[0])
			self.children[p.value] = p
			p.insert(str[1:])
		
	def search(self, stng):
		if len(stng) == 0:
			return "$" in self.children
		if stng[0] not in self.children:
			return False
		if stng[0] in self.children:
			self = self.children[stng[0]]
			stng = stng[1:]
			return self.search(stng)
		return False

	def randomChild(self): #choose a random letter from children of current node #choice(List()) from random library
		return choice([self.children[x].value for x in self.children])

	def searchForNextLetter(self, stng): #recursive #runs through tree to final character in string and then calls random child
		if len(stng) == 0:
			return self.randomChild()
		self = self.children[stng[0]]
		stng = stng[1:]
		return self.searchForNextLetter(stng)

	def fragmentInDictionary(self, stng): #recursive #checks that string is in trie 
		if len(stng) == 0:
			return True
		if stng[0] not in self.children:
			return False
		if stng[0] in self.children:
			self = self.children[stng[0]]
			stng = stng[1:]
			return self.fragmentInDictionary(stng)
		return False

from sys import setrecursionlimit; setrecursionlimit(100)
from random import choice
from time import clock
main()		
