f = 0
f_p = 1
f_p_p = 1
i = 2

while 5 == 5:
	i = i + 1
	f = f_p + f_p_p
	f_p_p = f_p
	f_p = f
	if len(str(f)) == 1000:
		print("The result is:" + str(i))
		break
	else:
		print("The length of fibonacchi term " + str(i) + " is " + str(len(str(f))))

