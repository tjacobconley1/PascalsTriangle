# PASCALS TRIANGLE
# Author: Tyler Conley

# Pascal's triangle is a never ending equilateral triangle
# of numbers that follow a rule of adding the two numbers
# above to get the number below

# The Binomial Theorem:
# (a + b)^n = the summation from 0 to n as a polynomial
# the coefficients of the polynomial will be the pascal triangle
# so....
#
#         (x + y)^0 = 1
#
#  and
#
#         (x + y)^n = x^n + nxy + y^n
#



import numpy as np
import math

# iteration variables
i = 0
j = 0

# array size scaler
scale = int(input("how many iterations? ->"))

# create blank array of size 'scale'
pascalgrid = np.zeros((scale, scale))

for i in range(scale):
    for j in range(scale):
        pascalgrid[i][j] = ((i + j)^scale)

print(pascalgrid)



