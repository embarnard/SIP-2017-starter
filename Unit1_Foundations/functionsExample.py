# this is how you define a function
# this function has one parameter, named number
def squareANumber(number):
	return(number ** 2)


# you can then use the function multiple times in your code
print(squareANumber(5))

x = squareANumber(-3)
print(x)


# here's another function:
def compareNumbers(num1, num2):
	if num1 < num2:
		print("The first number is less than the second number.")
	elif num2 < num1:
		print("The first number is greater than the second number.")
	else:
		print("The two numbers are equal!")
		
		
# and we can now use the function:
compareNumbers(3, 11)
compareNumbers(-6, -100)
compareNumbers(5, 5)
	