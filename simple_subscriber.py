#!/usr/bin/env python

import rospy
from std_msgs.msg import String

def stringSubscriberCallBack(data):
    rospy.loginfo("%s",data.data)

def stringSubscriber():
    rospy.init_node('node_2', anonymous=False)
    rospy.Subscriber('publisher', String, stringSubscriberCallBack)
    rospy.spin()

if __name__ == '__main__':
    stringSubscriber()
