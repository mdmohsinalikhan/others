

import itertools

digits = list()

for i in range(0,10):
	digits.append(str(i))

s=''

sums = 0


for p in itertools.permutations(digits):
	s = "".join(p)	
	if int(s[1:4])%2 == 0 and int(s[2:5])%3 == 0 and int(s[3:6])%5 == 0 and int(s[4:7])%7 == 0 and int(s[5:8])%11 == 0 and int(s[6:9])%13 == 0 and int(s[7:10])%17 == 0:
		print(s)
		sums = sums + int(s)

print(sums)
