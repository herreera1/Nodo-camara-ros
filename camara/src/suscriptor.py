#!/usr/bin/python3

import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def callback(image_msg):
    try:
        cv_image = bridge.imgmsg_to_cv2(image_msg)
        cv2.imshow('ROS Image Subscriber', cv_image)
        cv2.waitKey(10)
    except CvBridgeError as error:
        print(error)

if __name__=="__main__":
    bridge = CvBridge()
    rospy.init_node("nodo_suscriptor", anonymous=False)
    print("Subscribe images from topic /topic_imagen ...")

    image_subcriber = rospy.Subscriber("topic_imagen", Image, callback)

    try:
        # spin() simply keeps python from exiting until this node is stopped
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
