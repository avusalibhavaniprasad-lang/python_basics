#Area of circle  
radius = float(input("Enter r value:"))
AOC = 3.14*radius**2
print(AOC)
#Area of Triangle
h = float(input("enter height: "))
b = float(input("enter base: "))
AOT = 1/2*h*b
print(AOT)
#simple interest
#(p*r*t)/100
# f -> c (f = (c*9/5)+32)
#km -> m
#m - cm
#cm -> m
#km -> miles
m = int(input("enter the meters: "))
km = m*1000
print(km)
km= int(input("enter the kilometers: "))
m = km/1000
print(m)
cm = int(input("enter the centimeters: "))
m1 = cm * 100
print(m1)
m2 = int(input("enter the meters: "))
cm = m2 / 100
print(cm)
#check whether Even or Odd
number = int(input("enter your number: "))
if number%2==0:
   print("the number even")
else:
   print("the number is odd")
#leap
year = int(input("enter your year: "))
if year%4 == 0:
    print("leap")
# check the  number whether it is positive, negative , zero 
num = int(input("enter num value: "))
if num > 0:
   print("leap") 

x = 28
x = x+89
print(x)
a1 = 28
a1 %=2 
print(a1)
a = 15
b = 1
print(a<<b)
a = 8
b = 15
print(a>>b)
x = [1,2,3,4]
y = x
z = [1,2,3,4]
print(x is y) 
print(x is z) 
