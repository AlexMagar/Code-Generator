import platform
import random as rn
# Fibonacci Series
# 0 1 1 2 3 5 8 13.... 

a,b = 0,1
while b<100:
    print(a, end=" ")
    c=a+b
    a,b=b,c
print() #endline

print('This is python version {}'.format(platform.python_version()))

print(rn.randint(0,23))