#I figured that the number has to be a multiple of 2520 since, 2520 is the 
# first number divisible by 1-10, and also must be 1-20
list = [11, 12, 13, 14, 15, 16, 17, 18, 19, 20]

def divisible(number):
	for item in list:
		if not number % item == 0:
			return False
	return True


number = 2520
count = 1

while divisible(number) is False:
	number = 2520 * count
	count = count + 1
print number
