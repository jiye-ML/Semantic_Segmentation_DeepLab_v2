## DeepLab: Semantic Image Segmentation with Deep Convolutional Nets, Atrous Convolution, and Fully Connected CRFs

## abstract

* 针对目标分割任务，做了三个主要贡献。
    1. 使用上采样和空洞卷积。
        * 空洞卷积有效控制分辨率
        * 空洞卷积在不增加参数数量的情况下增加感受野
    2. 提出atrous spatial pyramid pooling (ASPP) 
        * 在不同尺度下获得图像的上下文信息；
    3. 结合DCNNs and probabilistic graphical models. 
        * 获得更好的目标边界
        
       
## Introduction

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
* [DeepLab illustration](model_illustration.png)
    * ResNet-101作为分类器
        * 转变最后的全连接层为全卷积层
        * 使用空洞卷积增加特征分辨率
        * 使用CRF修正边界信息。
    

## Related work

* 过去几年深度学习在图像分类和分割任务上取得了重大突破。因为这个任务即涉及了分类也涉及了分割， 
所以关键问题是如何结合这两者
* 第一种是自底向上的级联网络。
    * 边界框， 边界信息
* 第二种使用卷积，
    * 多尺度预测
    * 跳跃链接
* 第三种全卷积
    * 多层池化技术
    * CRF


## method

### Atrous Convolution for Dense Feature Extraction and Field-of-View Enlargement
* 使用DCNN于语义分割任务，在使用全卷积网络时得到了解决
* 但多次的池化和下采样操作丢失了很多重要的空间信息。
    * 可以使用反卷积方法部分解决这个问题，但这需要额外的空间和时间
* 我们使用空洞卷积
    * 这种算法可以允许在任意层得到想要的分辨率
    * 既可以接入训练好的网络中
    * 也可以无缝接入训练的过程中
    * [atrous 1d](atrous_1d.png)
    * [atrous 2d](atrous_2d.png)
* 我们可以在任意分辨率下使用空洞卷积
    * 我们将最后下采样的层stride设为1， 把卷积设置为空洞卷积 r = 2
    * 这样造成了计算量增大
        * 没懂
        
* 空洞卷积可以在增大感受野到任意大小
    * 在每个间隙中补 rate-1 
    * k_new = k + (k - 1)(r - 1)
    
* 实现方面：
    1. 隐式上采样卷积核，或者离散采样输入特征图，
    2. 方法下采样输入特征图使用和空洞卷积rate，逐行扫描得到r^2个分辨率图，
        * 每张图都是可转变的
        * 使用标准卷积到这些中间特征图，再次扫描到原来图像的分辨率。
        * 通过把空洞卷积转换为标准卷积，我们可以使用现有的优化的卷积路径。
    
### Multiscale Image Representations using Atrous Spatial Pyramid Pooling

* 我们实验了两种方法处理尺度变化在语义分割中
    1. 整合标准多尺度操作，使用线性插值到同样大小，然后融合
    2. 空间金字塔池化，使用不同rate平行空洞卷积，然后融合。
    
### Structured Prediction with Fully-Connected Conditional Random Fields for Accurate Boundary Recovery

* 以前的工作主要是连个方向：
    1. 从卷积网络的多层中获得有用的信息定位边界
    2. 使用超像素表示，将定位任务委派给更低水平的分割方法。

* DCNNs + CRF对于定位挑战很关键。

* CRF
    * 相似的像素点相同的类标

* 我们使用的网络在生成语义分割类标预测时和弱的分类器不同
    * 热力图时平滑的，产生了很和谐的分类结果。
    * 在这些区域，使用短范围的CRFs是有害的。
    * 我们的目标是恢复局部结构细节信息而不是进一步平滑它
    * 利用反直觉潜力在短距离链接CRF链接上的，可以提高定位但仍然失去了结构
    * 并且需要解决昂贵的离散优化问题
    
* 为了克服上面问题
    * 没看
    
## Experimental Results

* 使用 imagenet_pretrained 的ResNet101
* 使用交叉熵作为损失
* 使用SGD作为优化函数
