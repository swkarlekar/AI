#GG is the only case which would produce two gold coins
from random import choice
options = [0, 1]
count = 0
for n in range(10000):
	if(choice(list(options)) != 0): 
		count += 1 #probability for GS drawer
	count+=1 #probability for GG drawer
	count+=0 #probability for SS drawer
print("------------------------------------------------------------------")
print("| Probably of obtaining a second gold coin: ", 100*(10000/count), "% |")
print("------------------------------------------------------------------")
