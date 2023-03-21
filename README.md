# CS 640 Project_Team_16
## Small Object Detection Challenge for Spotting Birds @MVA2023

# Contents

Code: This directory contains the project code in both Jupyter Notebook (.ipynb) and Python script (.py) formats. It also includes configuration and base files required for the implementation of bird detection for the competition.

Data: The data used for this project is not included in the repository due to size limitations. However, you can access it from the following Google Drive link: https://drive.google.com/drive/folders/1NWt8lap3spKKK_trOAzkdXAxlEhv2t0m?usp=sharing

## Dataset Directory Structure
**[Download Link](https://drive.google.com/drive/folders/1NWt8lap3spKKK_trOAzkdXAxlEhv2t0m?usp=sharing)**

```
data
 ├ drone2021 (62.4GB)
 │  ├ images
 │  └ annotations
 ├ mva2023_sod4bird_train (9.4GB)
 │  ├ images
 │  └ annotations
 ├ mva2023_sod4bird_pub_test (8.7GB)
 │  ├ images
 │  └ annotations(including an empty annotation file)
 └ mva2023_sod4bird_private_test (4kB)
    ├ images(empty)
    └ annotations(empty)
 ```   

## Repo Structure

```
├── code
│   ├── project_640.ipynb
│   ├── project_640.py
│   ├── config
│       ├── base
│           ├── coco_detection.py
│           ├── faster_rcnn_r50_fpn.py
│           └── faster_rcnn_r50_fpn_1x_coco.py
│       └── faster_rcnn_r50_fpn_1x_bird.py
└── data
```

Usage

1. Clone this repository to your local machine.

2. Download the dataset from the provided Google Drive link and place it in the appropriate directory.

3. Install the required dependencies by running pip install -r requirements.txt.

4. Run the Jupyter Notebook or Python script to train and evaluate the bird detection model.

License

This project is licensed under the MIT License. See the LICENSE file for more information.

