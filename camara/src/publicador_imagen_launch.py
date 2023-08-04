#!/usr/bin/python3

import cv2
import rospy
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

class camera_publisher:

    def __init__(self):
        self.image_pub = rospy.Publisher("topic_imagen", Image, queue_size=10)
        self.bridge = CvBridge()
        self.capture = cv2.VideoCapture(rospy.get_param('/nodo_camara/nombre_camara'))

    def publish_image(self):
        while not rospy.is_shutdown():
            # Capture a frame
            ret, img = self.capture.read()
            if not ret:
                rospy.ERROR("Could not grab a frame!")
                break
            # Publish the image to the topic 
            try:
                img_msg = self.bridge.cv2_to_imgmsg(img, "bgr8")
                img_msg.header.stamp = rospy.Time.now()
                self.image_pub.publish(img_msg)
            except CvBridgeError as error:
                print(error)


if __name__=="__main__":
    cam_pub = camera_publisher()
    rospy.init_node("my_cam", anonymous=True)
    print("Image is being published to the topic ...")
    cam_pub.publish_image()
    
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
