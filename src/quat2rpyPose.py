#!/usr/bin/env python2



import rospy
from std_msgs.msg import Header
from std_msgs.msg import Int32, Bool
from std_msgs.msg import String
from sensor_msgs.msg import Joy
from sensor_msgs.msg import Imu
from geometry_msgs.msg import PoseStamped, TwistStamped
import csv
from datetime import datetime

import tf

from geometry_msgs.msg import PoseWithCovarianceStamped
from geometry_msgs.msg import Vector3

loc_RPY_pub = rospy.Publisher('/VehiclePose_RollPithchYaw', Vector3, queue_size=5)


def command_calback(msg):
   # quaternion = (
    #msg.pose.pose.orientation.x, msg.pose.pose.orientation.y, msg.pose.pose.orientation.z, msg.pose.pose.orientation.w)

    quaternion = (msg.orientation.x, msg.orientation.y, msg.orientation.z, msg.orientation.w)

    euler = tf.transformations.euler_from_quaternion(quaternion)
    roll = euler[0]
    pitch = euler[1]
    yaw = euler[2]

    RPY = Vector3(roll, pitch, yaw)

    loc_RPY_pub.publish(RPY)


rospy.init_node('Pose_RollPithchYaw_pub')


def main():
    rate = rospy.Rate(100)
    while not rospy.is_shutdown():
    #    msg = rospy.wait_for_message("/mavros/local_position/pose", PoseWithCovarianceStamped)
        msg = rospy.wait_for_message("/mavros/imu/data", Imu)

        command_calback(msg)
        rate.sleep()


main()
