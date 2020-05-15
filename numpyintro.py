import numpy as np
#Create array of 10 zeros
np.zeros(10)
#Create array of 10 ones
np.ones(10)
#Create an array of 10 5's
np.ones(10) * 5
#Create array of integers from 10 - 50
np.arange(10, 51)
#Create array of even integers from 10 - 50
np.arrange(10, 51, 2)
#Create 3x3 matrix with values from 0 to 8
np.arange(9).reshape(3,3)
# Create 3x3 identity matrix
np.eye(3)
# numpy to generate random number between 0 and 1
np.random.rand(1)
# use numpy to generate 25 numbers sampled from a normal distribution
np.random.randn(25)
###
np.arange(1,101).reshape(10,10) / 100 #    or      np.linspace(0.01,1,100).reshape(10,10)
# Array of 20 linearly spaced points between 0 and 1
np.linspace(0, 1, 20)
# given mat = np.arange(1, 26).reshape(5,5)
# create slices
mat[2:,1:]
mat[3,4]
mat[0:3,1].reshape(3,1) # or mat[0:3,1:2]

