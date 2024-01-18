#先删除前五张图！！！保留995张
import os

# 文件夹路径
folder_path = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_180/fish_theta0_60hz/cam0'

# 读取 time.txt 中的顺序
txt_file_path = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_180/time.txt'
with open(txt_file_path, 'r') as txt_file:
    ordered_names = [line.strip() for line in txt_file]

# 获取文件夹中的所有文件
files = os.listdir(folder_path)

# 按照原名称中“path3.”后面数字的顺序排序图像
files_sorted = sorted(files, key=lambda x: int(x.split('path3.')[-1].split('.')[0]))

# 遍历排序后的文件，并按照顺序重命名
for old_name, new_name in zip(files_sorted, ordered_names):
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, f"{new_name}.png")
    os.rename(old_path, new_path)

print("Images have been renamed according to the order in time.txt.")

#现有一个/media/hl/Stuff/ubuntu_share_2/Dataset/ue_180/0_degree/left文件夹，里面都是图片，名为path3.0005.png、path3.0006.png等以此类推（有两个小数点分隔符，第二个后面的是文件后缀名，第一个是名称的一部分），现在要对其中的所有图片重命名，具体方法为：先按照原名称中“path3.”后面数字的顺序排列图像，然后，在/media/hl/Stuff/ubuntu_share_2/Dataset/ue_180/0_degree/time.txt文件中的每一行保存了新的图像名称，里面的数据如1701691073793958466、1701691073893155533等，为纯数字，要将每一行的数字作为对应的新图像的名称
