"""
Created on Sat May 09 14:07:31 2015
Reads files and animates 2D particle mesh trajectory
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim

# read data files
tn,pxn,pyn,vxn,vyn = np.loadtxt('trajectory.txt',dtype=float,unpack=True)

# set input parameters
nprts = 20  # particles per frame
xymin = 0    # domain min
xymax = 10   # domain max

# format arrays
ta      = []
pxa,pya = [],[]
ntot = len(tn)
nfrm = int(ntot/nprts)
for i in range(0,ntot,nprts):
    ta.append(tn[i])
    pxa.append(pxn[i:i+nprts])
    pya.append(pyn[i:i+nprts])

# generate animation
fig = plt.figure()
fig.suptitle('2d Particle Mesh Trajectory',fontsize=14)
ax = fig.add_subplot(1,1,1)

# setup subplot axes
ax.set_xlim(xymin,xymax)
ax.set_ylim(xymin,xymax)
ax.set_xlabel('x',fontsize=14)
ax.set_ylabel('y',fontsize=14)

# initialize plot data
line1,  = ax.plot([],[],'bo',markersize=10)
t,px,py = [],[],[]

# define data generator function
def gendata():
    # loop to generate plot data
    line1.set_data([],[])
    return line1,

# define update plot function
def genplot(i):
    # update plot data
    t.append(ta[i])
    px.append(pxa[i])
    py.append(pya[i])
    line1.set_data(px[-1],py[-1])
    text1 = ax.annotate('t = '+str(t[-1]),fontsize=14,xy=(0.14,0.85),xycoords='figure fraction')
    return line1,text1,

ani = anim.FuncAnimation(fig,genplot,init_func=gendata,frames=nfrm,interval=200,blit=True,repeat=False)
plt.show()