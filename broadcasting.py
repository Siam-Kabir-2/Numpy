import numpy as np

# Broadcasting allows NumPy to perform operations on arrays
# with different shapes by virtually expanding dimensions
# so they match the larger array's shape.

# The dimensions have the same size.
# OR
#One of the dimensions has a size of 1.


# arr1=np.array([[1,2,3,4]])
# arr2=np.array([[1],[2],[3],[4]])
# arr3=np.array([[1,2,3,4],[5,6,7,8]])
# arr4=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])

# print(arr1.shape)
# print(arr2.shape)
# print(arr3.shape)
# print(arr4.shape)


# print(arr1*arr2)
# print(arr3*arr1)
# print(arr3*arr4) #no dimension matched, so will not execute



array1=np.array([[1,2,3,4,5,6,7,8,9,10]])
array2 = np.array([[1],[2],[3],[4], [5],[6],[7],[8],[9],[10]])

print (array1.shape)
print (array2.shape)

print(array2*array1)