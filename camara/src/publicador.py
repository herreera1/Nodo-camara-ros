#!/usr/bin/python3
import rospy
import cv2
from cv_bridge import CvBridge, CvBridgeError
from sensor_msgs.msg import Image

def publish_image():
    image_pub = rospy.Publisher("topic_imagen", Image, queue_size=10)
    bridge = CvBridge()
    capture = cv2.VideoCapture("/dev/video1")

    while not rospy.is_shutdown():
        # Capture a frame
        ret, img = capture.read()
        if not ret:
            rospy.ERROR("Could not grab a frame!")
            break
        # Publish the image to the topic image_raw
        try:
            img_msg = bridge.cv2_to_imgmsg(img, "bgr8")
            image_pub.publish(img_msg)
        except CvBridgeError as error:
            print(error)

if __name__=="__main__":
    rospy.init_node("nodo_publicador", anonymous=False)
    print("Image is being published to the topic /topic_imagen ...")
    publish_image()
    try:
        rospy.spin()
    except KeyboardInterrupt:
        print("Shutting down!")
