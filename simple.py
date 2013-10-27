#This is going to be my first python script
num = int(raw_input("How many Fib numbs?:"))
print num


x = 0
a, b = 0, 1
while x < num:
	a, b = b, a + b
	print b
	x = x + 1
print "And this is the end of the script. We found fib #", num