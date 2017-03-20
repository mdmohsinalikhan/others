desired_numbers = set()
decimal = ''
decimal_reverse = ''
binary = ''
binary_reverse = ''
for i in range(0,1000000):
	decimal = str(i)
	decimal_reverse = str(i)[::-1]
	binary = str(bin(i))[2:]
	binary_reverse = str(bin(i))[2:][::-1]
	if decimal == decimal_reverse and binary == binary_reverse :
		desired_numbers.add(i)
		print("decimal:" + decimal + " decimal reverse: " + decimal_reverse + " binary: " + binary + " binary reverse: " + binary_reverse)


print(sum(desired_numbers))
