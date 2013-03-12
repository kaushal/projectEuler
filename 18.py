import shlex

f = open('numbers.txt', 'r')

dictionary = {}

lineCounter = 0
for line in f:
	dictionary[str(lineCounter)] = []
	for item in shlex.split(line):
		if item is not '\n':
			if item[0] == '0':
				item = item[1:]
			dictionary[str(lineCounter)].append(int(item))
	lineCounter += 1

masterList = []
print dictionary

def recFunc(depth, total, startIndex):
	if depth < 13:
		recFunc(depth + 1, total + dictionary[str(depth + 1)][startIndex], startIndex)
		recFunc(depth + 1, total + dictionary[str(depth + 1)][startIndex + 1], startIndex + 1)
	else:
		masterList.append(total + dictionary[str(depth + 1)][startIndex])
		masterList.append(total + dictionary[str(depth + 1)][startIndex + 1])

recFunc(0, 75, 0)


#print masterList
#print masterList.sort()
#print masterList[-1:][0]
