no_of_solutions = list()
triple = set()
set_of_triples = set()

for i in range(0,1001):
	no_of_solutions.append(0)

for i in range(0,1001):
	for j in range(i//3,i//2):
		for k in range(1,j-1):
			if j*j == k*k + (i-j-k)*(i-j-k):
				print("For perimeter: " + str(i) + " hyptenous: " + str(j) + " lombo: " + str(k) + " bhumi: " + str(i-j-k))
				no_of_solutions[i] = no_of_solutions[i] + 1
				break

maxs = 0
maxindex = -1
for i in range(0,1001):
	if no_of_solutions[i] > maxs:
		maxs = no_of_solutions[i]
		maxindex = i

print("Maximum solutions: " + str(maxs) + " for perimeter: " + str(maxindex))
