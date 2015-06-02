"""
Created on Sat Apr 04 18:21:52 2015
Plot gradient test function
"""

import numpy as np
import matplotlib.pyplot as plt

# function to calculate 2d gradient
def grad2d(x,y):
    # calculate gradient function
    gradx = 1.0 + 1.0/(x**2 + y**2) - (2*x**2)/(x**2 + y**2)**2
    grady = -(2*x*y)/(x**2 + y**2)**2
    return gradx,grady

# set limits
gmin,gmax = -4.0,4.0
n = 100
ndx = 3

# get grid
h = (gmax-gmin)/n
xgrid = np.linspace(gmin,gmax,n)
ygrid = np.linspace(gmin,gmax,n)
gradx = np.zeros((n,n))
grady = np.zeros((n,n))

# get gradient
for i in range(n):
    for j in range(n):
        gx,gy = grad2d(xgrid[i],ygrid[j])
        gradx[i,j] = gx
        grady[i,j] = gy

# make plot
plt.figure()
mag = (gradx**2 + grady**2)**0.5
gradxnorm = gradx/mag
gradynorm = grady/mag
plt.quiver(xgrid[::ndx], ygrid[::ndx], gradxnorm[::ndx,::ndx], gradynorm[::ndx,::ndx],mag[::ndx,::ndx])
plt.colorbar()
plt.title('Gradient Field')
plt.xlabel('x')
plt.ylabel('y')