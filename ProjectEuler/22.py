f = open('input.txt', 'r')
s = f.readline()

names = s.split('","')

names[0] = names[0][1:]
names[len(names)-1] = names[len(names)-1][:6]

names.sort()

weight = 0
result = 0

for i in range(0,len(names)):
	print(names[i])
	weight = 0
	for j in range(0,len(names[i])):
		print(ord(names[i][j])-64)
		weight = weight + ord(names[i][j])-64
	result = result + weight*(i+1)

print(result)

