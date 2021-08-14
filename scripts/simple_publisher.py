#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def stringPublisher():
    publisher = rospy.Publisher('publisher', String, queue_size=10)
    rospy.init_node('node_1', anonymous=False)
    rate = rospy.Rate(1)

    publish_content = "Hello World !!"

    while not rospy.is_shutdown():
        publisher.publish(publish_content)
        rate.sleep()

if __name__ == '__main__':
    try:
        stringPublisher()
    except rospy.ROSInterruptException:
        pass
