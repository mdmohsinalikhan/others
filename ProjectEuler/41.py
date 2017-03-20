import itertools


def checkifprime(p):
	if p < 2:
		return False
	for i in range(2,p-1):
		if p%i == 0:
			return False
	
	return True

digits = list()

s=0
maxs = 0


for i in range(1,10):
	del digits[:]
	for j in range(1,i+1):
		digits.append(str(j))
	
	for p in itertools.permutations(digits):
		s = int("".join(p))
		if checkifprime(s) == True:
			print(s)
			if s > maxs:
				maxs = s


print(maxs)	  
	

