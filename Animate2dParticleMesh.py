"""
Created on Sat May 09 14:07:31 2015
Reads files and generates 2D particle mesh trajectories
"""
import numpy as np
import matplotlib.pyplot as plt

# read data files
tn,pxn,pyn,vxn,vyn = np.loadtxt('trajectory.txt',dtype=float,unpack=True)

# set input parameters
nprts = 200  # particles per frame
xymin = 0    # domain min
xymax = 20   # domain max

# get velocity unit vectors
vmag = (vxn**2 + vyn**2)**0.5
vxn  = vxn/vmag
vyn  = vyn/vmag
cmap = np.linspace(min(vmag),max(vmag),nprts)

# setup formatted arrays
ta      = []
pxa,pya = [],[]
vxa,vya = [],[]
mag=[]
ntot = len(tn)
nfrm = int(ntot/nprts)

# get formatted arrays
for i in range(0,ntot,nprts):
    ta.append(tn[i])
    pxa.append(pxn[i:i+nprts])
    pya.append(pyn[i:i+nprts])
    vxa.append(vxn[i:i+nprts])
    vya.append(vyn[i:i+nprts])
    mag.append(vmag[i:i+nprts])

# loop to generate plot images
plt.ioff()
cnt = 0
for i in range(nfrm):
    plt.figure()
    plt.plot(pxa[i],pya[i],'bo')
    plt.xlim(xymin,xymax)
    plt.ylim(xymin,xymax)
    q = plt.quiver(pxa[i],pya[i],vxa[i],vya[i],cmap)
    Q = plt.quiver(pxa[i],pya[i],vxa[i],vya[i],mag[i])
    plt.title('2D Particle Mesh Trajectory')
    plt.annotate('t = '+'%5.3f'%ta[i],fontsize=15,xy=(0.65,0.91),xycoords='figure fraction')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.colorbar(q)
    plt.savefig('Images/'+str(cnt)+'trajectory_t'+'%5.3f'%ta[i]+'.png')
    plt.close()
    cnt += 1

# finish
print '\ndone !'
print cnt,'images saved'
plt.ion()