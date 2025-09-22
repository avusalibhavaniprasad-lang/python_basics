def greet(): 
    print("Hello World")
greet()

# types of functions arguements:
# 1.positional Arguments:
def greet(rollno,name):
    print("Hello",name,",Your rollno is",rollno)
greet("L4","Prasad")

# 2.keyword arguments:
def greet(rollno,name):
    print("Hello",name,",your rollno is",rollno)
greet(name="Prasad",rollno="L4")

# 3.default arguments:
def greet(rollno,name="student"):
    print("Hello",name,",your rollno is",rollno)
greet(rollno="L4")
greet(name="Prasad",rollno="L4")

# 4.variable-length arguments:
# 1st. *:(variable-length arguments):
L = [10,20,30,40,50]
def summ(*L):
    print(sum(L))
summ(10,20,30,40,50)
# 2nd. **(keyword variable-length arguments):
def data(**info):
    for key,value in info.items():
        print(key,":",value)
data(name="Prasad",rollno="L4",branch="CSE.CS")

# scope of the variable:
x = 10
print("x=10 is global")
print("y=5 is local")
def test():
    y = 5
    print("inside function:",x,y)
test()
print("outside function:",x)

# Lambda functions:
# normal function for squaring a number:
def sqe(x):
    print(x*x)
sqe(5)
# lambda function for squaring a number:
squ = lambda x: x*x
print(squ(5))   

# recursive function:

def factorial():
    fact = 1
    for i in range(8,0,-1):
        fact = fact * i
    print(fact)
factorial()

def Rfactorial(n):
    if n == 0:
        return 1
    else:
        return n * Rfactorial(n-1)
print(Rfactorial(5))
        
# 1.MAP():
numbers = [1,2,3,4,5]
squ = list(map(lambda x:x*x, numbers))
print(squ)

# filter():
numbers = [1,2,3,4,5]
squ = list(filter(lambda x:x%2 == 0, numbers))
print(squ)

# reduce():
from functools import reduce
numbers = [1,2,3,4,5]
squ = reduce(lambda x,y:x+y, numbers)
print(squ)

# write a function to check wheather it is even or odd:
def check(n):
    if n<0:
        print("positive")
    else:
        print("negative")
check(-1)
check(2)
check(+64)
check(-88)

# write a function to check wheather the number is positive,negative,zero:
def check(n):
    if n>0:
        print("+ve")
    elif n<0:
        print("-ve")
    else:
        print("zero")
check(-1)
check(2)
check(+64)
check(0)

# write a function to check the largest number amoung three numbers:
a,b,c = 8,6,3
a>b , a<b
print(a>b,a<b)

