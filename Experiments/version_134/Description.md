|Model                |FPN      |
|---------------------|---------|
|Encoder              |Resnet 50|
|Train Batch Size     |25       |
|Validation Batch Size|25       |
|Loss Function        |DiceLoss |
|Optimizer            |ADAM     |
|Epochs               |20       |

```python
[{'valid_loss': 0.5200894474983215, 'valid_per_image_iou': 0.2979690432548523, 'valid_dataset_iou': 0.268897145986557}]
```