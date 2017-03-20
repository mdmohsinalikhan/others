def checkifprime(p):

	if p < 2:
		return False
	
	for i in range(2,p-1):
		if p%i == 0:
			return False
		
	return True


primes = set()

for i in range(2,1000000):
	primes.add(i)

for i in range(2,1001):
	for j in range(i,1000000):
		if i*j < 1000000:
			primes.discard(i*j)
		else:
			break
digits = set()
p = ''
flag = True
circularprimes = set()

for i in primes:
	print(i)
	digits = set(str(i))
	if i != 2:
		if '2' in digits or '4' in digits or '6' in digits or '8' in digits or '0' in digits:
			continue
	flag = True
	for j in range(0,len(str(i))-1):
		p = int(str(i)[j+1:len(str(i))] + str(i)[0:j+1])
		#print(int(p))
		if checkifprime(p) != True:
				flag = False
				break

	if flag == True:
		circularprimes.add(i)

print(circularprimes)
print(len(circularprimes)) 

