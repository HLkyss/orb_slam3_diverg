import os

# 指定第一个和第二个文件夹的路径
folder_path_2 = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2/cam1'  # 第二个文件夹

# 读取第一个文件夹中的顺序文件名
txt_file_path = '/media/hl/Stuff/ubuntu_share_2/Dataset/hikrobot_180/hik_180_2/time.txt'
with open(txt_file_path, 'r') as txt_file:
    ordered_file_names = [line.strip() for line in txt_file]

# 获取第二个文件夹中的所有文件
files_folder_2 = os.listdir(folder_path_2)

# 按照数字顺序排序第二个文件夹中的文件
files_folder_2_sorted = sorted(files_folder_2, key=lambda x: int(os.path.splitext(x)[0]))

# 遍历排序后的第二个文件夹中的文件，并按照顺序重命名
for old_name, new_name in zip(files_folder_2_sorted, ordered_file_names):
    old_path = os.path.join(folder_path_2, old_name)
    new_path = os.path.join(folder_path_2, f"{new_name}.png")
    os.rename(old_path, new_path)

print("Files in the second folder have been renamed according to the order in the txt file.")
#接下来要修改第二个文件夹里面图片的名字：第二个文件夹里面的图像有和第一个文件夹中类似的命名方式，文件名也是数字，现在要将其中的图片按数字从小到大排序，然后依次重命名为刚刚保存的txt中的每一行的数（也是按从小到大顺序顺序），写一个脚本
