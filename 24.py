import math

intermediate = 1000000
numbersLeft = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in range(9, -1, -1):
	digit = math.floor(intermediate / math.factorial(i))
	print numbersLeft[int(digit)]
	numbersLeft.pop(int(digit))
	intermediate -= math.factorial(i) * digit

#for x in range(1000000 - lastNumber):

