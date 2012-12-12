from galua import *

a = galua('00101011')
b = galua('00011110')
c = galua('1101')
print(a + b)
print(a * b)
print(a * b % c)
d = galua('1100010010')
e = galua('100011011')
print(d % e)
muls('1101', '100011011')
