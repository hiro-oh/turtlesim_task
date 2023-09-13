#!/usr/bin/env python3

import rospy, os, getpass, subprocess, sys
from geometry_msgs.msg import Twist

import asyncio

async def keyboard_event():
    while True:
        # user_input = await asyncio.to_thread(input, "Press 'q' to quit: ")
        input_key = sys.stdin.read(1)
        if input_key == "q":
            print("終了します。")
            sys.exit(0)
            break
        else:
            print("他の処理を続行中...")


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

    asyncio.run(keyboard_event())
    
    while not rospy.is_shutdown():
        turtlesim_task.publish()

        rate.sleep()
