# this script tests polynomial regression
# numpy stuff
import numpy as np
from numpy.linalg import svd 
from numpy.linalg import norm

# matplotlib stuff
import matplotlib as mp
from matplotlib import rc
import matplotlib.pyplot as plt

# import our own functions 
from poly_func import *

# turns on Tex for plotting
rc('text', usetex=True)
rc('font', family='serif')

# set random seed to ensure reproducible pseudorandom behavior
np.random.seed(3)

# plotting parameters
func_lwidth = 3

# load weight vector for 20-degree polynomial 
weights = np.load('poly_weights.npy')

# create data evaluations
degree = 20
nsamp = 500 
data = np.linspace(-1, 1, nsamp)
noise = 0.4
c_n = np.random.randn(nsamp,1)*noise

# generate observations
f_vals, A = poly_func(data, weights, degree)
f_obs = f_vals + c_n

# first, plot the data 

# try to do regression via pseudoinverse 

# plot this

# try to do regression via Tikhonov regularization
reg_val = 0.25
p = A.shape[1]

# plot this


plt.draw()
plt.show()


