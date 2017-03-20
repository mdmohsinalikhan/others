s1 = dict()
s2 = dict()
s3 = dict()
s4 = dict()
s5 = dict()
s6 = dict()

i = 2
while True:

	s1.clear()
	s2.clear()
	s3.clear()
	s4.clear()
	s5.clear()
	s6.clear()

	print(i)

	k = i
	for j in range(0,len(str(k))):
		if str(k)[j] in s1:
			s1[str(k)[j]] = s1[str(k)[j]] + 1
		else:
			s1[str(k)[j]] = 1

	k = 2*i
	for j in range(0,len(str(k))):
		if str(k)[j] in s2:
			s2[str(k)[j]] = s2[str(k)[j]] + 1
		else:
			s2[str(k)[j]] = 1

	k = 3*i
	for j in range(0,len(str(k))):
		if str(k)[j] in s3:
			s3[str(k)[j]] = s3[str(k)[j]] + 1
		else:
			s3[str(k)[j]] = 1

	k = 4*i
	for j in range(0,len(str(k))):
		if str(k)[j] in s4:
			s4[str(k)[j]] = s4[str(k)[j]] + 1
		else:
			s4[str(k)[j]] = 1

	k = 5*i
	for j in range(0,len(str(k))):
		if str(k)[j] in s5:
			s5[str(k)[j]] = s5[str(k)[j]] + 1
		else:
			s5[str(k)[j]] = 1

	k = 6*i
	for j in range(0,len(str(k))):
		if str(k)[j] in s6:
			s6[str(k)[j]] = s6[str(k)[j]] + 1
		else:
			s6[str(k)[j]] = 1

	if s1 == s2 == s3 == s4 == s5 == s6:
		print("i: " + str(i) + " 2*i: " + str(2*i) + " 3*i:" + str(3*i) + " 4*i: " + str(4*i) + "5*i:" + str(5*i) + "6*i:" + str(6*i))
		break


	i = i + 1
