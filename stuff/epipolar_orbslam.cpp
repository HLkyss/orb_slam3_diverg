// 将orb slam3中极线修正部分复现，发现大发散角度下结果确实有问题
#include <opencv2/imgcodecs.hpp>
#include <opencv2/highgui.hpp>
#include <opencv2/imgproc.hpp>
#include <opencv2/calib3d.hpp> // for cv::initUndistortRectifyMap
#include <iostream>

using namespace cv; // opencv的命名空间
using namespace std;

int main(void)
{
    cv::Mat imLeft = cv::imread("/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_S_same_phi/FOV110_theta25_S160/cam0/1701691073793958466.png");
    cv::Mat imRight = cv::imread("/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_S_same_phi/FOV110_theta25_S160/cam1/1701691073793958466.png");
    cv::Mat K1 = (cv::Mat_<double>(3, 3) << 335.75757575758, 0, 480.0, 0, 335.75757575758, 270.0, 0, 0, 1);
    cv::Mat K2 = (cv::Mat_<double>(3, 3) << 335.75757575758, 0, 480.0, 0, 335.75757575758, 270.0, 0, 0, 1);
    cv::Mat D1 = (cv::Mat_<double>(1, 5) << 0, 0, 0, 0, 0);
    cv::Mat D2 = (cv::Mat_<double>(1, 5) << 0, 0, 0, 0, 0);
    // 4x4变换矩阵 第2个摄像头到第1个摄像头
    cv::Mat T = (cv::Mat_<double>(4, 4) << 
                              0.64278761, 0.0,  0.76604444,  0.18126156,
                              0.0,  1.0,  0.0,  0.0,
                              -0.76604444, 0.0,  0.64278761, -0.08452365,
                              0, 0, 0, 1.000000000000000);

    // cv::Mat imLeft = cv::imread("/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_S_same_phi/FOV120_theta30_S180/cam0/1701691073793958466.png");
    // cv::Mat imRight = cv::imread("/media/hl/Stuff/ubuntu_share_2/Dataset/ue_stereo_test/diff_S_same_phi/FOV120_theta30_S180/cam1/1701691073793958466.png");
    // cv::Mat K1 = (cv::Mat_<double>(3, 3) << 276.767676768, 0, 480.0, 0, 276.767676768, 270.0, 0, 0, 1);
    // cv::Mat K2 = (cv::Mat_<double>(3, 3) << 276.767676768, 0, 480.0, 0, 276.767676768, 270.0, 0, 0, 1);
    // cv::Mat D1 = (cv::Mat_<double>(1, 5) << 0, 0, 0, 0, 0);
    // cv::Mat D2 = (cv::Mat_<double>(1, 5) << 0, 0, 0, 0, 0);
    // // 4x4变换矩阵 第2个摄像头到第1个摄像头
    // cv::Mat T = (cv::Mat_<double>(4, 4) << 
    //                           0.5, 0.0,  0.8660254,  0.1732,
    //                           0.0,  1.0,  0.0,  0.0,
    //                           -0.8660254, 0.0,  0.5, -0.1,
    //                           0, 0, 0, 1.000000000000000);

    // 第一个摄像头到第二个摄像头的相对旋转和平移
    cv::Mat R = T(cv::Rect(0, 0, 3, 3)); // 提取前3x3的旋转部分
    cv::Mat t = T(cv::Rect(3, 0, 1, 3)); // 提取第四列作为平移向量
    // 第二个摄像头到第一个摄像头的相对旋转和平移
    cv::Mat R12 = R.inv();
    cv::Mat t12 = -R12 * t;

    cv::Mat R1, R2, P1, P2, Q;  //R1, R2, P1, P2, 和 Q 是输出矩阵，分别用于存储校正旋转矩阵、新的投影矩阵和深度映射矩阵。

    double alpha = 1;//alpha 参数的值在0和1之间，其中0表示只有完全有效的像素区域被保留，1表示尽可能多的像素区域被保留  源代码为-1
/*  校正过程中的视野丢失：
    根据你提供的旋转和平移，有可能在校正过程中丢失了大部分视野，特别是如果两个摄像头之间的相对位置和方向差异很大。
    尝试调整 cv::stereoRectify 中的 alpha 参数。alpha 参数控制校正后的图像中可见视野的大小。alpha=0 表示仅保留有效区域，alpha=1 表示保留尽可能多的像素区域（可能包括无效区域）
    在 cv::stereoRectify 函数中修改 alpha 参数可以调整校正后的图像中可见视野的大小。
    alpha 参数的值在0和1之间，其中0表示只有完全有效的像素区域被保留，1表示尽可能多的像素区域被保留，即使它们包含了一些无效的像素。
    调整 alpha 可以帮助解决校正后图像全黑或全灰的问题，特别是当相机视角相差较大时。
    当 alpha 参数被设置为 -1 时，意味着函数将自动决定如何处理校正后图像的视野，以便在不引入无效区域的同时尽可能保留最多的有效像素区域。
调整alpha，结果仍然不好。考虑是输出图片大小问题*/

    // 原始图像大小
    cv::Size originalSize = imLeft.size();
    // 设置新的图像大小为原始大小的10倍
    cv::Size newSize(static_cast<int>(originalSize.width * 1), 
                     static_cast<int>(originalSize.height * 1));
/*结果还是不行，可能是因为共视区域图像在两个摆放角度较大的大视角相机的边缘，畸变较大。
不论修改alpha还是输出图像大小，都无法得到正常的图像，得到的只有几乎纯色的图片，可能是原图香洲某一个区域的放大图。
可能是修正后的图像，边缘被放大的太多了。*/
                     
    cv::stereoRectify(K1, D1, K2, D2, originalSize,
                        R12, t12,
                        R1, R2, P1, P2, Q,
                        cv::CALIB_ZERO_DISPARITY, alpha, newSize);
                        /*这个标志指示校正后的两个摄像头的光心（即成像中心）在水平方向上应该有相同的像素坐标。简单来说，它会尝试调整两个摄像头的视野，使得它们在水平方向上尽可能对齐。
                        在这种校正方式下，同一物体在左右两个摄像头拍摄的图像中将出现在相同的水平位置上。这种特性简化了立体视觉系统中的视差计算，因为搜索匹配点时只需要在水平方向上进行。*/

/*对于大视角相机，常规的校正方法可能不够有效。考虑使用专门针对鱼眼镜头或其他类型的大视角镜头设计的校正方法，比如 cv::fisheye::stereoRectify*/

/*  在使用 cv::stereoRectify 完成极线校正（Epipolar Rectification）之后，你可以使用 cv::initUndistortRectifyMap 和 cv::remap 函数来生成和可视化校正后的图像。
    这个过程包括两个主要步骤：首先，创建畸变矫正和校正变换映射；其次，应用这些映射到原始图像上。*/

    // 创建畸变矫正和校正变换映射
    cv::Mat M1l, M2l, M1r, M2r;
    cv::initUndistortRectifyMap(K1, D1, R1, P1, newSize, CV_32FC1, M1l, M2l);
    cv::initUndistortRectifyMap(K2, D2, R2, P2, newSize, CV_32FC1, M1r, M2r);

    // 应用映射到原始图像
    cv::Mat imLeftRectified, imRightRectified;
    cv::remap(imLeft, imLeftRectified, M1l, M2l, cv::INTER_LINEAR);
    cv::remap(imRight, imRightRectified, M1r, M2r, cv::INTER_LINEAR);

    // //缩放图像
    // cv::resize(imLeftRectified, imLeftRectified, cv::Size(), 0.1, 0.1);
    // cv::resize(imRightRectified, imRightRectified, cv::Size(), 0.1, 0.1);

    // 可视化校正后的图像
    cv::imshow("Left Rectified", imLeftRectified);
    cv::imshow("Right Rectified", imRightRectified);
    cv::waitKey(0);

    //保存图片
    // cv::imwrite("/home/hl/project/vscode_proj/OpenCV/stuff/left_rectified1.png", imLeftRectified);
    // cv::imwrite("/home/hl/project/vscode_proj/OpenCV/stuff/right_rectified1.png", imRightRectified);

    

}
