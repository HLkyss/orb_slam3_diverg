import numpy as np

# 定义将欧拉角转换为旋转矩阵的函数
def euler_to_rotation_matrix(yaw, pitch, roll):
    # 将角度转换为弧度
    yaw_rad = np.deg2rad(yaw)
    pitch_rad = np.deg2rad(pitch)
    roll_rad = np.deg2rad(roll)

    # 计算旋转矩阵
    R_yaw = np.array([[np.cos(yaw_rad), -np.sin(yaw_rad), 0],
                      [np.sin(yaw_rad), np.cos(yaw_rad), 0],
                      [0, 0, 1]])

    R_pitch = np.array([[np.cos(pitch_rad), 0, np.sin(pitch_rad)],
                        [0, 1, 0],
                        [-np.sin(pitch_rad), 0, np.cos(pitch_rad)]])

    R_roll = np.array([[1, 0, 0],
                       [0, np.cos(roll_rad), -np.sin(roll_rad)],
                       [0, np.sin(roll_rad), np.cos(roll_rad)]])

    # 顺序乘法得到总的旋转矩阵
    R = R_yaw @ R_pitch @ R_roll
    return R

# 修改函数以计算变换矩阵T
def euler_to_transformation_matrix(yaw, pitch, roll, translation):
    # 将角度转换为弧度
    yaw_rad = np.deg2rad(yaw)
    pitch_rad = np.deg2rad(pitch)
    roll_rad = np.deg2rad(roll)

    # 计算旋转矩阵
    R_yaw = np.array([[np.cos(yaw_rad), -np.sin(yaw_rad), 0],
                      [np.sin(yaw_rad), np.cos(yaw_rad), 0],
                      [0, 0, 1]])

    R_pitch = np.array([[np.cos(pitch_rad), 0, np.sin(pitch_rad)],
                        [0, 1, 0],
                        [-np.sin(pitch_rad), 0, np.cos(pitch_rad)]])

    R_roll = np.array([[1, 0, 0],
                       [0, np.cos(roll_rad), -np.sin(roll_rad)],
                       [0, np.sin(roll_rad), np.cos(roll_rad)]])

    # 顺序乘法得到总的旋转矩阵
    R = R_yaw @ R_pitch @ R_roll
    #transformed_translation = R @ translation

    # 构建变换矩阵T
    T = np.eye(4)
    T[:3, :3] = R
    #T[:3, 3] = transformed_translation
    T[0, 3] = translation[0]*np.cos(pitch/2*3.1415926/180)
    T[1, 3] = 0
    T[2, 3] = -translation[0]*np.sin(pitch/2*3.1415926/180)

    return T

# 定义欧拉角
yaw = 0  # 偏航角
pitch = 15  # 俯仰角
roll = 0  # 翻滚角
translation = np.array([0.2, 0.0, 0.0])  # 例如，沿x轴平移1.0单位

# 生成对应的旋转矩阵
rotation_matrix = euler_to_rotation_matrix(yaw, pitch, roll)
# 计算变换矩阵
transformation_matrix = euler_to_transformation_matrix(yaw, pitch, roll, translation)
transformation_matrix
print(transformation_matrix)

# https://chat.openai.com/share/78e63bae-c6df-44c7-927b-6d5a154e9877
