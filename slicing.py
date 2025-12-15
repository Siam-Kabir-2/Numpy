import numpy as np

array=np.array([[1,2,3,4],
                [5,6,7,8],
                [9,10,11,12],
                [13,14,15,16]])


#array[start:end(exclusive):step]

#row selection
# print(array[0])
# print(array[0:4])
# print(array[0:4:2])
# print(array[::2])
# print(array[::-1]) # prints reverse order


#column selection
print(array[:,0])
print(array[:,2])
print(array[:,-1])
print(array[:,0:3]) #first three columns
print(array[:,:]) #All columns
print(array[:,::2])
print(array[:,::-1])


#row and column selection

print(array[0:2,2:4])
print(array[2:4,0:2])