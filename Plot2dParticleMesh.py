"""
Created on Sat May 09 14:07:31 2015
Reads files and plots 2D particle mesh potential and field
"""

import numpy as np
import matplotlib.pyplot as plt

# read data files
xgrid,ygrid = np.loadtxt('xygrid.txt',dtype=float,unpack=True,skiprows=0)
Epot = np.loadtxt('potential.txt',dtype=float,ndmin=2,skiprows=1)
Ex = np.loadtxt('Exfield.txt',dtype=float,ndmin=2,skiprows=1)
Ey = np.loadtxt('Eyfield.txt',dtype=float,ndmin=2,skiprows=1)
tn,pxn,pyn,vxn,vyn = np.loadtxt('trajectory.txt',dtype=float,unpack=True)


# subsample arrays for plotting
ndx = 3

# get E-field normalization
Emag = (Ex**2 + Ey**2)**0.5
Ex = Ex/Emag
Ey = Ey/Emag

# make contour plot of potential
plt.figure()
plt.contourf(xgrid,ygrid,Epot)
plt.xlim(xgrid[0],xgrid[-1])
plt.ylim(ygrid[0],ygrid[-1])
plt.colorbar()
plt.title('Electric Potential Snapshot')
plt.annotate('t = 0.005',fontsize=15,xy=(0.65,0.91),xycoords='figure fraction')
plt.xlabel('x')
plt.ylabel('y')

# make vector plot
plt.figure()
Q = plt.quiver(xgrid[::ndx],ygrid[::ndx],Ex[::ndx,::ndx],Ey[::ndx,::ndx],Emag[::ndx,::ndx])
plt.xlim(xgrid[0],xgrid[-1])
plt.ylim(ygrid[0],ygrid[-1])
plt.title('Electric Field Snapshot')
plt.annotate('t = 0.005',fontsize=15,xy=(0.65,0.91),xycoords='figure fraction')
plt.xlabel('x')
plt.ylabel('y')
plt.colorbar()