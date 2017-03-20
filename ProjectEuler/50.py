
primes = set()

for i in range(2,1000001):
	primes.add(i)


for i in range(2,1001):
	for j in range(2,1000001):
		if i*j < 1000001:
			primes.discard(i*j)
		else:
			break

primes_list = list()

primes_list = list(primes)

primes_list.sort()

print(len(primes_list))

sums = 0
maxlength = 0
maxstarting = 0

for starting in range(0,len(primes_list)):
	sums = 0
	for i in range(starting,len(primes_list)):
		sums = sums + primes_list[i]
		if sums < 1000000:
			if sums in primes:
				if i-starting+1 > maxlength:
					maxlength = i-starting+1
					maxstarting = starting


		else:
			break

sums = 0
for i in range(maxstarting,maxstarting+maxlength):
	sums = sums + primes_list[i]
	print(primes_list[i])
	

print(maxlength)
print(sums)
