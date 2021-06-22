a=[1,2,3]
b=a[:]
a[1]=4
print(a)
print(b)

print("="*15)

from copy import copy
a=[1,2,3]
b=copy(a)
print(a)
print(b)
print(id(a))
print(id(b))