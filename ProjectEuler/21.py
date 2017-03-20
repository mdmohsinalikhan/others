sums = list()
amicables = set()
i = 0
j = 0
k = 0


for i in range(0,10001):
	sums.append(0)

for i in range(1,10001):
	j = i
	k = 2
	while k*j < 10001:
		sums[k*j] = sums[k*j] + j
		k = k+1

for i in range(2,10001):
	if sums[i] < 10001:
		if i == sums[sums[i]] and i != sums[i]:
			amicables.add(i)
			amicables.add(sums[i])

result = 0

for i in amicables:
	result = result + i
	print("sums[" + str(i) + "]: " + str(sums[i]))


print amicables

print("The final result is:" + str(result))




