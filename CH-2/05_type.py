
#TYPE() FUNCTION IN PYTHON:

a = 1 # a is integer
f = type(a)
print(f)

b = 0.4
g = type(b)
print(g) # b is floating point number 

c = "harry"
h = type(c)
print(h) # c is string 

d = False
i = type(d)
print(i) # d is a boolean variable

e = None
j = type(e)
print(j) # e is none type variable 


# TYPE CONVERSION: by using the functions of type conversion you can change the type of data type of a particular type of data type if the conversion is valid.

aa = "33.4" # this is offcourse a string variable.
# bb = type(aa)
# print(bb)
# till here the type of aa is showing me sting which is correct.
# however to do type conversion we use the below function.
cc = float(aa) # string to float conversion.
bb = type(cc)
print(bb)

 