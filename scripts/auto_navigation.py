#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import PoseStamped

listX = [-4.39, 1.5, 4.16, 4.39]
listY = [2.23, 2, 5.74, -2.78]

def init():
    rospy.init_node('auto_navigation', anonymous=True)
    time.sleep(5)
    goal = PoseStamped()
    goalPublisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
    goal.pose.position.z = 0.0
    goal.pose.orientation.x = 0.0
    goal.pose.orientation.y = 0.0
    goal.pose.orientation.z = 0.0
    goal.pose.orientation.w = 1.0
    goal.header.stamp = rospy.Time.now()
    goal.header.frame_id = "map"
    rospy.loginfo(goal)

    time.sleep(5)

    while not rospy.is_shutdown():
        i = 0
	while i < 4:
	    goal.pose.position.x = listX[i]
	    goal.pose.position.y = listY[i]
	    goalPublisher.publish(goal)
	    time.sleep(8)
	    goal.header.stamp = rospy.Time.now()
	    i = i+1

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass
