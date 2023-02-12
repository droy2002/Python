import math
a=int(input("Enter 1st side of a triangle: "))
b=int(input("Enter 2nd side of a triangle: "))
c=int(input("Enter 3rd side of a triangle: "))
s=(a+b+c)/2                                     #a!=b!=c
d=(s*(s-a)*(s-b)*(s-c))
area=math.sqrt(d)
print("Area of the traingale is= ", area)