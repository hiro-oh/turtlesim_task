#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import Twist
import keyboard

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

def on_key_event(e):
    if e.name == 'q' and e.event_type == keyboard.KEY_DOWN:
        print("終了します...")
        keyboard.unhook_all()  # イベントのフックを解除してプログラムを終了
    else:
        print(f'キー {e.name} が {e.event_type} されました')


if __name__=="__main__":
    rospy.init_node("turtlesim_main_node")

    turtlesim_task = Turtlesim_task()

    rate = rospy.Rate(1)
    keyboard.hook(on_key_event)

    while not rospy.is_shutdown():
        turtlesim_task.publish()

        rate.sleep()

    # try:
    #     while True:
    #         key = input("入力：　") 

    #         if key == "q":
    #             print("終了する")
    #             break
    #         else:
    #             print("何もしない")
    # except KeyboardInterrupt:
    #     pass
