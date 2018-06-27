### 多尺度融合 deeplab v2 版本实现 ， ResNet作为底层特征

* [论文解读](https://github.com/jiye-ML/Semantic_Segmentation_Review.git)

#### Training
```
num_steps: how many iterations to train

save_interval: how many steps to save the model

random_seed: random seed for tensorflow

weight_decay: l2 regularization parameter

learning_rate: initial learning rate

power: parameter for poly learning rate

momentum: momentum

encoder_name: name of pre-trained model, res101, res50 or deeplab

pretrain_file: the initial pre-trained model file for transfer learning

data_list: training data list file

grad_update_every (msc only): accumulate the gradients for how many steps before updating weights. Note that in the msc case, this is actually the true training batch size.
```


#### Testing/Validation
```
valid_step: checkpoint number for testing/validation

valid_num_steps: = number of testing/validation samples

valid_data_list: testing/validation data list file
```


#### Data
```
data_dir: data directory

batch_size: training batch size

input height: height of input image

input width: width of input image

num_classes: number of classes

ignore_label: label pixel value that should be ignored

random_scale: whether to perform random scaling data-augmentation

random_mirror: whether to perform random left-right flipping data-augmentation
```

#### Log
```
modeldir: where to store saved models

logfile: where to store training log

logdir: where to store log for tensorboard
```

## Training and Testing

#### Start training

After configuring the network, we can start to train. Run
```
python MainMsc.py
```
The training of Deeplab v2 ResNet will start.

#### Training process visualization

We employ tensorboard for visualization.

```
tensorboard --logdir=log --port=6006
```

You may visualize the graph of the model and (training images + groud truth labels + predicted labels).

To visualize the training loss curve, write your own script to make use of the training log.

#### Testing and prediction

Select a checkpoint to test/validate your model in terms of pixel accuracy and mean IoU.

Fill the valid_step in main.py with the checkpoint you want to test. Change valid_num_steps and valid_data_list accordingly. Run

```
python MainMsc.py --option=test
```

The final output includes pixel accuracy and mean IoU.

Run

```
python MainMsc.py --option=predict
```
The outputs will be saved in the 'output' folder.



* [参考文献](https://github.com/zhengyang-wang/Deeplab-v2--ResNet-101--Tensorflow)
