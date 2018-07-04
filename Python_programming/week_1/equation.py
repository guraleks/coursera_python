import sys

a = int(sys.argv[1])
b = int(sys.argv[2])
c = int(sys.argv[3])
 
discr = b**2 - 4 * a * c;

if discr > 0:
	import math
	x1 = int((-b + math.sqrt(discr)) / (2 * a))
	x2 = int((-b - math.sqrt(discr)) / (2 * a))
	print(x1)
	print(x2)
elif discr == 0:
	x = -b / (2 * a)
	print(x)
else:
	print("Корней нет")
