import numpy as np


# array=np.array([1,2,3,4])

# # #Scalar Arithmatic

# # print(array+1)
# # print(array-2)
# # print(array*2)
# # print(array/3)
# # print(array**3)



# # #Vectorized Math Funcs

# # print(np.sqrt(array))
# # print(np.round(np.sqrt(array)))
# # print(np.ceil(np.sqrt(array)))
# # print(np.pi)


# radii=np.array([1,2,3,4])

# print(np.pi*radii**2)




# #Element Wise Arithmatic

# arr1=np.array([1,2,3])
# arr2=np.array([4,5,6])

# print(arr1+arr2)
# print(arr1-arr2)
# print(arr1*arr2)
# print(arr1/arr2)
# print(arr1**arr2)



#Comparison Operator

scores=np.array([91,55,100,73,82,64])

print(scores==100)
print(scores>=60)
print(scores<60)

scores[scores<60]=0
print(scores)