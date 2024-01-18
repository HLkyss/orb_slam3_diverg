#将文件夹内标定板图片命名为用于kalibr标定的格式，下一步将重命名后的图片制作成rosbag
import os
import shutil

# 输入文件夹路径，包含照片
input_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_pin_fov100/calib/theta10/right'
# 输出文件夹路径，用于保存重命名后的照片
output_folder = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_pin_fov100/calib/theta10/cam1'

# 获取输入文件夹内所有文件
files = os.listdir(input_folder)

# 初始化起始时间戳
timestamp = 1385030208726607500

for file in files:
    # 检查文件是否为PNG格式
    if file.endswith('.png'):
        # 构建新的文件名
        new_file_name = f'{timestamp}.png'
        
        # 构建新文件的绝对路径
        new_file_path = os.path.join(output_folder, new_file_name)
        
        # 获取文件的绝对路径
        file_path = os.path.join(input_folder, file)
        
        # 复制文件到新位置
        shutil.copy(file_path, new_file_path)
        print(f'Copied {file} to {new_file_name}')
        
        # 增加时间戳
        timestamp += 1000000000  # 增加1秒的时间戳

print('Done')

