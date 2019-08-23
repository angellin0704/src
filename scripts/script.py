#!/usr/bin/env python
import rospy
from darknet_ros_msgs.msg import BoundingBoxes
      
def callback(data):
	for mid in data.bounding_boxes:
		if mid.Class == 'person':
			midx = (mid.xmin + mid.xmax)/2
			midy = (mid.ymin + mid.ymax)/2 

			print(midx,midy)     
	   
def listener():
	rospy.init_node('midpoint', anonymous=True)
	rospy.Subscriber("/darknet_ros/bounding_boxes", BoundingBoxes, callback)

	rospy.spin()

listener()