|Model                |FPN      |
|---------------------|---------|
|Encoder              |Resnet 50|
|Train Batch Size     |25       |
|Validation Batch Size|25       |
|Loss Function        |Jaccard  |
|Optimizer            |ADAM     |
|Epochs               |20       |

```python
[{'valid_loss': 0.5650312304496765, 'valid_per_image_iou': 0.46573010087013245, 'valid_dataset_iou': 0.37820571660995483}]
```