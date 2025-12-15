#pip install numpy
import numpy as np

print (np.__version__)

# python list - double the frequency
# my_list=[1,2,3,4,5]
# my_list=my_list*2
# print(my_list)

array = np.array([1,2,3,4])

array*=2

print(array)
print(type(array))