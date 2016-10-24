def fibonacci(n): 
	if n==1: 
		return 1
	if n==0:
		return 0
	return fibonacci(n-1) + fibonacci(n-2)

print("Enter \"quit\" to exit.")
userInput = raw_input("Enter Number(n): ")
while(userInput != "quit"):
	print(fibonacci(int(userInput)))
	userInput = raw_input("Enter Number(n): ")
