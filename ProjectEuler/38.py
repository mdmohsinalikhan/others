pandigitals = set()
sums = ''
j = 1
for i in range(2,9999):
	j = 1
	sums = ''
	while True:
		sums = sums + str(i*j)
		#print(sums)
		if len(str(sums)) > 9:
			break
		elif len(str(sums)) == 9:
			if len(set(sums)) == 9:
				if '0' not in set(sums):
					print("i: " + str(i) + " j: " + str(j) + " sums: " + sums)
					pandigitals.add(int(sums))
		j = j+1

print(max(pandigitals))

