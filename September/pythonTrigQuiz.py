'''
######################
|Sweta Karlekar Pd 4 |
|10/21/14            |
######################
'''
from math import sqrt, sin, cos, tan, asin, acos, atan, atan2, degrees, radians,  pi
x = (1+sqrt(5))/2
y = (x-1)/(x*x-x+1)
z = round(y-cos(radians(72)),3)
w = round(degrees(atan(sqrt(3))), 3)
theta = atan2(4,3)
phi = atan2(3,4)
print('ans1 = ', z)
print('ans2 = ', w)
print('ans3 = ', round(phi, 2))
print('ans4 = ', round(sin(theta)-cos(phi), 2))
print('ans5 = ', round(sin(theta+phi)+cos(w), 1))