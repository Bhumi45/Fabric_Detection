# Fabric Detection Model - Final Training Pipeline Branch

## Overview

This branch, **final_train_pipeline**, contains the final code for the machine learning model's training pipeline. 
The code here has been thoroughly tested and is ready to be merged into the **development** branch. 
The goal of this branch is to offer a stable and well-optimized pipeline for training the fabric classification model using image data.

The model is designed to classify fabric types corduroy and denimusing advanced image processing and machine learning techniques.

## Pipeline components:

### 1. Nested Cross Validation
- **Data Ingestion**: The pipeline reads and processes images from specified directories.
- **Data Validation**: The pipeline validates whether all data is images or not.
- **Feature Extraction**: Key features from fabric images are extracted using techniques like Local Binary Patterns (LBP), Gabor filters and Canny Edge Detection.
- **Nested Cross-Validation**: Performs the nested cross-validation to ensure the robustness of the model.

### 2. Final Model Training
- **Data Ingestion**: The pipeline reads and processes images from specified directories.
- **Data Validation**: The pipeline validates whether all data is images or not.
- **Feature Extraction**: Key features from fabric images are extracted using techniques like Local Binary Patterns (LBP), Gabor filters and Canny Edge Detection.
- **Feature Engineering** - Standardizes the features and performs dimensionality reduction using Principal Component Analysis(PCA).
- **Model Training**: Performs the final model training on the entire training data by using the best model selected from the *Nested Cross Validation Component* .
- **Model Evaluation** - The final model trained on the entire training data is evaluated on the test data and the metrics are saved at artifacts/model_evaluation/metrics.json
- 
## Key Files

- **`execute_cross_validation.py`**: Runs nested cross-validation to identify the best model.
- **`execute_final_model_training.py`**: Script for training the final model on the entire training data.


## Installation

Follow the steps below to set up the environment:

### Prerequisites

- Python 3.8+
- Virtual environment (recommended)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/fabric_detection_model.git
    cd fabric_detection_model
    git checkout final_train_pipeline
    ```

2. **Set up Virtual Environment** (optional):
    ```bash
    python -m venv fabric_train_env
    source fabric_train_env/bin/activate   # For Linux/Mac
    fabric_train_env\Scripts\activate      # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

## Running the Training Pipeline

To train the model, execute the following command:

```bash
python execute_cross_validation.py
python execute_final_model_training.py
```
