import numpy as np
# creating an array.

# 1D array
num1 = np.array([1,2,3,4,5,8])
print(num1)

# 2D array
num2 = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(num2)

# methods and operations in numpy python:
# ndim:
print(num1.ndim)

# shape():
print(num1.shape)

# size():
print(num1.size)
print(num2.size)

# dtype():
print(num1.dtype)
print(num2.dtype)

# creating array using numpy methods:
# zero():
print(np.zeros(8))

# ones():
print(np.ones(5))

# arange():
print(np.arange(1,10,2))

# linspace():
print(np.linspace(0,1,5))

# mathematical operations():
arr = np.array([1,2,3,4,5,6,7,8,9,10])
print(arr+10)
print(arr*8)
print(arr/28)
print(arr//8)

# multi-dimentional arrays(matrix operation):
mat1 = np.array([[1,2,3],[4,5,6],[7,8,9]])
mat2 = np.array([[9,8,7],[6,5,4],[3,2,1]])
print(mat1+mat2)
print(mat1-mat2)
print(mat1*mat2)

# dot():
print(np.dot(mat1,mat2))