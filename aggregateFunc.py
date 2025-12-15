import numpy as np

#Aggregate Functions = summarize data and typically return a single value

array=np.array([[1,2,3,4,5],
                [6,7,8,9,10]])

# print(np.sum(array))
# print(np.mean(array))
# print(np.std(array))#standard deviation
# print(np.var(array))#square of std
# print(np.min(array))
# print(np.max(array))
# print(np.argmin(array))#index of min
# print(np.argmax(array))#index of max

print(np.sum(array,axis=0)) # all columns
print(np.sum(array,axis=1)) # all rows