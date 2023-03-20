# Add this line to import the model configuration
_base_ = './faster_rcnn_r50_fpn_1x_coco.py'

# Modify the number of classes in the model's bbox head
model = dict(
    roi_head=dict(
        bbox_head=dict(
            num_classes=1,  # Only one class
        )
    )
)
