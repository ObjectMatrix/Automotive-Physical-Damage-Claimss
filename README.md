### Automotive-Physical-Damage-Claimss
- When an automotive physical damage loss is reported, the data is collected using First Notice of Loss (FNOL) channels. 
FNOL aims to obtain consistent and accurate data about the claim to guide segmentation and consequent assignment of the claim to the right resource for handling. 

- After the FNOL process, a review process starts where the claim is registered, segmented, and assigned to an adjuster. Not all claims are properly segmented on the first try. Inaccurate segmentation leads to additional costs, delays in claims processing, and poor customer experience. Recent advancements in computer vision may enable Liberty Mutual to identify relevant features in images to consistently and accurately answer questions in the FNOL process. This project explores the use of computer vision models to help answer FNOL questions, increase the accuracy and efficiency of the process, and obtain better segmentation outcomes. The assignment could include several areas of focus including data annotation and labeling, data engineering, machine learning model training, model evaluation, engineering, and the communication of results with stakeholders. Experience Required: • Project management skills, detail-oriented • Strong Python coding skills • Knowledge of fundamental machine learning concepts with a focus on computer vision • Ability to analyze model output and report results using visualization tools (e.g. matplotlib, seaborn, etc.) • Experience working on the cloud (e.g. Cortex) Using Computer Vision to Assess Appetite for Business Lines Underwriting Duration: 3 months | Openings: 1 | Location: US | Exemption Status: Exempt only Assignment Description: Insurance underwriters currently face the challenge of manually extracting risk-related information from diverse data sources and include both text and images. This underwriting research process is not only time-consuming but also prone to error. Recent advancements in computer vision enable us to identify relevant features in images associated with undesirable risk characteristics. This project seeks to explore the use of computer vision models to inform underwriters of potential risks, increase underwriting efficiency, and improve underwriting decisions. The assignment could include several areas of focus including data annotation and labeling, data engineering, machine learning model training, model evaluation, engineering, and the communication of results with stakeholders.


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
