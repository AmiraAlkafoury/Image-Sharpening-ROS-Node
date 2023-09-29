# Image-Sharpening-ROS-Node


## Description

The Image Sharpening ROS Node aims to enhance images captured by a Web camera using the OpenCV library within ROS.The purpose of this project is to demonstrate how to create a ROS node that subscribes to a camera feed, performs image sharpening on the incoming images, and publishes the sharpened images as a new topic. Additionally, the project includes visualization of topics using RViz.


## Table of Contents

- [Installation](#installation)
- [How to run the code](#How-to-run-the-code)
- [Output](#Output)


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



## How-to-run-the-code

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



## Output

![image](https://github.com/AmiraAlkafoury/Image-Sharpening-ROS-Node/assets/108875740/7abfc739-1519-4018-9558-bd220d3ea410)

As you can see the upper image (the one we got from camera feed) is smoother than the one below(the one resulted from our node).
