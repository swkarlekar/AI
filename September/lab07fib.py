from time import clock;
dict = {1:1, 2:1}

def main(): 
   n = 100000; start = clock()
   print('1. fib1(',n,') = ',fib1(n))
   print('   time =', round(clock()-start, 6), 'seconds')
  # n = 100000; start = clock()
   #print('1. fib2(',n,') = ',fib2(n))
   #print('   time =', round(clock()-start, 1), 'seconds')
   n = 100000; start = clock()
   print('1. fib3(',n,') = ',fib3(n))
   print('   time =', round(clock()-start, 6), 'seconds')
  # n = 100000; start = clock()
   #print('1. fib4(',n,') = ',fib4(n))
  # print('   time =', round(clock()-start, 1), 'seconds')
  # n = 100000; start = clock()
  # print('1. fib5(',n,') = ',fib5(n))
  # print('   time =', round(clock()-start, 1), 'seconds')
   #n = 100000; start = clock()
   #print('1. fib6(',n,') = ',fib6(n))
   #print('   time =', round(clock()-start, 1), 'seconds')
   #n = 100000; start = clock()
   #print('1. fib7(',n,') = ',fib7(n))
   #print('   time =', round(clock()-start, 1), 'seconds')
   #n = 100000; start = clock()
   #print('1. fib8(',n,') = ',fib8(n))
   #print('   time =', round(clock()-start, 1), 'seconds')

def fib1(n):  
    a = 1
    b = 1
    c = 1
    for i in range(2,n):
      c = a + b
      a = b
      b = c
    return c
def fib2(n):
   if n<3: return 1
   return fib2(n-2)+fib2(n-1)
def fib3(n): 
   if n<3:
      return 1
   a = 1
   b = 1
   for i in range(1,n):
      if i%2 == 0: 
         a = a + b
      else: 
         b = a + b
   if n%2 == 0:
      return a
   return b
def fib4(n):
    lst = [1,1,2,3,5,8,13,21,34,55,89,144]
    if n < len(lst):
      return lst[n-1]
    return fib4(n-2)+fib4(n-1)
def fib5(n): 
   return [1,1,2,3,5,8,13,21,34,55,89,144][n-1]
def fib6(n):
   if n in dict:
      return dict[n]
   dict[n] = fib6(n-1)+fib6(n-2)
   return dict[n]
def fib7(n):
   import math
   phi = float(1 + math.sqrt(5))/2
   return (phi**n-((-1)**n/phi**n))/math.sqrt(5)   
def fib8(n):
   from decimal import Decimal, getcontext
   import math
   if n>70:
      getcontext().prec = 2*n
   phi1 = math.pow((1 + math.sqrt(5))/2, n)
   phi2 = math.pow((1 - math.sqrt(5))/2, n)
   return (phi1 - phi2)/math.sqrt(5)
main()