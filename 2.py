def fib(n):
	if n <= 1:
		return n
	else:
		return (fib(n-1) + fib(n-2))

tempNum = 0
fibNum = 0
count = 1
while tempNum <= 4000000:
	if tempNum % 2 == 0:
		fibNum = fibNum + tempNum
	tempNum = fib(count)
	count += 1
print fibNum

