# Using NumPy create random vector of size 20 having only float in the range 1-20.
# Then reshape the array to 4 by 5
# Then replace the max in each row by 0 (axis=1)
# (you can NOT implement it via for loop)


import numpy as np 

sampl=np.random.uniform(low=1,high=20,size=20)

reshape_arr=sampl.reshape(4,5)

np.where(reshape_arr== np.max(reshape_arr, axis=1, keepdims=True), 0, reshape_arr)
