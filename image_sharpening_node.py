#!/usr/bin/env python2

import rospy
import cv2
from sensor_msgs.msg import Image
from cv_bridge import CvBridge, CvBridgeError

def image_callback(msg):
    try:
       rospy.loginfo("entered the callback function")
        # Convert ROS Image message to OpenCV image
        bridge = CvBridge()
        cv_image = bridge.imgmsg_to_cv2(msg, "bgr8")

        # Perform image sharpening (you can adjust the kernel size and strength)
        kernel = numpy.array([[-1, -1, -1],
                               [-1, 9, -1],
                               [-1, -1, -1]])
        sharpened_image = cv2.filter2D(cv_image, -1, kernel)

        # Convert OpenCV image back to ROS Image message
        sharpened_msg = bridge.cv2_to_imgmsg(sharpened_image, "bgr8")

        # Publish the sharpened image
        pub.publish(sharpened_msg)

    except CvBridgeError as e:
        rospy.logerr(e)

if __name__ == '__main__':
    rospy.loginfo("the node started")
    rospy.init_node('image_sharpening_node')
    rospy.Subscriber("/usb_cam/image_raw", Image, image_callback)
    pub = rospy.Publisher("/sharpened_image", Image, queue_size=1)
    rospy.spin()