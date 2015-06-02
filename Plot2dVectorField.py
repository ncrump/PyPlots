"""
Created on Thu Feb 19 19:46:31 2015
Reads files and plots 2D vector field
"""

import numpy as np
import matplotlib.pyplot as plt

# read data files
x,y = np.loadtxt('DataFiles/xygrid.txt',dtype=float,unpack=True)
ff  = np.loadtxt('DataFiles/2dscalarfield.txt',dtype=float,ndmin=2)
gx  = np.loadtxt('DataFiles/2dvectorfieldX.txt',ndmin=2)
gy  = np.loadtxt('DataFiles/2dvectorfieldY.txt',ndmin=2)

# subsample arrays for plotting
ndx = 3

# make contour plot
plt.figure()
plt.contourf(x[::ndx],y[::ndx],ff[::ndx,::ndx])
plt.colorbar()
plt.title('Scalar Field')
plt.xlabel('x')
plt.ylabel('y')

# get normalization
mag = (gx**2 + gy**2)**0.5
gxnorm = gx/mag
gynorm = gy/mag

# make vector plot
plt.figure()
Q = plt.quiver(x[::ndx], y[::ndx], gxnorm[::ndx,::ndx], gynorm[::ndx,::ndx],mag[::ndx,::ndx])
plt.title('Vector Field')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()