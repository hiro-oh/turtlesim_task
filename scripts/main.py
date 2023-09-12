#!/usr/bin/env python3

import rospy, os, getpass, subprocess
from geometry_msgs.msg import Twist

class Turtlesim_task():
    def __init__(self):
        self.turtlesim_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    def publish(self):
        t = Twist()
        t.linear.x = 0.0
        t.linear.y = 0.0
        t.linear.z = 0.0
        t.angular.x = 0.0
        t.angular.y = 0.0
        t.angular.z = 0.0
        self.turtlesim_pub.publish(t)

if __name__=="__main__":
    rospy.init_node("turtlesim_main_node")

    turtlesim_task = Turtlesim_task()

    rate = rospy.Rate(1)

    user_name = os.getlogin()
    keyboard_file_path = '/home/' + user_name + '/catkin_ws/src/turtlesim_task/scripts/keyboard_event.py'

    command = "sudo -S python3 " + keyboard_file_path
    password = (getpass.getpass() + '\n').encode()
    subprocess.run(command.split(), input=password)
    
    
    while not rospy.is_shutdown():
        turtlesim_task.publish()

        rate.sleep()
