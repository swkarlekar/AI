'''
######################
|Sweta Karlekar Pd 4 |
|Trie Lab            |
|10/04/14            |
######################
'''

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



def main():
	root = Node("*")
	root.insert('cat')
	root.insert('catnip')
	root.insert('cats')
	root.insert('catnap')
	root.insert("can't")
	root.insert('cat-x')
	root.insert('dog')
	root.insert('dognip')
	root.display()
	print("Search:", root.search('cat'))
	print("Search:", root.search('catnip'))
	print("Search:", root.search('cats'))
	print("Search:", root.search('catnap'))
	print("Search:", root.search('can'))
main()		




from sys import setrecursionlimit; setrecursionlimit(100)
from time import clock