import math
#PAGE 1
print('1.', True, True) 
print('2.', 2 < 3, True) 
print('3.', True-1, 0)
print('4.', (2<3)+1, 2) 
print('5.', not 7, False) 
print('6.', 2<3 and 3>4, False) 
print('7.', 2<3 or 3/0==4, True)
print('8.', True == 1, True)
print('9.', True == 3, False)## True is assigned a numeric value of 1
print('10.', False == 0, True)
print('11.', 1<2<3, True)
print('12.', 1<2 and 2<3==2-1, False)##compound, 2<3 and 3==(2-1), unary comes first (2-1)
print('13.', 1<2 and 2<3==4-1, True)##compound, 2<3 and 3==(4-1), unary comes first (4-1)
print('14.', 1<2 and 2<3==True, False)##compound, 2<3 and 3==True
print('15.', 1<2 and 2<3==False, False)
a = 1; b = 2; c = 3; d = 4; e = 5
print('16.', a<b<c==d-1, True)##compound chain, a<b and b<c and c==(d-1), unary comes first (d-1)
print('17.', a<b<c==e-1, False)##compound chain, a<b and b<c and c==(e-1), unary comes first (e-1)
print('18.', False+1+2<3+1, True)##(0+1+2)<(3+1)

#PAGE 2
print(1 or 1<2, 1)
print(True or 1<2, True)
print(0 or 'Hello!' or True, 'Hello!')
print(1 and -1 or 2, -1)
print(1<2 and True, True)
print(1<2 and 1, 1)
print(0 or [] or () or None, None)
print(True, True)
print(2<3, True)
print(True-1, 0)
print((2<3) + 1, 2)
print(not 7, False)
print(2<3 and 3>4, False)
print(2<3 or 3/0==4, True)
print(True == 1, True)
print(True == 3, False)
print(False == 0, True)
print(False == 3, False)
print(1<2<3, True)
print(1 < 2 and 2<3 == 4-1, True)
print(1 < 2 and 2<3 == 2-1, False)
print(1<2 and 2<3==True, False)
a=1; b =2; c=3; d=4; e=5
print(a<b<c == d-1, True)
print(a<b<c == e-1, False)
print(False+1+2<3+1, True)
print(bin(35))


