# Tuples: Tuples are collection datatypes which are used to store multiple values in a single variable.

# example:
T = (10,20,30)
print(T)
print(type(T))

# Creating a tuple:
# Empty tuple:
E = ()
# tuple with numbers:
T = (10,20,30)
# tuple eith string:
St = ("A","B","C","a","b","c")
# tuple with mixed datatypes
M = (10,10.5,"hi",True,"False")
# Tuple with a single value
S = (10,) # Tuple
a = 10 #int
b = [10] #list
print(type(S))
print(type(a))
print(type(b))

# Accessing an element from the tuple.
A = (10,20,30,40,50)
#i    0  1  2  3  4  
#i   -5 -4 -3 -2 -1
print(A[0]) 
print(A[1]) 
print(A[2]) 
print(A[3]) 
print(A[4]) 
print(A[-1]) 
print(A[-2]) 
print(A[-3]) 
print(A[-4]) 
print(A[-5]) 

# Slicing the tuple:
A = (10,20,30,40,50)
print(A[1:4])
print(A[:3])

# Changing the values:
A = [10,20,30,40,50]
A[2] = 80
print(A)

# Mathematical operations
# Concentration:
t1 = (1,2,3)
t2 = (4,5)
c = t1+t2
print(c)
# Repetition
t1 = (1,2,3)
c = t1*3
print(c)

# Searching and Checking:
# in operator:

SC = ("Mrcet","Mrec","Mrce") 
print("Mrcet" in SC)
print("Mrcet" not in SC)

# index():
# Count():
T1 = (2,4,4,4,6,8,10,13,14)
print(T1.index(4))
print(T1.count(4))

# len,max,min,sum
T1 = (2,4,4,4,6,8,10,12,14)
print(len(T1))
print(max(T1))
print(min(T1))
print(sum(T1))

#nested tuple:
N = (1,2,(3,4),(5,6))
print(N[2][1])

# iterate the tuple using for loop.
T1 = (2,4,4,4,6,8,10,12,14)
for i in T1:
    print(i)

# Sum of all elements in the tuple.
a = (28,56,42,89,88)
print(sum(a))   

# find the length of the tuple without using len().
T1 = (2,4,4,4,6,8,10,12,14)
length = 0
for i in T1:
    length += 3
print(length) 

# Multiply each element with 2 in the list
T1 = (2,4,4,4,6,8,10,12,14)
multiple = 2
for i in T1:
    multiple *= 2
print(multiple)


