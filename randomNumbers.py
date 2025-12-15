import numpy as np

rng=np.random.default_rng()
# rng1=np.random.default_rng(seed=1) #seed will save the generated random number


# #(start,end(exclusive))
# print(rng.integers(low=1,high=777,size=(3,2)))
# print(rng1.integers(low=1,high=777,size=(3,2)))


# np.random.seed(seed=1)

# #floating rand num
# print(np.random.uniform(low=-1,high=1,size=(3,3)))


#Shuffling


array=np.array([1,2,3,4,5])
rng.shuffle(array)
print(array)

fruits=np.array(["apple",'orange','banana','coconut'])
fruits=rng.choice(fruits,size=3)
print(fruits)