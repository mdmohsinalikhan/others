desired_numbers = set()
factorial = {9:362880, 8:40320, 7:5040, 6:720, 5:120, 4:24, 3:6, 2:2, 1:1, 0:1}
sums = 0
i = 98
#print(factorial[int(str(i)[0])] + factorial[int(str(i)[1])])
for i in range(10,1000001):
	sums = 0
	for j in range(0,len(str(i))):
		sums = sums + factorial[int(str(i)[j])]

	if sums == i:
		desired_numbers.add(i)

print(sum(desired_numbers))
