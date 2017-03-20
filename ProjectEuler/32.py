pandigitals = set()
sums = ''
for i in range(1,999999):
	sums = ''
	for j in range(i,999999999):
		sums = str(i*j) + str(i) + str(j)

		if len(str(sums)) > 9:
			break
		elif len(str(sums)) == 9:
			if len(set(sums)) == 9:
				if '0' not in set(sums):
					print("i: " + str(i) + " j: " + str(j) + " i*j: " + str(i*j))
					pandigitals.add(int(i*j))

print(sum(pandigitals))
