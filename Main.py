import numpy as np
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import cv2
import pykitti
from PIL import Image

base = 'path/to/folder' # Importing data
date = '2011_09_26'
drive = '0009'
dataset = pykitti.raw(base, date, drive, frames=range(0, 20, 5))
point = dataset.get_velo(0) # Defining points
point[:,-1] = 1 # Replace the values of the last column with 1
point = point[point[:,0]>=5] # Eliminating points less than 5
K = dataset.calib.K_cam2   # Calibration matrix
M_t = dataset.calib.T_cam2_velo[0:3,:] # Transforming lidar points to camera image Eliminating the last point
P = K@M_t   # Projection matrix
point_cam2 = (P@point.T).T # Projecting 3D points to 2D
point_cam2 = np.array([point_cam2[:,0]/point_cam2[:,2],point_cam2[:,1]/point_cam2[:,2]]).T # Transforming points to Cartesian coordinates
I = np.array(dataset.get_cam2(0))
l = I.shape[0]
c = I.shape[1]
p_i = point_cam2[((point_cam2[:,0] > 0) & (point_cam2[:,0]  < c) & (point_cam2[:,1] > 0) & (point_cam2[:,1] < l)) ]
mask = (point_cam2[:,0] > 0) & (point_cam2[:,0]  < c) & (point_cam2[:,1] > 0) & (point_cam2[:,1] < l)
pts = point[:,0]*mask   # x-axis in the image == depth in 3D
pts = pts[pts != 0]    # Eliminate points equal to zero
t = 5/pts*64    # Creating the colormap by normalizing between 0 and 64
plt.figure(figsize=(10,5))
plt.imshow(I)   # Displaying the image
plt.scatter(p_i[:,0],p_i[:,1],marker = '.', s=60 ,c=t,cmap='jet')    # Displaying depths
plt.show()
