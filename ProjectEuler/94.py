import math

#340000000
perimeters = set()

sums = 0

for i in range(2,340000000):
	if i % 10000000 == 0:
		print("Finished" + str(i))
	if 3*i + 1 <= 1000000000:
		x = math.sqrt(i*i - ((i+1)/2)*((i+1)/2)) 
#		if x == round(x):
		x = round(x)
		if (x-1)*(x-1) + ((i+1)/2)*((i+1)/2) == i*i:
			print("i+1: " +  str(i+1) + " x: " +  str(x-1) ) 
			sums = sums + 3*i + 1
		elif (x)*(x) + ((i+1)/2)*((i+1)/2) == i*i:
			print("i+1: " +  str(i+1) + " x: " +  str(x) ) 
			sums = sums + 3*i + 1
		elif (x+1)*(x+1) + ((i+1)/2)*((i+1)/2) == i*i:
			print("i+1: " +  str(i+1) + " x: " +  str(x+1) ) 
			sums = sums + 3*i + 1
			

#print(perimeters)

print(sums)
