"""
Owen Danke - Pulverizer Algorithm
1/23/2024
"""

def pulverize(a, b):
	if b > a:
		res = the_pulverizer(b, a, 1, 0, 0, 1)
	else:
		res = the_pulverizer(a, b, 1, 0, 0, 1)

	return res

def the_pulverizer(A, B, X1, Y1, X2, Y2):

	if B == 0:  # base case
		return (X1, Y1)  # Tuple of ___ of d, for d = a(X1) + b(Y1)

	else:  		# inductive case
		q = A // B  # quotient
		r = A % B   # remainder

		next_x2 = X1 - q * X2  # calculate next x2
		next_y2 = Y1 - q * Y2  # calculate next y2
		
		return the_pulverizer(B, r, X2, Y2, next_x2, next_y2)
		
def itrPulverizer(A, B):
	X1 = 1
	Y1 = 0
	X2 = 0
	Y2 = 1

	next_x1 = X2
	next_y1 = Y2

	while B != 0: 
		q = A // B  # quotient
		r = A % B   # remainder

		nX1 = X2
		nY1 = Y2
		
		X2 = X1 - q * X2
		Y2 = Y1 - q * Y2
		
		X1 = nX1
		Y1 = nY1

		A = B
		B = r
		# end of loop
		
	return (A, B, X1, Y1)  # Tuple of ___ of d, for d = a(X1) + b(Y1)

def egcd(a, b):
	if b == 0:
		return a
	else:
		return egcd(b, a % b)


