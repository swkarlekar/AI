##########################
# Sweta Karlekar         #
# Period 4               #
# Letter-Shift Function  #
##########################

def main():
	str = input("Enter word: ")
	shift = int(input("Enter shift: "))
	print("Text shifted to right: ", end = "")
	tempRight = shiftText(str, shift)
	print(tempRight)
	print("Shifted back to the left: ", end = "")
	print(shiftText(tempRight, -shift))
	print("Text shifted to left: ", end = "")
	tempLeft = shiftText(str, -shift)
	print(tempLeft)
	print("Shifted back to the right: ", end = "")
	print(shiftText(tempLeft, shift))

def shiftText(str, shift):
	newstr = []
	for char in str:
		magnitude = ord(char)
		if ord('A')<=(ord(char))<=ord('Z'): 
			magnitude = ((ord(char)+shift)-ord('A'))%26 + ord('A')
		if ord('a')<=(ord(char))<=ord('z'):
			magnitude = ((ord(char)+shift)-ord('a'))%26 + ord('a')
		newstr.append(chr(magnitude))
	return "".join(newstr)

if __name__ == '__main__': 
	from time import clock; START_TIME = clock();main();
	print (' | %5.2f seconds |' %(clock()-START_TIME))

############# --------  OUTPUT ----------- #################
# Enter word: Cheer!                                       #
# Enter shift: 7                                           #
# Text shifted to right: Jolly!                            #
# Shifted back to the left: Cheer!                         #
# Text shifted to left: Vaxxk!                             #
# Shifted back to the right: Cheer!                        #
#  |  0.00 seconds |									   #
############################################################