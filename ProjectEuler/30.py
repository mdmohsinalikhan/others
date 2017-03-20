desired_numbers = set()
sums = 0

for i in range(2,999999):
	sums = 0
	for j in range(0,len(str(i))):
		sums = sums + int(str(i)[j])**5
	
	if sums == i:
		desired_numbers.add(i)

print(sum(desired_numbers))

print(desired_numbers)
