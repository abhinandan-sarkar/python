import math
#print(dir(math))

#factoral function
print(math.factorial(3)) #--->6

#math gcd function
print(math.gcd(12,27)) #--->3

#math pow function
print(math.pow(2,3))  #---->8.0

# pi value 
print(math.pi)

# *** truncated ***
print(math.trunc(-99.29)) #---
print(math.trunc(32.29))

# sqrt
print(math.sqrt(64)) #---> 8.0

# remainder 
print(math.remainder(9,2))  #--->1

# prod  returns of all product of all the elements in an iterable
x=[1,2,3,5]
x=(5,6,7,8)
x={1,2,3,4}

print(math.prod(x))

# isclose
print(math.isclose(1.233, 1.4566))
print(math.isclose(1.233, 1.233))
print(math.isclose(1.233, 1.24))



