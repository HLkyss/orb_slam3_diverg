#生成不同频率的时间戳txt文件
def downsample_timestamps(input_file, output_file, sample_rate=30, target_rate=15):
    # 确保目标采样率能被原始采样率整除
    if sample_rate % target_rate != 0:
        raise ValueError("Target rate must be a divisor of sample rate")

    # 计算步长
    step = sample_rate // target_rate

    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        # 按步长读取并写入时间戳
        for i, line in enumerate(infile):
            if i % step == 0:
                outfile.write(line)

# 使用函数
input_file = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_pin_fov100/time_30hz.txt'  # 替换为您的输入文件路径
output_file = '/media/hl/Stuff/ubuntu_share_2/Dataset/ue_pin_fov100/time_15hz.txt'  # 替换为您的输出文件路径

downsample_timestamps(input_file, output_file)
