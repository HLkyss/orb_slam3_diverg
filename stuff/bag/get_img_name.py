#在从rosbag里提取图片后，将图片名即时间戳提取到txt里
import os
import re

# 指定文件夹路径
folder_path = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2/left'
# 将文件名写入txt文件
output_file_path = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2/time.txt'

# 获取文件夹中所有文件
files = os.listdir(folder_path)

# 使用正则表达式提取文件名中的数字部分
pattern = re.compile(r'(\d+)')
filtered_files = [pattern.search(file).group(1) for file in files if pattern.search(file)]

# 将文件名按数字大小排序
filtered_files = sorted(filtered_files, key=lambda x: int(x))

with open(output_file_path, 'w') as output_file:
    for file_name in filtered_files:
        output_file.write(file_name + '\n')

print(f"File names have been saved to {output_file_path}")



