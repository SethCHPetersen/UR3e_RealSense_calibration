#!/usr/bin/env python

from encodings import utf_8
import time
import rospy
from std_msgs.msg import String
print("helloWOrld")
def talker():
    pub = rospy.Publisher('/ur_hardware_interface/script_command', String, queue_size=10)
    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        
        hello_str = 'popup("helloworld")'
        
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        time.sleep(5)
        rate.sleep()
        hello_str = "freedrive_mode()"
        rospy.loginfo(hello_str)
        pub.publish(hello_str)
        # hello_str = "end_freedrive_mode()"
        # rospy.loginfo(hello_str)
        # pub.publish(hello_str)
        # rate.sleep()
        time.sleep(5)   

if __name__ == '__main__':
    try:
        talker()
        time.sleep(5)
    except rospy.ROSInterruptException:
        pass
