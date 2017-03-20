months = {1: 31, 2: 28, 3: 31, 4: 30, 5: 31, 6: 30, 7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31}
daycount = 0
days = {0: 'Mon', 1: 'Tue', 2: 'Wed',3: 'Thu',4: 'Fri',5: 'Sat',6: 'Sun',}
y = 1900
m = 0
d = 0
sunday_count = 0

y = 1901

while y < 2001:
	if y % 4 == 0:
		if y%100 != 0:
			months[2] = 29
		
		if y%100 == 0 and y % 400 == 0:
			months[2] = 29
	else:
		months[2] = 28

	m = 1
	while m < 13:
		d = 0 
		while d <= months[m]:
			d = d+1
			if d <= months[m]:
				daycount = daycount+1
			if d == 1 and daycount%7 == 6:
				print('Today is: ' + str(d) + '-' + str(m) + '-' + str(y) + ' :' + days[daycount%7] )
				#print('here is daycount: ' + str(daycount))
				sunday_count = sunday_count + 1

		m = m +1

	y = y+1

print('Sundays: ' + str(sunday_count))
