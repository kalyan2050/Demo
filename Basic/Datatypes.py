''' DATA TYPES
Data Type represents the type of data present inside a variable.
In Python we are not required to specify the type explicitly. Based on value provided,
the type will be assigned automatically.Hence Python is dynamically Typed Language.
Python contains the following inbuilt data types
to get address of object.
1) Int
2) Float
3) Complex
4) Bool
5) Str
6) Bytes
7) Bytearray
8) Range
9) List
10) Tuple
11) Set
12) Frozenset
13) Dict
14) None
Note: Python contains several inbuilt functions
1) type()--> to check the type of variable
2) id() --> to get address of object
3) print() -->to print the value

'''




a = 10
print(type(a))
print(a)


f = 1.234
print(type(f))
print(f)

c = 3 + 5j
print(c.real)
print(c.imag)

b = True
print(type(b))
print(b)

s1 = 'kalyan'
print(type(s1))
print(s1)

#Slicing of Strings:
print(s1[0])

'''
TYPE CASTING
֍ We can convert one type value to another type. This conversion is called Typecasting 
or Type coersion.
֍ The following are various inbuilt functions for type casting.
1) int()
2) float()
3) complex()
4) bool()
5) str()
'''

print("***********     TYPE CASTING      **********")

print("***********     Float to Int Type      **********".format(f))

print(type(int(f)))