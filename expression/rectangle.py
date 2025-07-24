import math
a = float(input('enter a'))
b = float(input('enter b'))
c = float(input('enter c'))
r1 = (-b + math.sqrt(b**2 - 4 * a * c)) / (2 * a)
r2 = (-b - math.sqrt(b**2 - 4 * a * c)) / (2 * a)
print('r1 and r2 are ', r1,r2)