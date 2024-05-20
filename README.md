# Lidar to Camera Projection Visualization


## Objective

This work focuses on visualizing the projection of 3D lidar points onto a 2D camera image. By utilizing data from the KITTI dataset, the code performs the transformation from lidar coordinates to camera image coordinates and visualizes the result.

## Prerequisites

- **Python:** The script has been developed and tested with Python 3.8.2.
- **Libraries:** The following libraries are required:
  - numpy
  - cv2
  - pykitti
  - PIL
  - matplotlib

## Data Structure

The script expects the KITTI dataset to be available in  : http://www.cvlibs.net/datasets/kitti/.


## Expected Output Data

Upon execution, the script displays an image showing the camera view with lidar points projected onto it. The depth of each point is color-coded for better visualization.

## camera view with lidar points projected. 

[image1]: assets/1.png
![alt text][image1]


## Note

 - This code assumes a specific data structure from the KITTI dataset and may need modifications to work with other datasets or configurations. Additionally, ensure that the necessary dependencies are installed and properly configured.




