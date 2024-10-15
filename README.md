# Fabric Detection Model - Development Branch

## Overview

This is the **development** branch of the Fabric Detection Model project. The branch contains ongoing development work, including the folder structure setup and initial versions of the training pipeline. This branch is actively being updated with new features, improvements, and experimental code.

The goal of this project is to create a machine learning model capable of detecting and classifying various fabric types (e.g., corduroy, denim, linen) from images, using a modular pipeline for training, image processing, feature extraction, and deployment.

## Features in Development

- **Training Pipeline**: In-progress implementation of the pipeline for training the fabric classification model.
- **Image Processing Pipeline**: Modular image preprocessing and enhancement for optimal classification.
- **Feature Extraction**: Techniques being developed to extract relevant features from fabric images.
- **Deployment Pipeline**: Code for deploying the model, under active development.

## Branch Purpose

The **development** branch is a workspace for integrating, testing, and refining new features before they are merged into the stable **main** branch. It is used for:
- Implementing new functionalities (e.g., pipelines, utilities).
- Integrating different components like image processing, feature extraction, and model training.
- Testing and validating code before moving it to the **main** branch.

This branch may contain incomplete or experimental code and should not be used for production purposes.

## Project Structure

- **`artifacts/`**: Temporary storage for intermediate outputs such as models and processed images.
- **`common/`**: Utility scripts like configuration management.
- **`deployment/`**: Code for deploying the model, including configurations for AWS Elastic Beanstalk.
- **`training/`**: Code for the training pipeline.
- **`final_train_pipeline/`**: Contains final, stable training pipeline code before merging into the development branch.
- **`deployment_pipeline/`**: Contains the deployment pipeline code under development.
- **`requirements.txt`**: Lists dependencies for development and testing purposes.

## Installation

To work on the development branch, set up the environment as follows:

### Prerequisites

- Python 3.8+
- Virtual environment (recommended for isolated development)
- AWS account (for deployment pipeline testing)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/fabric_detection_model.git
    cd fabric_detection_model
    git checkout development
    ```

2. **Set up Virtual Environment** (optional):
    ```bash
    python -m venv fabric_dev_env
    source fabric_dev_env/bin/activate   # For Linux/Mac
    fabric_dev_env\Scripts\activate      # For Windows
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Run the Flask Application for Development**:
    This will allow you to test new features locally.
    ```bash
    python deployment/app.py
    ```

## Contribution Workflow

To contribute to this project, please follow these steps:

1. **Create a New Feature Branch**:
   Branch off from `development` to create a new feature branch for your work.
   ```bash
   git checkout -b feature/your-feature-name

2. **Make Your Changes**:
     Develop and test your code within this branch.
     
3. **Push to Remote**: Push your feature branch to the remote repository for review.
```bash
git push origin feature/your-feature-name
```
4. **Submit a Pull Request**: Open a pull request to merge your feature branch into development.

