#!/usr/bin/env python
#source /home/hl/project/cv_bridge_ws/src/vision_opencv-noetic/cv_bridge/install/install320/usr/local/setup.bash
#source /home/hl/Downloads/vision_opencv-noetic/cv_bridge/install/install320/usr/local/setup.bash
#分别提取rosbag中的对应话题的图像
import rosbag
import cv2
from cv_bridge import CvBridge
from sensor_msgs.msg import Image

# 输入ROS Bag文件和输出文件夹
#input_bag_file = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot/near_parallel/calibration2/calib_near.bag'
#output_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot/near_parallel/calibration2/img/cam1/'
input_bag_file = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2.bag'
output_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2/cam0/'

# 打开ROS Bag文件
with rosbag.Bag(input_bag_file, 'r') as bag:
    for topic, msg, t in bag.read_messages(topics=['/camera/left/image_raw']):
        if topic == '/camera/left/image_raw':
            # 使用cv_bridge将ROS Image消息转换为OpenCV图像
            bridge = CvBridge()
            cv_image = bridge.imgmsg_to_cv2(msg, desired_encoding="bgr8")

            # 保存图像文件
            image_filename = output_folder + str(t) + ".png"
            cv2.imwrite(image_filename, cv_image)

