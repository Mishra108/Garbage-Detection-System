# 🗑️ Garbage Detection System using YOLOv8

## Overview

This project is a Garbage Detection System built using YOLOv8 for real-time waste detection and localization in images and videos. The model identifies garbage objects and displays bounding boxes with confidence scores.

## Live link : https://mishra108-garbage-detection-system-appapp-hf-deploy-ezy8ta.streamlit.app/

## Features

* Image Upload Detection
* Video Upload Detection
* Real-time Object Localization
* Bounding Box Visualization
* Confidence Score Display
* Streamlit Web Application

## Dataset Strategy

To improve model robustness, multiple garbage detection datasets were explored and combined:

* Roboflow Garbage Detection Dataset
* UAVVaste Dataset

The datasets were cleaned, standardized, and converted to YOLO format before training.

## Model Training

### Model

* YOLOv8n (Nano Version)

### Training Platform

* Google Colab (T4 GPU)

### Training Configuration

* Image Size: 640
* Epochs: 50+
* Transfer Learning using COCO-pretrained weights

### Data Augmentation

* Horizontal Flip
* Mosaic Augmentation
* Brightness/Contrast Variation
* Scale Jitter

## Project Structure

```text
Garbage-Detection-System/
│
├── app/
│   └── app.py
│
├── models/
│   └── weights/
│       └── best.pt
│
├── training_artifacts/
│   ├── results.png
│   ├── confusion_matrix.png
│   └── val_predictions.jpg
│
├── requirements.txt
├── README.md
└── training_report.md
```

## Installation

```bash
git clone <repository-url>
cd Garbage-Detection-System

pip install -r requirements.txt
streamlit run app/app.py
```

## Usage

### Image Detection

1. Upload an image.
2. Model detects garbage objects.
3. Bounding boxes and confidence scores are displayed.

### Video Detection

1. Upload a video file.
2. Detection runs frame-by-frame.
3. Results are displayed with bounding boxes.

## Results

The trained model was evaluated using YOLOv8 validation metrics.

Metrics reported:

* mAP@50
* mAP@50-95
* Precision
* Recall
* Confusion Matrix

> Update the metrics section with your final training results before submission.

## Training Artifacts

* best.pt
* results.png
* confusion_matrix.png
* val_predictions.jpg
* training_report.md

## Tech Stack

* Python
* YOLOv8
* Ultralytics
* OpenCV
* Streamlit
* NumPy
* Pillow

## Future Improvements

* Live Webcam Detection
* Detection History Logging
* Class-wise Detection Summary
* FastAPI Inference Endpoint
* Mobile Responsive Interface

## Author

Prem Mishra

Machine Learning & AI Enthusiast
