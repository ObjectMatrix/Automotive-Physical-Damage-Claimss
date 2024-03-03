### Automotive-Physical-Damage-Claimss
When a car sustains damage, the initial details are gathered through First Notice of Loss (FNOL) methods. The goal of FNOL is to collect precise and consistent information on the claim to ensure it's directed to the appropriate resource for management.

Following the FNOL stage, a review phase commences, involving the claim's registration, segmentation, and allocation to an adjuster. However, not every claim is accurately segmented initially, leading to increased costs, processing delays, and dissatisfaction among customers. The potential application of computer vision technology at Auto and Home Insurance industry could improve the precision in identifying crucial image details during the FNOL phase, enhancing both the accuracy and the speed of the process, and resulting in better segmentation. The project may cover various aspects such as data marking, data management, training of machine learning models, their assessment, and engineering.

Insurance underwriters currently have the laborious task of manually sifting through varied data sources to pinpoint risk-related information, which is both inefficient and error-prone. The emergence of computer vision technology offers a promising solution to detect specific image features indicative of potential risks. This project aims to employ computer vision models to alert underwriters about potential risks, thereby streamlining the underwriting process and enhancing decision-making. The project could encompass tasks like data marking, data management, training and evaluating machine learning models, engineering, and sharing findings with relevant parties.






```
### Config.YAML
path: /content/drive/MyDrive/input/YOLO/source/images
train: /content/drive/MyDrive/input/YOLO/source/images
val: /content/drive/MyDrive/input/YOLO/source/images/

nc: 14

# Classes

names:
  - door-damage 
  - door-severe-damage
  - hood
  - windshield
  - trunk
  - dent
  - window
  - bumper
  - mirror
  - headlight
  - totaled
  - rear-windshield-damage
  - Damaged Car
  - Umdamaged Car
```
coco yolo format: https://docs.ultralytics.com/datasets/detect/coco8/
```
path: /content/drive/MyDrive/input/YOLO/source/images
train: /content/drive/MyDrive/input/YOLO/source/images
val: /content/drive/MyDrive/input/YOLO/source/images/

nc: 14

# Classes

names:
  0: Damaged Car
  1: Undamaged Car
  2: bumper
  3: dent
  4: door-damage
  5: door-severe-damage
  6: headlight
  7: hood
  8: mirror
  9: rear-windshield-damage
  10: totaled
  11: trunk
  12: window
  13: windshield
```

### Label Studio
- installation: `pip install -U label-studio`  
- unlimit images: `DATA_UPLOAD_MAX_NUMBER_FILES=1000000000 label-studio`

#### References:
A guide to convolution arithmatics for deep learning:
https://arxiv.org/pdf/1603.07285.pdf
