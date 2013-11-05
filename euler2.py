a, b, total = 0, 1, 0

while 2:
	a, b = b, a+b
	if(b > 40000000):
		break
	if(b%2 == 0):
		total = total + b
print b