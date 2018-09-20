#quadratic.py ev
def roots(a, b, c):

	D = (b*b - 4*a*c)**0.5
	x_1 = (-b + D)/(2*a)
	x_2 = (-b - D)/(2*a)
	
	print('x1: {0}'.format(x_1))
	print('x2: {0}'.format(x_2))
	
	
if __name__ == '__main__':
	a = input('Enter a: ')
	b = input('Enter b: ')
	c = input('Enter c: ')
	roots(float(a), float(b), float(c))

"""
Enter a: 7
Enter b: 19
Enter c: 12
x1: -1.0
x2: -1.7142857142857142
"""
