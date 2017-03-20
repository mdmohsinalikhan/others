
sums = 0
maxsums = 0
s = ''
for a in range(1,100):
	for b in range(1,100):
		s = str(a**b)
		sums = 0
		for i in range(0,len(s)):
			sums = sums + int(s[i])
			if sums > maxsums:
				maxsums = sums 

print(maxsums)
