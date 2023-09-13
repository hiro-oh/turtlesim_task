#!/usr/bin/env python3

import rospy, sys, threading
from geometry_msgs.msg import Twist

class Turtlesim_task():
    def __init__(self):
        self.turtlesim_pub = rospy.Publisher("/turtle1/cmd_vel", Twist, queue_size=10)

    def publish(self, linear_x=1.0, linear_y=0.0, linear_z=0.0, angle_x=0.0, angle_y=0.0, angle_z=0.0):
        t = Twist()
        t.linear.x = linear_x
        t.linear.y = linear_y
        t.linear.z = linear_z
        t.angular.x = angle_x
        t.angular.y = angle_y
        t.angular.z = angle_z
        self.turtlesim_pub.publish(t)
        print("publish turtlesim data")

def turtlesim_main():
    turtlesim_task = Turtlesim_task()

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        turtlesim_task.publish(1,1,1,1,1,1)

        rate.sleep()

def get_key():
    shutdown_message = "------------------------\n  main system shutdown\n------------------------"

    while True:
        print("keyboard event searching...")
        key = sys.stdin.read(1)
        if key == 'q':
            print(shutdown_message)
            rospy.signal_shutdown("Shutdown")
            break

if __name__=="__main__":
    rospy.init_node("turtlesim_main_node")

    try:
        turtlesim_thread = threading.Thread(target=turtlesim_main)
        turtlesim_thread.daemon = True
        turtlesim_thread.start()

        keyboard_thread = threading.Thread(target=get_key)
        keyboard_thread.daemon = True
        keyboard_thread.start()

        rospy.spin()

    except:
        print("System error happen.")