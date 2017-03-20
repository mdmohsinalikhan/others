sums = list()
abandunt_numbers = list()
desired_numbers = list()
outputset = set()

sums.append(0)
sums.append(0)

desired_numbers.append(0)
desired_numbers.append(0)

print("The program will take few minutes to terminate to process all the numbers below 28124")

for i in range(2,28124):
	sums.append(1)
	desired_numbers.append(0)

for i in range(2,28124):
	if i%1000 == 0:
		print("Already processed upto " + str(i) + " numbers")
	for j in range(2,28124):
		if i*j < 28124:
			sums[i*j] = sums[i*j] + j
		else: break

for i in range(2,28124):
	if i < sums[i]:
		abandunt_numbers.append(i)

print("Finding the numbers which are sums of two abandunt numbers below 28124")
for i in range(0,len(abandunt_numbers)):
	for j in range(i,len(abandunt_numbers)):
		if abandunt_numbers[i] + abandunt_numbers[j] < 28124:
			desired_numbers[abandunt_numbers[i] + abandunt_numbers[j]] = 1

print("Finding the numbers which are not sums of two abandunt numbers")
for i in range(0,28124):
	if desired_numbers[i] !=1:
		outputset.add(i)

print("Computing the desired sum")
result = 0
for i in outputset:
	result = result + i

print("The final result is: " + str(result))
