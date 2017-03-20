length = {'hundred': 7, 'and': 3, 1: 3, 2: 3, 3: 5, 4: 4, 5: 4, 6: 3, 7: 5, 8: 5, 9: 4, 10: 3, 11: 6, 12: 6, 13: 8, 14: 8, 15: 7, 16: 7, 17: 9, 18: 8, 19: 8}

lengthy = {2: 6, 3: 6 , 4: 5, 5:  5, 6: 5, 7: 7, 8:6, 9: 6}

sum = 0

for i in range(1,1001):
	k = i
	if k == 1000:
		sum = sum + 11
		continue

	if k//100 > 0:
		j = k//100
		sum = sum + length[j]
		sum = sum + length['hundred']
		k = k%100
		if k > 0:
			sum = sum + length['and']
	
	if k//10 > 1:
		j = k//10
		sum = sum + lengthy[j]
		k = k%10
		
	if k > 0:
		sum = sum + length[k]

print("Sum is: " + str(sum))
