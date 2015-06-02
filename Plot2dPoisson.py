"""
Created on Sat May 02 00:30:23 2015
Reads files and plots 2D electric potential and electric field
"""

import numpy as np
import matplotlib.pyplot as plt

# read data files
x,y   = np.loadtxt('xygrid.txt',dtype=float,unpack=True)
Epot  = np.loadtxt('potential.txt',dtype=float,ndmin=2)
gradx = np.loadtxt('gradx.txt',dtype=float,ndmin=2)
grady = np.loadtxt('grady.txt',dtype=float,ndmin=2)

# subsample arrays for plotting
ndx = 6

# make contour plot
plt.figure()
plt.contourf(x,y,Epot)
plt.xlim(x[0],x[-1])
plt.ylim(y[0],y[-1])
plt.colorbar()
plt.title('Electric Potential')
plt.xlabel('x')
plt.ylabel('y')

# get normalization
mag = (gradx**2 + grady**2)**0.5
gradx = gradx/mag
grady = grady/mag

# make vector plot
plt.figure()
Q = plt.quiver(x[::ndx],y[::ndx],gradx[::ndx,::ndx],grady[::ndx,::ndx],mag[::ndx,::ndx])
plt.xlim(x[0],x[-1])
plt.ylim(y[0],y[-1])
plt.title('Electric Field')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()