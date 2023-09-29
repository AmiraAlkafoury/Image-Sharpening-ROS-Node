# Image-Sharpening-ROS-Node


## Description

The Image Sharpening ROS Node aims to enhance images captured by a USB camera using the OpenCV library within ROS. This documentation provides an overview of the project, installation instructions, usage guidelines, and insights into the code structure.

## Table of Contents

- [Installation](#installation)
- [How to run the code](#usage)

  ## Installation

1-ROS Installation: If you haven't already, install ROS following the instructions on the official ROS website (http://www.ros.org/install/).

2-Python Dependencies: Make sure you have Python installed, along with OpenCV and cv_bridge. You can install OpenCV using pip:

```
pip install opencv-python
```

3-ROS Packages: Install the necessary ROS packages (usb_cam and RViz) using the following commands:

```
sudo apt-get install ros-melodic-usb-cam
sudo apt-get install ros-melodic-rviz

```

Environment Setup
Source your ROS workspace to ensure ROS can locate the necessary packages and scripts:

```
source /path/to/your/ros/workspace/devel/setup.bash
```

After Setting up your environment and making sure to have all the Dependencies, Now I will show you how to run this project


## How to run the code

1-Launch ROS Core, the master node (if not already running):

```
roscore
```

2-Start the USB Camera Node:

```
roslaunch usb_cam usb_cam.launch
```

3-Run the Image Sharpening Node:

```
rosrun image_sharpening_node.py

```


4-Launching RViz
To visualize the topics, launch RViz:

```
rviz
```

In RViz, you can add visualizers to display topics, including the /usb_cam/image_raw topic for the camera feed and the /sharpened_image topic for the sharpened images.


