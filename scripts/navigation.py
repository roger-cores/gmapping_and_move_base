#!/usr/bin/env python
import rospy
import time
from geometry_msgs.msg import PoseStamped

def init():
    rospy.init_node('navigation', anonymous=True)
    time.sleep(5)
    goalPublisher = rospy.Publisher('move_base_simple/goal', PoseStamped, queue_size=10)
    goal = PoseStamped()
    goal.pose.position.x = 4
    goal.pose.position.y = 5
    goal.pose.orientation.w = 1.0
    goal.header.stamp = time.time()
    goal.header.frame_id = "map"

    goalPublisher.publish(goal)
    rospy.spin()

if __name__ == '__main__':
    try:
        init()
    except rospy.ROSInterruptException: pass
