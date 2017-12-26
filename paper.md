## DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs

### abstract
* 针对目标分割任务，做了三个主要贡献。
    1. 使用上采样和空洞卷积。
        * 空洞卷积有效控制分辨率
        * 空洞卷积在不增加参数数量的情况下增加感受野
    2. 提出atrous spatial pyramid pooling (ASPP) 
        * 在不同尺度下获得图像的上下文信息；
    3. 结合DCNNs and probabilistic graphical models. 
        * 获得更好的目标边界
        
       
### Introduction
* 端对端DCNN获得了惊人的效果。
    * Essential to this success is the built-in invariance of DCNNs to local image transformations,
    which allows them to learn increasingly abstract data representations。
    * 这种形式不变性，对分类任务很好，对分割任务不利（需要空间信息）。
* 利用DCNN做语义分割的三大挑战：
    1. 特征分辨率的降低
        * 池化， 下采样
    2. 存在目标的多个尺度
    3. 因为DCNN形式不变性造成局部准确度的降低。
* 为了克服上面三大难题：
    * 去除最后的池化，用上采样。
        * 采用线性插值法
        * 组合空洞卷积恢复分辨率
    * 多尺度融合，“atrous spatial pyramid pooling” (ASPP).
    * 使用跳跃链接, CRF
* 对已有分类器的修改
    * 转变最后的全连接层为全卷积层
    * 使用空洞卷积增加特征分辨率
    * 使用CRF修正边界信息。
    
  
### Related work
