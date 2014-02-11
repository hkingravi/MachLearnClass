# this script tests Bayesian RBF networks 
import random 

# numpy stuff
import numpy as np
from scipy.io import loadmat, savemat
from numpy.linalg import svd 
from numpy.linalg import norm

# matplotlib stuff
import matplotlib as mp
from matplotlib import rc
import matplotlib.pyplot as plt


# our imports 
from gencolorarray import *

# turns on Tex for plotting
rc('text', usetex=True)
rc('font', family='serif')

# set random seed to ensure reproducible pseudorandom behavior
np.random.seed(0)

# plotting parameters
func_lwidth = 1.5
basis_lwidth = 2.5

# load data
A = np.load('signalMat.npy')
eval_data = np.load('evalData.npy')

# plot random functions
fig = plt.figure()
ax = fig.gca()

num_rfunc = A.shape[0]

for i in xrange(0, num_rfunc):
  i # fill in stuff here that's not dummy code
  
plt.title(r"Random functions",fontsize=20)

# now, generate basis for random functions using SVD 
rank1 = 1
rank2 = 3
rank3 = 8

# fill in 

# create low-rank matrices

# reconstruct 

# plot reconstructed signals for rank1 

color_list = gencolorarray(rank1) # get a list of colors for plotting; 
                                  # see documentation on how to use

# plot reconstructed signals for rank2 

color_list = gencolorarray(rank2) # get a list of colors for plotting 


# plot reconstructed signals for rank3

color_list = gencolorarray(rank3) # get a list of colors for plotting 


plt.draw()
plt.show()


