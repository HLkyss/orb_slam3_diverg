#!/usr/bin/env python
import rosbag
from sensor_msgs.msg import Image
from cv_bridge import CvBridge
import cv2
import os
import rospy

def create_rosbag(left_img_folder, right_img_folder, output_bag_file, frame_rate=10.0):
    # 初始化cv_bridge
    bridge = CvBridge()

    # 初始化ROS节点（如果在独立脚本中运行）
    rospy.init_node('image_to_rosbag', anonymous=True)

    # 计算每帧之间的时间间隔（以秒为单位）
    frame_interval = rospy.Duration(1.0 / frame_rate)

    # 创建新的rosbag
    with rosbag.Bag(output_bag_file, 'w') as bag:
        left_images = sorted(os.listdir(left_img_folder))
        right_images = sorted(os.listdir(right_img_folder))

        # 初始时间戳
        current_time = rospy.Time.now()

        for left_img, right_img in zip(left_images, right_images):
            # 读取图像
            left_img_path = os.path.join(left_img_folder, left_img)
            right_img_path = os.path.join(right_img_folder, right_img)

            left_cv_image = cv2.imread(left_img_path)
            right_cv_image = cv2.imread(right_img_path)

            # 转换成ROS图像消息
            left_ros_img = bridge.cv2_to_imgmsg(left_cv_image, "bgr8")
            right_ros_img = bridge.cv2_to_imgmsg(right_cv_image, "bgr8")

            left_ros_img.header.stamp = current_time
            right_ros_img.header.stamp = current_time

            # 写入图像到rosbag
            bag.write('/camera/left/image_raw', left_ros_img, current_time)
            bag.write('/camera/right/image_raw', right_ros_img, current_time)

            # 更新时间戳
            current_time += frame_interval

if __name__ == "__main__":
    left_img_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_b_same_fov/theta30_b_40/cam0'
    right_img_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_b_same_fov/theta30_b_40/cam1'
    output_bag_file = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_b_same_fov/rosbag/theta30_b_40.bag'
    create_rosbag(left_img_folder, right_img_folder, output_bag_file)

