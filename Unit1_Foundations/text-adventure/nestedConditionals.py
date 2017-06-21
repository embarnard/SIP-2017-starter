number = int(input("Please enter a number: "))

if number % 2 == 0: # evens
	if number < 3:
		print("A")
	elif number < 10:
		print("B")
	else:
		print("C")
else: # odds
	if number < 3:
		print("a")
	elif number < 10:
		print("b")
	else:
		print("c")
	