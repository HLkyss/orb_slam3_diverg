V1
此工程作为备份，非特殊情况不要修改。

此代码为了能在发散双目和发散鱼眼情况下成功跑通，不跟丢。
对源码的主要更改：
加了c_new条件，在特征点少时强制添加关键帧，防止跟丢
初始化时单独设置前几帧每张图特征点提取数量，保证大角度发散时在较小共视区域仍有足够点初始化
个别位置的调参，如鱼眼相机时暴力匹配参数调整

具体可以搜索diy等字眼

------------------------------------------------------------------
注释版，来源：
https://github.com/electech6/ORB_SLAM3_detailed_comments
<img src="https://github.com/HLkyss/orb_slam3_diverg/assets/69629475/217cb91a-958b-4f97-881b-8cb2cc3c43fd" width="800"> <br />
<img src="https://github.com/HLkyss/orb_slam3_diverg/assets/69629475/04ff2d25-6ec9-4c08-83e9-089223c7e9df" width="800"> <br />
