import numpy as np

array=np.array([[['A','B','C'],['D','E','F'],['G','H','I']],
                [['A','B','C'],['D','E','F'],['G','H','I']],
                [['A','B','C'],['D','E','F'],['G','H','I']]])

#gives array dimension
print(array.ndim) 

#gives the shape of the dimensions like size of elements (like height,width,length)
print(array.shape) 

#chain indexing
print(array[0][0][0])

#multidimensional indexing (Faster than chain)
print(array[1,2,0])

word=array[0,0,0]+array[1,2,1]+array[1,2,1]
print(word)