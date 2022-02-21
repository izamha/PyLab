import numpy as np

a = np.array(42)
b = np.array([1, 2, 3, 4, 5])
c = np.array([[1, 2, 3], [4, 5, 6]])
d = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])

print(a)
print(b)
print(c)
print(d)

'''
    An array can have any number of dimensions.
    When created, you can define the number of by using ndmin=5
'''

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('Number of dimensions', arr.ndim)

# Access Array Elements

arr = np.array([1, 2, 3, 4])
print(arr[1] + arr[3])

# Access 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st dim: ', arr[0, 1])

# Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

# Access the third element of the second array of the first array
print(arr[0, 1, 2])

# Slicing arrays
# [start:end]
# [start:end:step]

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

# Slicing elements from index 4 to the end of the array
print(arr[4:])

# Negative Slicing
print(arr[-3:-1])
# Checking the datatype of an array
print(arr.dtype)

arr_string = np.array(['apple', 'Banana', 'Cherry'])
print(arr_string.dtype)
