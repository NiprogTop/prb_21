#!/usr/bin/env python
import rospy
from geometry_msgs.msg import Twist


def vel_paramet(vel, lx=0, ly=0, lz=0, ax=0, ay=0, az=0):
    vel.linear.x = lx
    vel.linear.y = ly
    vel.linear.z = lz

    vel.angular.x = ax
    vel.angular.y = ay
    vel.angular.z = az
    return vel


def move_turt(line_vel, ang_vel):
    rospy.init_node('turtmove', anonymous=True)
    pub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    rate = rospy.Rate(1)
    vel = Twist()

    while True:
        pub.publish(vel_paramet(vel, lx=line_vel))
        rate.sleep()
        pub.publish(vel_paramet(vel, az=ang_vel))
        rate.sleep()


if __name__ == '__main__':
    move_turt(3.0, -1.57)
