"""
Created on Thu Feb 19 19:46:31 2015
Generate and plot 2D vector field
"""

import numpy as np
import matplotlib.pyplot as plt

# function to calculate 2d scalar field
def func2d(a,b,x,y,n):
    # initialize array
    f = np.zeros((n,n))
    # loop to calculate function
    for i in range(n):
        for j in range(n):
            f[j,i] = a*x[i] + (b*x[i])/(x[i]**2 + y[j]**2)
    return f

# function to calculate 2d gradient of scalar field
def grad2d(f,n,h):
    # initialize arrays
    gx = np.zeros((n,n))
    gy = np.zeros((n,n))
    # forward difference at xy lower boundaries
    gx[0,:] = (f[1,:]-f[0,:])/h
    gy[:,0] = (f[:,1]-f[:,0])/h
    # backward difference at xy upper boundaries
    gx[n-1,:] = (f[n-1,:]-f[n-2,:])/h
    gy[:,n-1] = (f[:,n-1]-f[:,n-2])/h
    # central difference at xy interior points
    for i in range(1,n-1):
        gx[i,:] = (f[i+1,:]-f[i-1,:])/(2*h)
        gy[:,i] = (f[:,i+1]-f[:,i-1])/(2*h)
    return gx,gy

# function to calculate maximum magnitude of gradient
def maxmag(gx,gy,n):
    # initialize array
    mag = np.zeros((n,n))
    # loop to calculate magnitude
    for i in range(n):
        mag[i,:] = (gx[i,:]**2 + gy[i,:]**2)**0.5
    return np.max(mag)

# set limits
gmin,gmax = -2.0,2.0
n = 100
ndx = 3

# get grid
h = (gmax-gmin)/n
xgrid = np.linspace(gmin,gmax,n)
ygrid = np.linspace(gmin,gmax,n)

# get functions
ff = func2d(1.0,1.0,xgrid,ygrid,n)
gx,gy = grad2d(ff,n,h)
mag = maxmag(gx,gy,n)
print '\nmax magnitude of gradient = %1.3f' % mag

# make plots
plt.figure()
plt.contourf(xgrid[::ndx],ygrid[::ndx],ff[::ndx,::ndx])
plt.colorbar()
plt.title('Scalar Field')
plt.xlabel('x')
plt.ylabel('y')

plt.figure()
mag = (gx**2 + gy**2)**0.5
gxnorm = gx/mag
gynorm = gy/mag
plt.quiver(xgrid[::ndx], ygrid[::ndx], gxnorm[::ndx,::ndx], gynorm[::ndx,::ndx],mag[::ndx,::ndx])
plt.colorbar()
plt.title('Vector Field')
plt.xlabel('x')
plt.ylabel('y')