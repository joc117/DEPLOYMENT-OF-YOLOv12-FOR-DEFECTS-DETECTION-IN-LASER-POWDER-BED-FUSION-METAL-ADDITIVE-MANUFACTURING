DEPLOYMENT OF YOLOv12 FOR DEFECTS DETECTION IN LASER-BED FUSION METAL ADDITIVE MANUFACTURING

Table below shows the result of our 3 models, namely (1) Dataset A (2) Dataset B (3) Dataset A + B

| Model  | Class   | Images | Instances | Box Precision | Recall | mAP50 | mAP50-95 |
|--------|---------|--------|-----------|---------------|--------|-------|----------|
|   1    | all     | 87     | 2937      | 0.872         | 0.749  | 0.816 | 0.605    |
|   2    | all     | 75     | 241       | 0.631         | 0.477  | 0.536 | 0.303    |
|   3    | Dataset A | 108  | 3688      | 0.700         | 0.614  | 0.651 | 0.280    |
|   3    | Dataset B | 67   | 261       | 0.579         | 0.521  | 0.555 | 0.336    |

Code splitting and preprocessing the images is included in Prepocessing ORNL.ipynb

Code running the YOLOv12 model is included in training_model.ipynb
