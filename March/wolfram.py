def setUpCanvas(root): 
	root.title("Wolfram's cellular automata: A Tk/Python Graphics Program")
	canvas = Canvas(root, width = 1270, height = 780, bg = 'black')
	canvas.pack(expand = YES, fill = BOTH)
	return canvas

def printList(rule):
	canvas.create_text(170, 20, text = "Rule " + str(rule), fill = 'gold', font = ('Helvetica', 10, 'bold'))
	L = [1,]
	copyOfRule = rule[::-1]
	canvas.create_text(650, 10, text = chr(9607), fill = 'RED', font = ('Helvetica', FSIZE, 'bold'))
	for row in range(1, 330):
		L = [0, 0] + L + [0, 0]
		listTriples = []
		for r in range(len(L)-2):
			listTriples.append(L[r:(r+3)])
		L = []
		for triple in listTriples:
			bin = int(str(triple[0])+str(triple[1])+str(triple[2]), 2)
			temp = copyOfRule[bin]
			L.append(temp)
		for n in range(len(L)):
			if L[n] == 1: 
				kolor = 'RED'
			else: kolor = 'BLACK'
			canvas.create_text(650-row*FSIZE + FSIZE*n, row*FSIZE+10, text = chr(9607), fill = kolor, font = ('Helvetica', FSIZE, 'bold'))

from tkinter import Tk, Canvas, BOTH, YES 
from time import clock
root = Tk()
canvas = setUpCanvas(root)
FSIZE = 2

def main():
	rule = [0, 0, 0, 1, 1, 1, 1, 0,]
	#rule = [1, 1, 1, 1, 1, 1, 1, 1,]
	#rule = [1, 1, 1, 1, 1, 1, 1, 1,]
	#rule = [1, 1, 1, 1, 1, 1, 1, 1,]
	#rule = [1, 1, 1, 1, 1, 1, 1, 1,]
	printList(rule)
	root.mainloop()

if __name__ == '__main__': main()