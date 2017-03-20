result = 1
sum = 0
for i in range(1,101):
	result = result*i

while result > 0:
	sum = sum + result%10
	result = result//10

print('Sum is: ' + str(sum))
